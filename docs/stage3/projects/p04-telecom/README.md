# 项目P04：通讯公司客户响应速度提升

## 📋 项目概述

某通讯运营商面临日益激烈的市场竞争，客户流失率逐年上升。本项目通过 RFM 分析和机器学习模型，帮助公司识别高价值客户和潜在流失客户，从而制定针对性的营销策略。

### 项目目标

1. **RFM 分析**：通过最近消费时间(Recency)、消费频率(Frequency)、消费金额(Monetary)三个维度对客户进行价值评估
2. **客户细分**：基于 RFM 模型将客户划分为不同群体(高价值客户、流失风险客户等)
3. **流失预测**：构建机器学习模型预测客户流失概率，识别高风险客户
4. **策略建议**：为不同客户群体提供差异化的营销策略建议

### 业务价值

- ✅ 识别高价值客户，提供 VIP 服务，提升客户满意度和忠诚度
- ✅ 预测流失风险，提前干预，降低客户流失率
- ✅ 优化资源分配，将营销预算集中在高 ROI 客户群体
- ✅ 提升客户响应速度，改善整体服务水平

## 📊 数据集说明

### 数据格式

- **文件名**: `telecom_customer_data.csv`
- **文件大小**: 约 25 MB
- **样本数量**: 约 100,000 条客户记录
- **数据周期**: 2023年1月 - 2024年12月 (24个月)
- **流失率**: 约 15%（行业平均水平）

### 核心字段

| 字段名 | 类型 | 说明 |
|--------|------|------|
| customer_id | string | 客户唯一标识符 |
| last_transaction_date | date | 最后一次交易日期 |
| transaction_count | int | 交易次数(24个月内) |
| total_amount | float | 总消费金额(元) |
| churn | int | 是否流失(0=未流失, 1=已流失) |
| complaint_count | int | 投诉次数 |
| service_call_count | int | 客服呼叫次数 |

详细字段说明请查看[完整项目文档](../../../../projects/stage3/p04-telecom/README.md)

## 🎯 学习要点

本项目涵盖以下核心技能：

### 数据分析技能
- RFM 客户价值分析
- 客户细分与聚类（K-means）
- 数据可视化（客户分布图、价值矩阵）

### 机器学习技能
- 分类模型构建（逻辑回归、随机森林）
- 类别不平衡处理（SMOTE 过采样）
- 模型评估（混淆矩阵、ROC/AUC）

### 工程实践
- 模块化代码设计（数据加载、特征工程、模型训练分离）
- 配置文件管理（YAML）
- 日志记录与错误处理

## 🚀 快速开始

### 环境要求

- Python ≥3.9（推荐 3.11+）
- 内存：至少 4GB（推荐 8GB+）
- CPU 即可运行（无需 GPU）

### 方式 1：Jupyter Notebook（推荐新手）

```bash
# 1. 安装依赖
uv pip install -e ".[stage3]"

# 2. 启动 Jupyter Lab
jupyter lab

# 3. 打开 notebooks/stage3/p04-telecom-analysis.ipynb
# 按顺序运行每个 cell
```

### 方式 2：Python 脚本（推荐有经验者）

```bash
# 1. 进入项目目录
cd projects/stage3/p04-telecom

# 2. 运行分析脚本
python src/analyze.py --config configs/default.yaml

# 3. 查看输出结果
ls outputs/
# - figures/          # 可视化图表
# - reports/          # 分析报告
# - models/           # 训练好的模型
```

## 📈 预期结果

完成项目后，你将获得：

### 分析结果
- **客户价值分层**：将客户分为 8-10 个细分群体
- **流失预测模型**：AUC ≥ 0.80，召回率 ≥ 0.70
- **高价值客户占比**：识别出约 20% 的高价值客户（贡献 80% 收入）

### 可视化输出
- RFM 价值分布热力图
- 客户生命周期曲线
- 流失风险概率分布图
- 特征重要性排序图

### 策略建议
针对不同客户群体的营销策略建议文档

## 📚 项目文件

完整项目代码位于：`projects/stage3/p04-telecom/`

```
p04-telecom/
├── README.md              # 完整项目文档
├── src/                   # 源代码
│   ├── analyze.py         # 主分析脚本
│   ├── data/              # 数据加载模块
│   ├── models/            # 模型模块（RFM、流失预测）
│   └── utils/             # 工具函数
├── notebooks/             # Jupyter Notebook 教学版
│   └── analysis.ipynb
├── configs/               # 配置文件
│   └── default.yaml
├── tests/                 # 单元测试
└── outputs/               # 输出目录（生成）
```

## 🎓 相关资源

- [阶段3：机器学习与数据挖掘](../../index.md)
- [M02：Pandas 实战](../../02-pandas-practice/README.md)
- [M04：机器学习进阶](../../04-ml-advanced/README.md)
- [完整项目代码](../../../../projects/stage3/p04-telecom/)

## 🔗 其他项目

- [P01：医疗数据分析](../p01-healthcare/README.md)
- [P02：服装零售分析](../p02-ecommerce/README.md)
- [P03：银行营销分析](../p03-finance/README.md)
- **P04：通讯客户响应**（当前）
- [P05：零售超市分析](../p05-retail/README.md)

---

**开始学习？** 查看[完整项目文档](../../../../projects/stage3/p04-telecom/README.md)或直接运行 Notebook！
