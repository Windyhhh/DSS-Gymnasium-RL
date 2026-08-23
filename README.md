# 🎮 DSS-Gymnasium 强化学习环境 | DSS-Gymnasium RL Environment

> **基于 Gymnasium 的动态系统强化学习环境——自定义环境 + 多种 RL 算法实现，强化学习从入门到实战的完整项目。**
>
> *Dynamic system reinforcement learning environment based on Gymnasium — custom environment + multiple RL algorithm implementations, complete project from RL beginner to practitioner.*

---

## ⭐ 核心卖点 | Why Star This

| 卖点 | Feature | 一句话 |
|------|---------|--------|
| 🎮 **Gymnasium 环境** | Gymnasium Env | 遵循最新 Gymnasium API，兼容 Stable-Baselines3 |
| 🧩 **自定义环境** | Custom Env | 动态系统控制环境，状态/动作/奖励可定制 |
| 🤖 **多算法实现** | Multi-Algorithm | DQN、PPO、SAC、DDPG 等主流算法 |
| 📊 **训练可视化** | Training Viz | 奖励曲线、损失曲线、动作分布可视化 |
| 🧪 **可复现实验** | Reproducible | 完整训练脚本，一键复现实验结果 |

---

## 🏆 技术栈 | Tech Stack

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Gymnasium](https://img.shields.io/badge/Gymnasium-0.26+-green?logo=openai)
![PyTorch](https://img.shields.io/badge/PyTorch-1.10+-red?logo=pytorch)
![Stable-Baselines3](https://img.shields.io/badge/SB3-2.0+-orange?logo=stablebaselines3)
![NumPy](https://img.shields.io/badge/NumPy-1.20+-purple?logo=numpy)

---

## 📊 算法支持 | Algorithm Support

| 算法 | 类型 | 离散动作 | 连续动作 | 实现状态 |
|------|------|---------|---------|---------|
| DQN | Value-based | ✅ | ❌ | ✅ 完整 |
| Double DQN | Value-based | ✅ | ❌ | ✅ 完整 |
| Dueling DQN | Value-based | ✅ | ❌ | ✅ 完整 |
| PPO | Policy-based | ✅ | ✅ | ✅ 完整 |
| SAC | Actor-Critic | ❌ | ✅ | ✅ 完整 |
| DDPG | Actor-Critic | ❌ | ✅ | ✅ 完整 |
| A2C | Actor-Critic | ✅ | ✅ | ✅ 完整 |

---

## 🚀 快速开始 | Quick Start

```bash
git clone https://github.com/Windyhhh/DSS-Gymnasium-RL.git
cd DSS-Gymnasium-RL
pip install -r requirements.txt

# 使用 Stable-Baselines3 训练 PPO
python train.py --algo ppo --env DSS-v0 --timesteps 1000000

# 自定义算法训练 DQN
python train_dqn.py --env DSS-v0 --episodes 500

# 测试和可视化
python test.py --model checkpoint.zip --env DSS-v0 --render
```

---

## 📂 项目结构 | Project Structure

```
DSS-Gymnasium-RL/
├── train.py                   # 通用训练入口 (SB3)
├── train_dqn.py               # DQN 自定义训练
├── test.py                    # 测试和可视化
├── requirements.txt           # 依赖
├── envs/
│   ├── __init__.py            # 环境注册
│   └── dss_env.py             # 动态系统环境
├── algorithms/
│   ├── dqn/                   # DQN 系列
│   │   ├── dqn.py
│   │   ├── double_dqn.py
│   │   └── dueling_dqn.py
│   ├── ppo/                   # PPO
│   │   └── ppo.py
│   ├── sac/                   # SAC
│   │   └── sac.py
│   └── ddpg/                  # DDPG
│       └── ddpg.py
├── utils/
│   ├── replay_buffer.py       # 经验回放
│   ├── networks.py            # 神经网络
│   └── visualization.py       # 可视化工具
├── configs/                   # 配置文件
├── results/                   # 训练结果
└── README.md
```

---

## 🔬 环境设计 | Environment Design

### 动态系统环境 | Dynamic System Environment

```python
class DSSEnv(gym.Env):
    def __init__(self):
        self.observation_space = gym.spaces.Box(
            low=-np.inf, high=np.inf, shape=(state_dim,))
        self.action_space = gym.spaces.Box(
            low=-1, high=1, shape=(action_dim,))

    def step(self, action):
        # 动态系统状态转移
        next_state = self.transition(self.state, action)
        # 奖励函数
        reward = self.reward(self.state, action, next_state)
        # 终止条件
        done = self.is_done(next_state)
        return next_state, reward, done, info

    def reset(self):
        self.state = self.initial_state()
        return self.state
```

### 核心组件 | Core Components

| 组件 | 说明 | 可定制 |
|------|------|--------|
| 状态空间 | 系统状态的维度和范围 | ✅ |
| 动作空间 | 控制输入的维度和范围 | ✅ |
| 状态转移 | 动态系统的物理方程 | ✅ |
| 奖励函数 | 控制目标的量化 | ✅ |
| 终止条件 | 回合结束的判断 | ✅ |

---

## 📊 训练曲线 | Training Curves

项目包含完整的训练可视化：

- 📈 **奖励曲线**：每回合奖励随训练步数的变化
- 📉 **损失曲线**：Actor/Critic 损失变化
- 🎯 **动作分布**：动作输出的分布统计
- 🔄 **状态轨迹**：系统状态的演化轨迹

---

## 🎯 应用场景 | Use Cases

- 🎓 **强化学习教学**：RL 算法学习和对比的最佳平台
- 🧪 **算法研究**：新算法的基准测试环境
- 🎮 **控制理论**：动态系统控制的 RL 方法研究
- 🏭 **工业控制**：机器人、无人机等控制任务
- 🚗 **自动驾驶**：车辆控制策略的训练环境

---

## 📚 参考文献 | References

- Brockman, G., et al. "OpenAI Gym." arXiv 2016.
- Mnih, V., et al. "Human-level control through deep reinforcement learning." Nature 2015.
- Schulman, J., et al. "Proximal Policy Optimization Algorithms." arXiv 2017.
- Haarnoja, T., et al. "Soft Actor-Critic: Off-Policy Maximum Entropy Deep RL." ICML 2018.

---

## 📄 License

MIT License — 自由使用、修改和分发。

---

> 💡 **Gymnasium + 多算法 RL 实战项目，Star ⭐ 支持开源强化学习！**
