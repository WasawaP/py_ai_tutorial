# Stage 3 数据集说明

本目录包含阶段3（机器学习与数据挖掘）的9个项目数据集。

---

## 📊 数据集概览

| 项目 | 数据集名称 | 文件名 | 大小 | 行数 | 用途 |
|------|-----------|--------|------|------|------|
| P01 | 朝阳医院销售数据 | `hospital_sales.csv` | 52MB | 500K | 数据清洗、分组聚合、时间序列分析 |
| P02 | 服装零售销售数据 | `clothing_retail.csv` | 105MB | 1000K | RFM模型、客户细分、关联规则 |
| P03 | 银行营销数据 | `bank_marketing.csv` | 210MB | 45K | 分类模型、特征工程、不平衡数据处理 |
| P04 | 通讯公司客户数据 | `telecom_customer_data.csv` | 8.2MB | 100K | RFM模型、流失预测、客户细分 |
| P05 | 零售超市数据 | `retail_supermarket.csv` | 320MB | 2000K | SWOT分析、关联规则、销售预测 |
| P06 | 滴滴运营数据 | `didi_operations.csv` | 420MB | 3000K | 异常检测、时间序列、地理可视化 |
| P07 | 淘宝用户行为数据 | `taobao_user_behavior.csv` | 520MB | 100000K | 大规模数据处理、推荐系统、用户行为建模 |
| P08 | 航空公司客户数据 | `airline_customer.csv` | 205MB | 800K | K-means聚类、LRFMC模型、客户价值分析 |
| P09 | 信贷数据 | `credit_loan.csv` | 110MB | 307K | 风控建模、不平衡数据、模型解释 |

**总大小**: ~2.0GB  
**总行数**: ~108M 行

---

## 🚀 快速开始

### 方法1: 自动下载（推荐）

使用下载脚本自动获取所有数据集：

```bash
# 标准下载（国外服务器）
python scripts/data/download-stage3.py

# 使用国内镜像加速
python scripts/data/download-stage3.py --mirror

# 仅下载特定数据集
python scripts/data/download-stage3.py --dataset DS-S3-P01-HOSPITAL

# 校验已下载的数据
python scripts/data/download-stage3.py --verify-only
```

### 方法2: 手动下载

如果自动下载失败,可以手动下载：

#### P01: 朝阳医院销售数据
- **来源**: 合成数据（基于真实场景）
- **下载链接**: 
  - GitHub Releases: `https://github.com/shychee/py_ai_tutorial/releases/download/v1.0.0/hospital_sales.csv`
  - 镜像: `https://mirror.example.com/datasets/stage3/hospital_sales.csv`
- **SHA256**: `待生成`
- **放置位置**: `data/stage3/hospital_sales.csv`

#### P02: 服装零售销售数据
- **来源**: 合成数据
- **下载链接**: 
  - GitHub Releases: `https://github.com/shychee/py_ai_tutorial/releases/download/v1.0.0/clothing_retail.csv`
  - 镜像: `https://mirror.example.com/datasets/stage3/clothing_retail.csv`
- **SHA256**: `待生成`
- **放置位置**: `data/stage3/clothing_retail.csv`

#### P03: 银行营销数据
- **来源**: UCI Machine Learning Repository
- **下载链接**: `https://archive.ics.uci.edu/ml/datasets/Bank+Marketing`
- **许可证**: CC BY 4.0
- **引用**: Moro et al., 2014. A Data-Driven Approach to Predict the Success of Bank Telemarketing.
- **SHA256**: `待生成`
- **放置位置**: `data/stage3/bank_marketing.csv`

#### P04-P09: 其他数据集
详细下载链接请参考 `configs/content/datasets.yaml` 配置文件。

### 方法3: 使用离线数据包

如果网络不稳定或需要快速部署,可以使用离线数据包：

```bash
# 下载离线包（约2GB）
wget https://github.com/shychee/py_ai_tutorial/releases/download/v1.0.0/stage3-data.tar.gz

# 解压到data目录
tar -xzf stage3-data.tar.gz -C data/
```

---

## 🔐 数据校验

为确保数据完整性,请在使用前进行校验：

```bash
# 使用下载脚本自动校验
python scripts/data/download-stage3.py --verify-only

# 或手动校验单个文件
sha256sum data/stage3/hospital_sales.csv
```

**校验清单** (checksums.txt):
```
PLACEHOLDER  data/stage3/hospital_sales.csv
PLACEHOLDER  data/stage3/clothing_retail.csv
PLACEHOLDER  data/stage3/bank_marketing.csv
PLACEHOLDER  data/stage3/telecom_customer.csv
PLACEHOLDER  data/stage3/retail_supermarket.csv
PLACEHOLDER  data/stage3/didi_operations.csv
PLACEHOLDER  data/stage3/taobao_user_behavior.csv
PLACEHOLDER  data/stage3/airline_customer.csv
PLACEHOLDER  data/stage3/credit_loan.csv
```

