# 项目P04：通讯公司客户响应速度提升

## 项目概述

### 项目背景

某通讯运营商面临日益激烈的市场竞争，客户流失率逐年上升。为了提升客户服务质量和响应速度,公司希望通过数据分析来识别高价值客户和潜在流失客户,从而制定针对性的营销策略和服务改进方案。

### 项目目标

1. **RFM分析**:通过最近消费时间(Recency)、消费频率(Frequency)、消费金额(Monetary)三个维度对客户进行价值评估
2. **客户细分**:基于RFM模型将客户划分为不同群体(如高价值客户、流失风险客户等)
3. **流失预测**:构建机器学习模型预测客户流失概率,识别高风险客户
4. **策略建议**:为不同客户群体提供差异化的营销策略建议

### 业务价值

- 识别高价值客户,提供VIP服务,提升客户满意度和忠诚度
- 预测流失风险,提前干预,降低客户流失率
- 优化资源分配,将营销预算集中在高ROI客户群体
- 提升客户响应速度,改善整体服务水平

## 数据集说明

### 数据来源

数据来自某通讯运营商的客户交易记录和行为数据(已脱敏处理,仅供教学使用)。

### 数据格式

- **文件名**: `telecom_customer_data.csv`
- **文件大小**: 约25 MB
- **样本数量**: 约100,000条客户记录
- **数据周期**: 2023年1月 - 2024年12月 (24个月)

### 字段说明

| 字段名 | 类型 | 说明 | 示例 |
|--------|------|------|------|
| customer_id | string | 客户唯一标识符 | "C000001" |
| registration_date | date | 注册日期 | "2023-01-15" |
| last_transaction_date | date | 最后一次交易日期 | "2024-10-20" |
| transaction_count | int | 交易次数(24个月内) | 48 |
| total_amount | float | 总消费金额(元) | 5680.50 |
| avg_amount_per_transaction | float | 平均单次消费金额(元) | 118.34 |
| service_type | string | 主要服务类型 | "移动套餐"/"宽带"/"固话" |
| contract_type | string | 合约类型 | "月付"/"年付"/"按量付费" |
| complaint_count | int | 投诉次数 | 2 |
| service_call_count | int | 客服呼叫次数 | 5 |
| churn | int | 是否流失(标签) | 0(未流失)/1(已流失) |
| age_group | string | 年龄段 | "18-25"/"26-35"/"36-45"/"46+" |
| region | string | 所在地区 | "华东"/"华北"/"华南"等 |

### 数据说明

- `churn`字段为目标标签:0表示客户仍在使用服务,1表示已流失(超过6个月无交易记录)
- 流失率约为15%(行业平均水平)
- 数据已完成基础清洗,但可能仍存在少量异常值需要处理
- 部分字段可能存在缺失值,需要在分析前进行处理

## 环境要求

### Python版本

- Python >= 3.9 (推荐 3.11+)

### 依赖库

核心依赖:
- pandas >= 2.1.0
- numpy >= 1.26.0
- scikit-learn >= 1.3.0
- matplotlib >= 3.8.0
- seaborn >= 0.13.0

开发依赖:
- pytest >= 7.4.0
- black >= 23.0.0
- mypy >= 1.5.0

### 硬件要求

- **CPU**: 现代多核处理器(推荐4核+)
- **内存**: 至少4GB(推荐8GB+)
- **存储**: 至少500MB可用空间
- **GPU**: 不需要(CPU即可运行)

## 快速开始

### 1. 环境配置

```bash
# 克隆项目(若未克隆)
git clone https://github.com/shychee/py_ai_tutorial.git
cd py_ai_tutorial

# 创建虚拟环境
uv venv --python 3.11
source .venv/bin/activate  # Windows: .\.venv\Scripts\Activate.ps1

# 安装依赖
uv pip install -e ".[stage3]"
```

### 2. 数据准备

```bash
# 下载项目数据集
python scripts/data/download-stage3.py --project p04-telecom

# 验证数据完整性
python scripts/data/verify.py --stage 3 --project p04-telecom
```

### 3. 运行分析脚本

```bash
cd docs/stage3/projects/p04-telecom

# 运行完整分析流程
python src/analyze.py --config configs/default.yaml

# 查看输出结果
ls outputs/
```

**预期输出**:
- `outputs/models/`: 训练好的流失预测模型(`churn_model.pkl`)
- `outputs/figures/`: RFM分析图表、客户细分可视化、特征重要性图等
- `outputs/reports/`: 分析报告(`report.md`)
- `outputs/experiment_info.json`: 实验元数据与指标

**运行时间**: 约2-3分钟(CPU环境)

### 4. 运行Jupyter Notebook(可选)

```bash
# 安装Jupyter Lab
uv pip install jupyterlab

# 启动Jupyter Lab
jupyter lab

# 在浏览器中打开 notebooks/analysis.ipynb
# 按顺序运行所有cell
```

