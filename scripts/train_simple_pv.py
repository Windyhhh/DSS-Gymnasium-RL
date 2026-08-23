"""
Train a DRL agent for PV Volt-VAR control
Using DQN algorithm from Stable Baselines3
"""

import sys
import os

# Add src directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
src_dir = os.path.join(project_root, 'src')
sys.path.append(src_dir)

from environments.simple_pv_env import SimplePVEnv
from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy

# Create output directory
output_dir = os.path.join(project_root, 'output')
os.makedirs(output_dir, exist_ok=True)

print("=== Training DRL Agent for PV Volt-VAR Control ===\n")

# Create environment
print("Creating environment...")
env = SimplePVEnv()
print("[OK] Environment created\n")

# Create DQN model
print("Creating DQN model...")
model = DQN(
    policy="MlpPolicy",
    env=env,
    learning_rate=1e-3,
    buffer_size=10000,
    learning_starts=100,
    batch_size=32,
    gamma=0.99,
    exploration_fraction=0.3,
    exploration_initial_eps=1.0,
    exploration_final_eps=0.05,
    verbose=1,
    tensorboard_log=os.path.join(output_dir, 'tensorboard')
)
print("[OK] DQN model created\n")

# Train the model
print("Training model...")
print("This will run for 5000 timesteps (about 200 episodes)")
print("=" * 60)
model.learn(
    total_timesteps=5000,
    progress_bar=True,
    tb_log_name="DQN_PV_VoltVAR"
)
print("=" * 60)
print("[OK] Training complete\n")

# Save the model
model_path = os.path.join(output_dir, 'dqn_pv_voltvar.zip')
model.save(model_path)
print(f"[OK] Model saved to: {model_path}\n")

# Evaluate the trained policy
print("Evaluating trained policy...")
mean_reward, std_reward = evaluate_policy(
    model, 
    env, 
    n_eval_episodes=10,
    deterministic=True
)
print(f"Mean reward: {mean_reward:.4f} +/- {std_reward:.4f}\n")

# Test the trained agent
print("Testing trained agent on one episode...")
print("=" * 60)
obs, info = env.reset()
print(f"Initial: voltage={info['voltage_pu']:.4f} pu, kvar={info['kvar']:.1f}")

total_reward = 0
for step in range(24):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = env.step(action)
    total_reward += reward
    
    action_name = ['Decrease kvar', 'No change', 'Increase kvar'][action]
    print(f"Step {step+1:2d}: {action_name:15s} -> voltage={info['voltage_pu']:.4f} pu, kvar={info['kvar']:6.1f}, reward={reward:.6f}")
    
    if terminated or truncated:
        break

print("=" * 60)
print(f"Total reward: {total_reward:.4f}\n")

print("=== Training and Testing Complete! ===")
print(f"\nTo view training metrics with Tensorboard, run:")
print(f"  tensorboard --logdir {os.path.join(output_dir, 'tensorboard')}")
print(f"\nThen open http://localhost:6006 in your browser")