---

## 📝 数据集详细说明

### P01: 朝阳医院销售数据

**项目路径**: `docs/stage3/projects/p01-healthcare/`

**数据描述**:
- 医疗行业药品销售记录
- 包含：订单编号、日期、药品名称、类别、数量、单价、总金额、客户类型等18个字段
- 时间范围: 2022-01-01 至 2024-12-31
- 数据已脱敏,不包含真实患者信息

**关键字段**:
- `order_id`: 订单编号
- `order_date`: 订单日期
- `product_name`: 药品名称
- `category`: 药品分类（15类）
- `quantity`: 销售数量
- `unit_price`: 单价（元）
- `total_amount`: 总金额（元）
- `customer_type`: 客户类型（个人/机构）

**数据质量**:
- 缺失值: 0.5%
- 重复值: 0.2%
- 异常值: 1%

**学习目标**:
- 数据清洗与预处理
- 时间序列分析
- 销售趋势可视化
- 分组聚合统计

---

### P02: 服装零售销售数据

**项目路径**: `docs/stage3/projects/p02-ecommerce/`

**数据描述**:
- 服装零售行业订单数据
- 包含：客户ID、订单日期、商品ID、商品类别、价格、数量等22个字段
- 50,000名客户、2,000件商品、100万条订单记录
- 时间范围: 2023-01-01 至 2024-12-31

**学习目标**:
- RFM模型构建
- 客户细分与画像
- 关联规则挖掘
- 商品推荐系统基础

---

### P03: 银行营销数据

**项目路径**: `docs/stage3/projects/p03-finance/`

**数据描述**:
- 银行电话营销活动数据（UCI公开数据集）
- 包含：年龄、职业、婚姻状况、教育、账户余额、响应结果等17个字段
- 45,211条记录,类别不平衡(正负比例 1:8)

**学习目标**:
- 二分类模型训练
- 特征工程与选择
- 不平衡数据处理(SMOTE)
- 模型评估与调优

---

### P04: 通讯公司客户数据

**项目路径**: `docs/stage3/projects/p04-telecom/`

**数据描述**:
- 通讯运营商客户管理数据(模拟生成)
- 100,000条客户记录,流失率15.08%
- 包含13个字段：客户ID、注册日期、最后交易日期、交易次数、消费金额、服务类型、合约类型、投诉次数、客服呼叫、流失标签、年龄段、地区等
- 文件大小: 8.2 MB
- 时间跨度: 2023年1月 - 2024年12月

**关键字段**:
- `customer_id`: 客户唯一标识 (C000001-C100000)
- `registration_date`: 注册日期
- `last_transaction_date`: 最后交易日期
- `transaction_count`: 24个月内交易次数 (1-100)
- `total_amount`: 总消费金额(元)
- `avg_amount_per_transaction`: 平均单次消费(元)
- `service_type`: 服务类型 (移动套餐/宽带/固话/移动+宽带/全业务)
- `contract_type`: 合约类型 (月付/年付/按量付费)
- `complaint_count`: 投诉次数 (0-10)
- `service_call_count`: 客服呼叫次数 (0-20)
- `churn`: 是否流失 (0=未流失, 1=已流失)
- `age_group`: 年龄段 (18-25/26-35/36-45/46-55/56+)
- `region`: 所在地区 (华东/华北/华南/华中/西南/西北/东北)

**数据生成方式**:
```bash
# 使用纯Python脚本生成(无需pandas)
python scripts/data/generate-stage3-telecom-data-simple.py

# 或使用pandas版本
python scripts/data/generate-stage3-telecom-data.py
```

**数据特征**:
- 流失率: 15.08% (符合行业平均水平)
- 交易次数: Gamma分布 (shape=2, scale=15)
- 消费金额: Gamma分布 (shape=4, scale=25)
- 投诉/呼叫: 泊松分布 (流失客户频率更高)
- 流失客户特征: 最后交易距今90-365天,投诉更多,呼叫更频繁

**学习目标**:
- RFM客户价值分析 (Recency/Frequency/Monetary)
- 客户细分 (8个细分群体: 冠军/忠诚/流失风险/休眠等)
- 客户流失预测建模 (随机森林分类器)
- 类别不平衡处理 (class_weight='balanced')
- 特征重要性分析
- 业务策略制定

---

### P05: 零售超市数据

**项目路径**: `docs/stage3/projects/p05-retail/`