## 项目结构

```
p04-telecom/
├── README.md                 # 项目说明(本文件)
├── pyproject.toml            # 项目配置与依赖
├── .python-version           # Python版本锁定(3.11)
├── data/                     # 数据目录(软链接到 ../../../../data/stage3/)
│   └── telecom_customer_data.csv
├── configs/
│   └── default.yaml          # 默认配置(RFM阈值、模型超参数等)
├── src/
│   ├── __init__.py
│   ├── analyze.py            # 主分析脚本(CLI入口)
│   ├── data/
│   │   ├── __init__.py
│   │   ├── loader.py         # 数据加载函数
│   │   └── preprocessor.py   # 数据预处理(缺失值、异常值处理)
│   ├── models/
│   │   ├── __init__.py
│   │   ├── rfm.py            # RFM分析模型
│   │   └── churn_predictor.py # 流失预测模型
│   └── utils/
│       ├── __init__.py
│       ├── logger.py         # 日志配置
│       ├── metrics.py        # 评估指标计算
│       └── visualization.py  # 可视化工具
├── notebooks/
│   └── analysis.ipynb        # Jupyter Notebook教学版
├── tests/
│   ├── __init__.py
│   ├── test_data_loader.py
│   └── test_rfm.py
└── outputs/                  # 输出目录(运行后生成)
    ├── models/
    │   └── churn_model.pkl
    ├── figures/
    │   ├── rfm_distribution.png
    │   ├── customer_segments.png
    │   ├── churn_prediction_roc.png
    │   └── feature_importance.png
    ├── logs/
    │   └── analysis.log
    └── reports/
        └── report.md
```

## 评估指标

### RFM分析指标

- **RFM评分**: R、F、M三个维度的评分(1-5分,5分最高)
- **客户细分准确性**: 各细分群体的样本分布是否合理(推荐分布: 冠军客户5-10%, 流失风险客户10-15%)

### 流失预测模型指标

#### 预期指标范围

基于随机森林分类器(默认配置):

| 指标 | 最小值 | 最大值 | 目标值 |
|------|--------|--------|--------|
| Accuracy(准确率) | 0.80 | 0.88 | ≥0.83 |
| Precision(精确率) | 0.70 | 0.85 | ≥0.75 |
| Recall(召回率) | 0.65 | 0.80 | ≥0.70 |
| F1-Score | 0.68 | 0.82 | ≥0.72 |
| AUC-ROC | 0.85 | 0.92 | ≥0.87 |

**说明**:
- 使用5折交叉验证,上述为平均值
- 由于数据存在随机性,允许±3%的波动
- 流失预测任务中,召回率(Recall)特别重要(避免遗漏高风险客户)

### 验证方法

```bash
# 运行评估脚本
python src/analyze.py --config configs/default.yaml

# 查看实验结果
cat outputs/experiment_info.json

# 输出示例:
# {
#   "timestamp": "2025-11-13T12:00:00Z",
#   "metrics": {
#     "accuracy": 0.851,
#     "precision": 0.782,
#     "recall": 0.745,
#     "f1_score": 0.763,
#     "auc_roc": 0.891
#   },
#   "rfm_summary": {
#     "champion_customers": 850,
#     "loyal_customers": 2300,
#     "at_risk_customers": 1200,
#     "churned_customers": 650
#   }
# }
```

如果你的指标在预期范围内,**恭喜!分析成功**。

## 交付物

### 必须提交的文件

1. **训练好的模型**
   - 位置: `outputs/models/churn_model.pkl`
   - 格式: pickle序列化的scikit-learn模型
   - 验证: 必须能成功加载并对测试数据进行预测

2. **实验报告**
   - 位置: `outputs/reports/report.md`
   - 格式: Markdown
   - 必须包含章节:
     - 项目背景与目标
     - 数据说明与预处理步骤
     - RFM分析结果(各细分客户群体特征)
     - 流失预测模型选择与超参数
     - 实验结果(指标、图表)
     - 业务建议(针对不同客户群体的策略)
     - 结论与改进方向

3. **评估指标文件**
   - 位置: `outputs/experiment_info.json`
   - 格式: JSON
   - 必须包含: timestamp、metrics、rfm_summary等字段

4. **可视化图表**
   - 位置: `outputs/figures/`
   - 格式: PNG或SVG
   - 必须包含:
     - RFM分布图(三维散点图或热力图)
     - 客户细分可视化(饼图或柱状图)
     - ROC曲线与AUC值
     - 特征重要性图(随机森林)
     - 混淆矩阵

### 可选提交的文件

- 训练日志: `outputs/logs/analysis.log`
- 测试集预测结果: `outputs/predictions.csv`
- 超参数搜索记录: `outputs/hyperparams.json`

## 评分标准

### 评分维度(总分100分)

1. **代码质量**(30分)
   - 遵循PEP 8规范(10分)
   - 类型注解与文档字符串完整(10分)
   - 异常处理与日志记录完善(10分)

