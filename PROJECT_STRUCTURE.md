# DSS-Gymnasium 项目结构

## 概述

本文档描述了DSS-Gymnasium项目的清晰目录结构。此结构将代码、数据、配置和输出文件进行了模块化组织，便于维护和扩展。

## 项目结构

```
DSS-Gymnasium/
├── README.md                          # 项目说明文档
├── PROJECT_SUMMARY.md                 # 项目总结
├── LICENSE                            # 许可证
├── PROJECT_STRUCTURE.md               # 本文档
│
├── src/                               # 源代码
│   ├── environments/                  # Gymnasium环境
│   │   └── simple_pv_env.py          # 简单PV控制环境
│   ├── agents/                        # 强化学习代理
│   │   └── (待扩展)
│   └── utils/                         # 工具函数
│       └── (待扩展)
│
├── scripts/                           # 执行脚本
│   ├── train_simple_pv.py            # 简单PV环境训练脚本
│   └── (待扩展)
│
├── config/                            # 配置文件
│   └── requirements.txt              # Python依赖包
│
├── data/                              # 数据文件
│   ├── datasets/                      # 数据集
│   │   ├── load_profiles/            # 负载配置文件
│   │   │   ├── LoadShape1.CSV        # 居民负载
│   │   │   ├── LoadShape2.CSV        # 商业负载
│   │   │   └── LoadShape3.CSV        # 工业负载
│   │   ├── solar_data/               # 太阳能数据
│   │   │   └── pv_profile_60min.csv  # NREL太阳能辐照度数据
│   │   └── weather/                  # 天气数据
│   │       └── dallas_tx_pv_temp_60min.csv  # 温度数据
│   │
│   └── ieee_systems/                  # IEEE测试系统
│       ├── ieee123/                   # IEEE 123节点系统
│       │   ├── IEEE123Master.dss     # 主电路文件
│       │   ├── IEEE123Loads.DSS      # 负载定义
│       │   ├── IEEE123Regulators.DSS # 调节器定义
│       │   ├── IEEELineCodes.DSS     # 线路代码
│       │   └── (其他支持文件)
│       │
│       ├── ieee13/                    # IEEE 13节点系统
│       │   ├── IEEE13Nodeckt.dss     # 主电路文件
│       │   ├── IEEELineCodes.DSS     # 线路代码
│       │   └── (其他支持文件)
│       │
│       └── ieee34/                    # IEEE 34节点系统
│           ├── ieee34Mod1.dss        # 模式1主电路
│           ├── ieee34Mod2.dss        # 模式2主电路
│           ├── IEEELineCodes.DSS     # 线路代码
│           └── (其他支持文件)
│
├── examples/                          # 示例代码
│   ├── basic/                         # 基础示例
│   │   └── (待扩展)
│   │
│   ├── advanced/                      # 高级示例
│   │   ├── ieee123_single_pv/        # IEEE 123节点单PV系统
│   │   │   ├── dss_circuit_123bus_singlePV.py
│   │   │   ├── gymnasium_env_123bus_singlePV.py
│   │   │   └── singlePV_agent_123bus.py
│   │   │
│   │   └── ieee34_local_pv/          # IEEE 34节点本地PV系统
│   │       ├── agent_train_34bus.py
│   │       ├── dss_circuit_34bus.py
│   │       ├── gymnasium_env_34bus.py
│   │       └── (其他支持文件)
│   │
│   └── experiments/                   # 实验示例
│       └── emergency_restoration/     # 应急恢复
│           └── RandomFaultTrainingCode/
│               ├── DQNTrainModelieee123SaveBestRandomFault.py
│               ├── IEEE123nodeRandomFaultSWpwrsENV0912.py
│               └── (其他支持文件)
│
├── tests/                             # 测试文件
│   └── (待扩展)
│
└── output/                            # 输出结果
    ├── dqn_pv_voltvar.zip            # 预训练模型
    └── tensorboard/                   # TensorBoard日志
        ├── DQN_PV_VoltVAR_1/
        ├── DQN_PV_VoltVAR_2/
        └── DQN_PV_VoltVAR_3/
```