**数据描述**:
- 零售超市经营数据
- 2,000,000条销售记录,5,000种商品,50家门店
- 包含：商品信息、销售数据、库存记录、促销活动等15个字段

**学习目标**:
- SWOT分析
- 关联规则挖掘(Apriori算法)
- 销售预测
- 库存优化建议

---

### P06: 滴滴运营数据

**项目路径**: `docs/stage3/projects/p06-internet/`

**数据描述**:
- 出行平台运营数据（合成）
- 3,000,000条订单记录,10,000名司机
- 包含：订单信息、轨迹数据、异常标签等18个字段

**学习目标**:
- 异常检测算法
- 时间序列分析
- 地理数据可视化
- 运营指标计算

---

### P07: 淘宝用户行为数据

**项目路径**: `docs/stage3/projects/p07-ecommerce-annual/`

**数据描述**:
- 淘宝百万级用户行为数据（天池公开数据集）
- 100,000,000条行为记录(浏览/收藏/加购/购买)
- 包含：用户ID、商品ID、类别ID、行为类型、时间戳等6个字段

⚠️ **注意**:
- 数据量大（520MB,1亿行）,建议使用分块读取或采样
- 支持Dask/Pandas chunking进行并行计算
- 提供1M行采样数据用于快速实验

**学习目标**:
- 大规模数据处理技巧
- 用户行为分析
- 协同过滤推荐
- 转化率分析

---

### P08: 航空公司客户数据

**项目路径**: `docs/stage3/projects/p08-airline/`

**数据描述**:
- 航空公司会员数据
- 800,000名会员,4个会员等级
- 包含：飞行记录、里程累积、消费金额等14个字段

**学习目标**:
- K-means聚类
- LRFMC模型（航空业客户价值模型）
- 客户生命周期价值分析
- 可视化呈现

---

### P09: 信贷数据

**项目路径**: `docs/stage3/projects/p09-credit/`

**数据描述**:
- 信用贷款申请数据（Kaggle竞赛数据）
- 307,511条申请记录,违约率8.1%（不平衡）
- 122个特征（需要特征工程）

**学习目标**:
- 金融风控建模
- 高维特征处理
- 模型解释性分析(SHAP)
- 业务指标优化

---

## ⚠️ 数据使用注意事项

### 许可证与引用

- **合成数据** (P01, P02, P04, P05, P06, P08): MIT License,仅供教学使用
- **公开数据** (P03, P07, P09): 遵循原始数据集许可证,使用时请注明出处

引用示例:
```
Moro, S., Cortez, P., & Rita, P. (2014). A data-driven approach to predict the success 
of bank telemarketing. Decision Support Systems, 62, 22-31.
```

### 隐私与合规

- 所有数据已脱敏处理
- 不包含真实个人身份信息
- 合成数据基于真实场景但无法追溯到真实个体

### 存储建议

- 推荐使用SSD存储,加快读取速度
- 大数据集(P07)建议使用Parquet格式或数据库存储
- 定期备份数据,避免意外丢失

---

## 🐛 常见问题

### Q1: 下载速度慢怎么办？
A: 使用`--mirror`参数切换到国内镜像,或直接下载离线数据包。

### Q2: 校验和不匹配怎么办？
A: 删除文件重新下载,或检查网络是否稳定。如多次失败,请提Issue。

### Q3: 某个数据集下载失败怎么办？
A: 使用`--dataset`参数单独下载该数据集,或手动从提供的链接下载。

### Q4: P07数据集太大,内存不足怎么办？
A: 使用Pandas的`chunksize`参数分块读取:
```python
for chunk in pd.read_csv('data/stage3/taobao_user_behavior.csv', chunksize=100000):
    # 处理每个chunk
    process(chunk)
```

### Q5: 数据集更新了怎么办？
A: 重新运行下载脚本,会自动检测并下载新版本。

---

## 📚 相关文档

- [数据集配置文件](../../configs/content/datasets.yaml) - 完整的数据集元数据
- [下载脚本源码](../../scripts/data/download-stage3.py) - 自动下载工具
- [阶段3学习路径](../../docs/learning-path.md#阶段3-机器学习与数据挖掘) - 如何使用这些数据集

---

## 🔗 外部资源

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/) - 公开数据集库
- [Kaggle Datasets](https://www.kaggle.com/datasets) - 数据科学竞赛平台
- [天池数据集](https://tianchi.aliyun.com/dataset) - 阿里云数据集平台

---

**最后更新**: 2025-11-12
**维护者**: py_ai_tutorial团队

**反馈**: 如有数据问题,请在GitHub提Issue: `https://github.com/shychee/py_ai_tutorial/issues`