2. **数据处理正确性**(25分)
   - 正确处理缺失值与异常值(10分)
   - RFM计算准确(10分)
   - 特征工程合理(5分)

3. **模型性能**(25分)
   - 流失预测指标达标(F1-Score ≥0.72)(15分)
   - 模型选择与调参合理(10分)

4. **分析深度**(15分)
   - RFM分析深入,客户细分有洞察(8分)
   - 业务建议可操作性强(7分)

5. **可视化质量**(5分)
   - 图表类型选择合理(3分)
   - 标题、标签、图例完整(2分)

### 及格线

- **总分 ≥60分**: 及格
- **总分 ≥80分**: 优秀

### 自我检查清单

- [ ] 代码通过`black`格式化检查
- [ ] 代码通过`mypy`类型检查
- [ ] 单元测试通过(`pytest tests/`)
- [ ] RFM分析结果包含至少4个客户细分群体
- [ ] 流失预测模型F1-Score ≥0.72
- [ ] 实验报告完整,包含所有必须章节
- [ ] 可视化图表清晰易读,至少5张图
- [ ] 所有输出文件路径符合规范

## 常见问题

### Q1: RFM分析中的R、F、M如何计算?

**A**:
- **Recency(最近消费时间)**: 当前日期 - 最后一次交易日期(天数),越小越好
- **Frequency(消费频率)**: 24个月内的交易次数,越多越好
- **Monetary(消费金额)**: 24个月内的总消费金额,越高越好

每个维度按五分位数(quintile)划分为1-5分,5分为最好。

### Q2: 如何处理类别不平衡问题(流失客户占15%)?

**A**:
1. 使用`class_weight='balanced'`参数(在scikit-learn分类器中)
2. 使用SMOTE过采样(可选,需安装`imbalanced-learn`)
3. 关注Precision-Recall曲线而非仅看Accuracy
4. 使用F1-Score或AUC-ROC作为主要评估指标

### Q3: 模型训练时间过长怎么办?

**A**:
1. 减少数据量进行快速验证(使用前10%数据)
2. 降低随机森林的`n_estimators`(如从100降到50)
3. 使用`n_jobs=-1`开启多核并行
4. 考虑使用更快的模型(如逻辑回归)

### Q4: 如何解释模型预测结果给业务团队?

**A**:
1. 使用特征重要性图展示哪些因素最影响流失(如投诉次数、服务类型等)
2. 针对高风险客户,输出具体特征值(如"该客户90天未交易,投诉3次")
3. 提供可操作的建议(如"建议对投诉次数>2的客户进行回访")
4. 使用业务语言而非技术术语(如"高流失风险"而非"churn概率0.8")

### Q5: 遇到错误"FileNotFoundError: telecom_customer_data.csv"

**A**:
1. 确认已运行数据下载脚本: `python scripts/data/download-stage3.py --project p04-telecom`
2. 检查数据目录是否正确: `ls data/` 应能看到 `telecom_customer_data.csv`
3. 若使用离线数据包,确认已解压到正确位置

### Q6: 如何提升模型性能?

**A**:
1. 特征工程: 尝试创建新特征(如"平均消费/交易次数"、"投诉率"等)
2. 超参数调优: 使用GridSearchCV或RandomizedSearchCV
3. 模型融合: 尝试多个模型(逻辑回归、XGBoost、LightGBM)并集成
4. 数据增强: 收集更多特征(如客户历史服务评分、家庭信息等)

## 学习资源

### 推荐阅读

1. **RFM分析**:
   - [RFM Analysis for Successful Customer Segmentation](https://www.putler.com/rfm-analysis/)
   - [Customer Segmentation using RFM Analysis](https://towardsdatascience.com/customer-segmentation-using-rfm-analysis-3c81c6fc0e52)

2. **客户流失预测**:
   - [Predicting Customer Churn](https://towardsdatascience.com/predict-customer-churn-with-python-e8cd6d3aaa7)
   - [Handling Imbalanced Datasets in Machine Learning](https://developers.google.com/machine-learning/data-prep/construct/sampling-splitting/imbalanced-data)

3. **scikit-learn文档**:
   - [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
   - [Classification metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics)

### 拓展项目

完成基础任务后,可尝试:
1. 使用深度学习模型(如神经网络)进行流失预测
2. 实现客户生命周期价值(CLV)预测
3. 构建实时流失预警系统(Streaming ML)
4. 对比多种客户细分方法(K-means聚类、层次聚类等)

## 获取帮助

- **项目Issues**: [GitHub Issues](https://github.com/shychee/py_ai_tutorial/issues)
- **学习社群**: [Discord/微信群链接]
- **故障排查**: 参见 `docs/cross-platform/troubleshooting.md`
- **邮件支持**: tutorial@example.com

---

**祝学习顺利!通过RFM分析与流失预测,掌握客户价值管理的核心技能。**