## 目录说明

### src/ (源代码)
包含项目的核心代码实现：
- **environments/**: Gymnasium环境实现
- **agents/**: 强化学习代理实现
- **utils/**: 工具函数和通用代码

### scripts/ (执行脚本)
包含可执行的训练和测试脚本：
- **train_simple_pv.py**: 简单PV控制环境的DQN训练脚本

### config/ (配置文件)
包含项目配置和依赖信息：
- **requirements.txt**: Python依赖包列表

### data/ (数据文件)
按类型组织的数据文件：
- **datasets/**: 原始数据集
  - **load_profiles/**: 负载配置文件（居民、商业、工业）
  - **solar_data/**: 太阳能辐照度数据
  - **weather/**: 天气数据（温度等）
- **ieee_systems/**: IEEE标准测试系统
  - **ieee123/**: IEEE 123节点系统
  - **ieee13/**: IEEE 13节点系统  
  - **ieee34/**: IEEE 34节点系统

### examples/ (示例代码)
按复杂度组织的示例和实验：
- **basic/**: 基础示例（待扩展）
- **advanced/**: 高级示例（完整实现）
  - **ieee123_single_pv/**: IEEE 123节点单PV系统控制
  - **ieee34_local_pv/**: IEEE 34节点本地PV控制
- **experiments/**: 实验性代码
  - **emergency_restoration/**: 故障恢复场景

### tests/ (测试文件)
单元测试和集成测试（待扩展）

### output/ (输出结果)
训练和实验的输出：
- **dqn_pv_voltvar.zip**: 预训练的DQN模型
- **tensorboard/**: TensorBoard训练日志

## 使用指南

### 快速开始

1. **安装依赖**
   ```bash
   pip install -r config/requirements.txt
   ```

2. **运行基础训练**
   ```bash
   python scripts/train_simple_pv.py
   ```

3. **查看训练结果**
   ```bash
   tensorboard --logdir output/tensorboard
   ```

### 文件路径更新

项目重构后，所有文件路径都已更新为相对路径：

```python
# 获取项目根目录
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))

# 构建IEEE 123节点系统路径
ieee123_dir = os.path.join(project_root, 'data', 'ieee_systems', 'ieee123')
dss_file = os.path.join(ieee123_dir, 'IEEE123Master.dss')
```

### 添加新组件

- **新环境**: 添加到 `src/environments/`
- **新代理**: 添加到 `src/agents/`
- **新数据集**: 添加到 `data/datasets/`
- **新示例**: 添加到 `examples/basic/` 或 `examples/advanced/`

## 数据文件详情

### 负载配置文件
- **LoadShape1.CSV**: 居民负载模式
- **LoadShape2.CSV**: 商业负载模式
- **LoadShape3.CSV**: 工业负载模式

### 太阳能数据
- **pv_profile_60min.csv**: NREL NSRDB太阳能辐照度数据
  - 位置：德克萨斯州中部
  - 时间：2006年全年
  - 分辨率：每小时

### 天气数据
- **dallas_tx_pv_temp_60min.csv**: 温度数据
  - 位置：达拉斯，德克萨斯州
  - 用途：PV效率建模

### IEEE测试系统
- **IEEE 123节点**: 主测试系统，包含25个子系统
- **IEEE 13节点**: 紧凑型测试系统
- **IEEE 34节点**: 延伸型测试系统

## 输出文件

### 预训练模型
- **dqn_pv_voltvar.zip**: 完整的DQN模型，可直接加载使用

### 训练日志
- **tensorboard/**: TensorBoard日志文件
  - 包含训练曲线、损失函数、奖励函数等指标

## 版本信息

- **当前版本**: 2.0 (重构版本)
- **最后更新**: 2026-01-01
- **重构内容**: 模块化目录结构，路径标准化，文件组织优化

## 联系信息

如有问题或建议，请查看项目文档或提交Issue。