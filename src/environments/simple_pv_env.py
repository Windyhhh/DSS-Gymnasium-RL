"""
Simple Gymnasium environment for PV Volt-VAR control
This demonstrates the basic DSS-Gymnasium framework
"""

import gymnasium as gym
from gymnasium.spaces import Discrete, Box
import numpy as np
from opendssdirect import dss
import os

# Get local paths
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
ieee123_dir = os.path.join(project_root, 'data', 'ieee_systems', 'ieee123')
dss_file = os.path.join(ieee123_dir, 'IEEE123Master.dss')


class SimplePVEnv(gym.Env):
    """
    Simple PV Volt-VAR control environment
    
    Observation: Bus voltage (pu)
    Action: Discrete reactive power adjustment {-20, 0, +20} kvar
    Reward: Negative squared voltage deviation from 1.0 pu
    """
    
    def __init__(self):
        super().__init__()
        
        # Action space: 3 discrete actions
        # 0: decrease kvar by 20
        # 1: no change
        # 2: increase kvar by 20
        self.action_space = Discrete(3)
        
        # Observation space: bus voltage in pu [0.9, 1.1]
        self.observation_space = Box(
            low=np.array([0.9], dtype=np.float32),
            high=np.array([1.1], dtype=np.float32),
            dtype=np.float32
        )
        
        # Environment parameters
        self.max_steps = 24  # 24 hour simulation
        self.current_step = 0
        self.current_kvar = 0.0
        self.kvar_step = 20.0
        self.max_kvar = 66.0  # IEEE 1547 limit
        
        # Initialize circuit
        self._init_circuit()
        
    def _init_circuit(self):
        """Initialize the OpenDSS circuit"""
        dss.Command('ClearAll')
        dss.Command(f'Redirect "{dss_file}"')
        dss.Command('Set Loadmult=1.25')
        dss.Loads.Status(3)
        dss.Command('set ControlMode=OFF')
        dss.Command('solve')
        
        # Build XY curves
        self._build_xy_curves()
        
        # Build simple loadshapes
        self._build_loadshapes()
        
        # Add PV system
        dss.Command('New PVSystem.pv71 phases=1 bus1=71.1 kV=2.4 kVA=150 irrad=1 Pmpp=150 conn=wye'
                    ' temperature=25 effcurve=PV_eff P-TCurve=PV_temp Daily=irrad TDaily=temp'
                    ' %cutin=0.05 %cutout=0.05 kvarMax=66 kvarMaxAbs=66')
        
    def _build_xy_curves(self):
        """Build XY curves for PV"""
        # Temperature curve
        dss.Command('New XYCurve.PV_temp')
        temp_xarr = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
        power_yarr = np.array([0.82, 0.92, 0.97, 0.98, 0.99, 1.0, 0.99, 0.97, 0.89, 0.8, 0.75, 0.7, 0.65])
        dss.XYCurves.Npts(13)
        dss.XYCurves.XArray(temp_xarr)
        dss.XYCurves.YArray(power_yarr)
        
        # Efficiency curve
        dss.Command('New XYCurve.PV_eff')
        eff_xarr = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
        eff_yarr = np.array([0.75, 0.78, 0.8, 0.83, 0.86, 0.89, 0.93, 0.95, 0.97, 0.99])
        dss.XYCurves.Npts(10)
        dss.XYCurves.XArray(eff_xarr)
        dss.XYCurves.YArray(eff_yarr)
        
    def _build_loadshapes(self):
        """Build simple loadshapes"""
        num_steps = 24
        step_size = 60
        
        # PV irradiance (bell curve)
        pv_irrad = np.array([0, 0, 0, 0, 0, 0, 0.1, 0.3, 0.5, 0.7, 0.85, 0.95,
                             1.0, 0.95, 0.85, 0.7, 0.5, 0.3, 0.1, 0, 0, 0, 0, 0])
        
        dss.Command('New Loadshape.irrad')
        dss.LoadShape.Npts(num_steps)
        dss.LoadShape.MinInterval(step_size)
        dss.LoadShape.PMult(pv_irrad)
        
        # Temperature curve
        temp_curve = [15, 15, 14, 14, 13, 13, 14, 16, 18, 20, 22, 24,
                      26, 27, 28, 27, 25, 23, 21, 19, 18, 17, 16, 15]
        
        dss.Command(f'New Tshape.temp npts={num_steps} minterval={step_size} temp={temp_curve}')
        
    def _get_observation(self):
        """Get current bus voltage"""
        dss.Circuit.SetActiveBus('71')
        voltage_pu = dss.Bus.puVmagAngle()[0]
        return np.array([voltage_pu], dtype=np.float32)
    
    def _calculate_reward(self, voltage_pu):
        """Calculate reward based on voltage deviation from 1.0 pu"""
        # Negative squared error (want voltage close to 1.0 pu)
        reward = -(voltage_pu - 1.0) ** 2
        return reward
    
    def step(self, action):
        """Execute one step in the environment"""
        # Apply action to adjust kvar
        if action == 0:  # Decrease kvar
            self.current_kvar = max(-self.max_kvar, self.current_kvar - self.kvar_step)
        elif action == 2:  # Increase kvar
            self.current_kvar = min(self.max_kvar, self.current_kvar + self.kvar_step)
        # action == 1: no change
        
        # Set PV kvar and solve
        dss.PVsystems.Name('pv71')
        dss.PVsystems.kvar(self.current_kvar)
        dss.Command('solve')
        
        # Get observation
        observation = self._get_observation()
        
        # Calculate reward
        reward = self._calculate_reward(observation[0])
        
        # Check if done
        self.current_step += 1
        terminated = self.current_step >= self.max_steps
        truncated = False
        
        info = {
            'voltage_pu': observation[0],
            'kvar': self.current_kvar,
            'step': self.current_step
        }
        
        return observation, reward, terminated, truncated, info
    
    def reset(self, seed=None, options=None):
        """Reset the environment"""
        super().reset(seed=seed)
        
        self.current_step = 0
        self.current_kvar = 0.0
        
        # Reset circuit
        dss.Command('solve')
        
        observation = self._get_observation()
        info = {'voltage_pu': observation[0], 'kvar': self.current_kvar}
        
        return observation, info


if __name__ == '__main__':
    # Test the environment
    print("Testing SimplePVEnv...")
    env = SimplePVEnv()
    
    # Check environment
    from stable_baselines3.common.env_checker import check_env
    print("Checking environment...")
    check_env(env, warn=True)
    print("[OK] Environment check passed!")
    
    # Test a few steps
    print("\nTesting environment steps...")
    obs, info = env.reset()
    print(f"Initial observation: {obs}, info: {info}")
    
    for i in range(5):
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)
        print(f"Step {i+1}: action={action}, voltage={info['voltage_pu']:.4f}, kvar={info['kvar']:.1f}, reward={reward:.6f}")
        
        if terminated or truncated:
            break
    
    print("\n=== Environment test successful! ===")

