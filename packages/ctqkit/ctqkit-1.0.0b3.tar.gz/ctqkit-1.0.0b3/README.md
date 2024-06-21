# CtqKit
[![License](https://img.shields.io/github/license/Qiskit/qiskit.svg?)](https://opensource.org/licenses/Apache-2.0) <!--- long-description-skip-begin -->


CTQit Python SDK
本项目由国盾量子计算云平台，中电信天衍量子计算云平台，中科院量子创新研究院开发团队联合开发，
包含新建量子实验、保存量子实验、运行量子实验、查看量子实验结果等多个实验操作接口

## 结构说明
CTQit Python SDK主要包括以下模块:
+ quantum_platform--实验模块，定义新建实验和实验集合、保存实验、提交运行实验、查看实验结果、停止实验等接口
+ utils--工具模块，实现了qasm转qcis、qcis转qasm、化简量子电路等功能
+ visualization--可视化模块，实现了可视化量子电路，拓扑图，直方图等功能
+ simulator--模拟器模块，实现了模拟器接口
+ qalgo--算法模块
+ benchmark--算法模块

## 文档
文档使用sphinx搭建，包含入门教程和API说明。

[ctqkit_docs](https://ctqkit.readthedocs.io/en/latest/index.html)

## 安装
推荐使用 `pip` 安装 ctqkit:
```bash
pip install ctqkit
```


## License
[Apache License 2.0](LICENSE)