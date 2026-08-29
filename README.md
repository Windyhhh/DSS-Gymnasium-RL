<div align="center">

# 决策支持 RL 环境 | DSS-Gymnasium-RL

### Custom Gymnasium RL environments for a decision support system.

Reinforcement-learning environments built on Gymnasium for power-system decision support — IEEE 123-bus with solar & load profiles.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Gymnasium](https://img.shields.io/badge/Gymnasium-0.28-2EA44F)](https://gymnasium.farama.org/)

</div>

---

**DSS-Gymnasium-RL** provides custom **Gymnasium** reinforcement-learning environments for a decision-support system in power systems — grounded in the **IEEE 123-bus** model with solar PV and load-shape data.

> [!NOTE]
> 中文项目：决策支持系统自定义 RL 环境——Gymnasium，基于 IEEE 123 节点系统与太阳能/负荷数据。

---

## Quickstart

```bash
git clone https://github.com/Windyhhh/DSS-Gymnasium-RL.git
cd DSS-Gymnasium-RL

pip install -r config/requirements.txt

# explore environments & run an RL episode
python examples/...   # see PROJECT_STRUCTURE.md
```

Data (IEEE 123-bus `.dss`, load profiles, solar PV) ships in `data/`.

---

## Features

- **Custom Gymnasium envs** — RL-ready decision-support environments.
- **IEEE 123-bus** — realistic power-system topology and profiles.
- **Solar & load data** — PV, weather and load-shape datasets included.

---

## Project Structure

```
DSS-Gymnasium-RL/
├── config/requirements.txt
├── data/
│   ├── ieee_systems/ieee123/   # IEEE123 .dss + load shapes
│   └── datasets/               # load profiles, solar, weather
├── PROJECT_STRUCTURE.md
├── CONTRIBUTING.md
└── LICENSE
```

---

## 技术实现细节

### 架构概览

项目采用模块化设计，核心目录包括：**config, data, examples, output, scripts, src**。

### 核心类与模块

- **SimplePVEnv**

### 关键函数

- `step`, `reset`

### 技术栈与依赖

**核心框架/库**：NumPy

**主要 import**：
```python
from setuptools import setup, find_packages
import gymnasium as gym
from gymnasium.spaces import Discrete, Box
import numpy as np
from opendssdirect import dss
import os
from stable_baselines3.common.env_checker import check_env
```

### 实现要点

- 以 `SimplePVEnv` 为核心类，封装主要业务逻辑
- 通过 `step` 等函数实现核心流程编排
- 基于 NumPy 构建，保证技术栈成熟稳定
- 代码结构清晰，模块间低耦合，便于扩展和维护

---
## License

MIT — free to use, modify and distribute.
