# 阶段3：机器学习与数据挖掘

## 🎯 学习目标

掌握数据分析与传统机器学习算法，能够完成端到端机器学习项目。通过本阶段学习，你将能够：

- 熟练使用 NumPy、Pandas、Matplotlib 进行数据分析
- 理解并应用传统机器学习算法（分类、回归、聚类、集成学习）
- 完成真实场景的数据分析项目
- 掌握数据预处理、特征工程、模型评估等核心技能

## 📚 课程模块

### [M01：科学计算库](01-scientific-computing/README.md)

学习 Python 数据科学核心工具栈：

- **NumPy**：多维数组计算、矩阵运算、数学函数
- **Pandas**：DataFrame 操作、数据清洗、分组聚合
- **Matplotlib**：数据可视化、图表绘制

**学习时长**：1-2 小时

### [M02：Pandas 实战](02-pandas-practice/README.md)

通过真实案例深入掌握 Pandas：

- 数据读取与导出（CSV、Excel、SQL）
- 数据清洗与转换
- 时间序列分析
- 高级分组与透视表

**学习时长**：2-3 小时

### [M03：AI 数学基础](03-ml-basics/README.md)

机器学习必备数学知识：

- 线性代数基础
- 概率统计
- 微积分与梯度下降
- 信息论基础

**学习时长**：2-3 小时

### [M04：机器学习进阶](04-ml-advanced/README.md)

掌握传统机器学习算法与应用：

- **监督学习**：线性回归、逻辑回归、决策树、支持向量机
- **无监督学习**：K-means 聚类、层次聚类、主成分分析
- **集成学习**：随机森林、GBDT、XGBoost、LightGBM
- **模型评估**：交叉验证、混淆矩阵、ROC/AUC

**学习时长**：4-6 小时

## 🚀 项目实战

本阶段包含 **9 个真实场景的数据分析项目**，覆盖医疗、电商、金融、通讯等行业：

| 项目 | 名称 | 技术栈 | 难度 |
|------|------|--------|------|
| [P01](projects/p01-healthcare/README.md) | 朝阳医院指标搭建及销售数据汇总 | Pandas + Matplotlib | ⭐⭐ |
| [P02](projects/p02-ecommerce/README.md) | 服装零售销售数据分析（优衣库4P分析） | Pandas + RFM 分析 | ⭐⭐⭐ |
| [P03](projects/p03-finance/README.md) | 银行电话营销活动分析 | 分类模型 + 评估 | ⭐⭐⭐ |
| [P04](projects/p04-telecom/README.md) | 通讯公司客户响应速度提升 | RFM 分析 + 客户分层 | ⭐⭐⭐ |
| [P05](projects/p05-retail/README.md) | 零售超市经营分析 | SWOT 分析 | ⭐⭐ |
| [P06](projects/p06-internet/README.md) | 滴滴出行运营数据异常分析 | 异常检测 | ⭐⭐⭐ |
| [P07](projects/p07-ecommerce-annual/README.md) | 淘宝百万级用户行为分析 | 大数据分析 + 年度复盘 | ⭐⭐⭐⭐ |
| [P08](projects/p08-airline/README.md) | 航空公司客户价值分析 | K-means 聚类 | ⭐⭐⭐ |
| [P09](projects/p09-credit/README.md) | 信用贷款前审批项目 | 风控模型 + 集成学习 | ⭐⭐⭐⭐ |

### 项目特点

✅ **真实数据**：基于真实行业场景的数据集
✅ **端到端**：从数据探索到模型部署的完整流程
✅ **代码质量**：遵循 PEP 8 规范，包含类型注解和文档字符串
✅ **双模式**：提供 Jupyter Notebook（教学版）和 Python 脚本（生产版）

## ⏱️ 学习时长

- **理论学习**：8-12 小时（4 个模块）
- **项目实战**：18-27 小时（9 个项目，每个 2-3 小时）
- **总计**：26-39 小时

建议学习节奏：
- **速通模式**（1-2周）：专注核心模块 + 3-4 个项目
- **深度学习模式**（3-4周）：完成所有模块 + 全部 9 个项目

## 🛠️ 环境准备

### 系统要求

- Python ≥3.9（推荐 3.11+）
- 内存：8GB+（16GB 推荐）
- 磁盘空间：约 2GB（数据集）
- 运行环境：CPU 即可（无需 GPU）

### 快速安装

```bash
# 1. 安装 uv 包管理器
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. 创建虚拟环境
uv venv --python 3.11
source .venv/bin/activate

# 3. 安装阶段3依赖
uv pip install -e ".[stage3]"

# 4. 下载数据集（~2GB）
python scripts/data/download-stage3.py

# 5. 验证环境
python scripts/env/check-stage3.py
```

详细的跨平台配置指引：
- [macOS Intel](../cross-platform/setup-macos-intel.md)
- [macOS Apple Silicon](../cross-platform/setup-macos-arm64.md)
- [Linux](../cross-platform/setup-linux.md)
- [Windows 原生](../cross-platform/setup-windows-native.md)
- [Windows WSL2](../cross-platform/setup-windows-wsl2.md)

## 📖 学习路径建议

### 新手路径（按顺序学习）

1. **M01 科学计算库** → 掌握基础工具
2. **M02 Pandas 实战** → 熟悉数据操作
3. **P01 医疗数据分析** → 第一个完整项目
4. **M03 AI 数学基础** → 理解算法原理
5. **M04 机器学习进阶** → 学习核心算法
6. **P03 银行营销分析** → 实战分类模型
7. **P08 航空客户价值** → 实战聚类算法
8. 选做其他 6 个项目巩固技能

### 有经验者路径（可跳过部分模块）

- 如果熟悉 NumPy/Pandas → 直接从 **M04** 或项目开始
- 如果已学过传统 ML → 直接做高难度项目（P07、P09）
- 如果想快速进入深度学习 → 完成 P01-P03 后进入[阶段4](../stage4/index.md)

## 🎓 前置知识要求

✅ **必须掌握**：
- Python 基础语法（变量、函数、类、模块）
- 基本数据结构（列表、字典、集合）
- 文件读写与异常处理

❓ **有帮助但非必须**：
- Linux 命令行基础
- Git 版本控制
- SQL 基础

不满足前置要求？查看我们的[先修课程推荐](../prerequisites.md)

## 🔗 相关资源

- [官方文档](https://shychee.github.io/py_ai_tutorial/)
- [GitHub 仓库](https://github.com/shychee/py_ai_tutorial)
- [问题反馈](https://github.com/shychee/py_ai_tutorial/issues)
- [贡献指南](../contributing.md)

## ⏭️ 下一步

完成阶段3后，继续学习：
- **[阶段4：深度学习](../stage4/index.md)** - PyTorch/TensorFlow + CV/NLP
- **[阶段5：AIGC与大模型](../stage5/index.md)** - LangChain + RAG + Agent

---

**准备好了吗？从 [M01：科学计算库](01-scientific-computing/README.md) 开始你的 AI 学习之旅！** 🚀
