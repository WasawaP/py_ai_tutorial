# Pandas项目实战 (Pandas Practice)

**模块ID**: M02
**所属阶段**: Stage 3 - 机器学习与数据挖掘
**预计学习时间**: 1-1.5小时
**难度**: ⭐⭐ 初级-中级

---

## 📖 模块简介

本模块是M01科学计算库的实战延伸，将带你通过真实数据分析项目深入掌握Pandas的核心技能：
- **描述性分析**: 理解数据的集中趋势、离散程度、分布特征
- **探索性数据分析 (EDA)**: 发现数据中的模式、异常值、关系
- **数据预处理**: 数据合并、清洗、标准化、特征工程

这些技能是所有数据分析和机器学习项目的必备基础。

---

## 🎯 学习目标

完成本模块后，你将能够：

1. ✅ 进行全面的描述性统计分析
2. ✅ 使用可视化进行探索性数据分析
3. ✅ 识别和处理数据质量问题（缺失值、异常值、重复值）
4. ✅ 进行数据合并与拼接（merge、concat、join）
5. ✅ 应用数据标准化与归一化
6. ✅ 使用正则表达式进行文本数据清洗
7. ✅ 进行特征工程（编码、分箱、派生特征）
8. ✅ 独立完成端到端的数据分析项目

---

## 📚 知识点清单

### 1. 描述性分析

<details>
<summary><strong>核心概念</strong></summary>

**集中趋势**:
- 均值 (Mean): 数据的平均水平
- 中位数 (Median): 数据的中间值，对异常值不敏感
- 众数 (Mode): 出现频率最高的值
- 几何平均数: 适用于增长率数据

**离散程度**:
- 方差 (Variance): 数据的分散程度
- 标准差 (Standard Deviation): 方差的平方根，与数据同单位
- 极差 (Range): 最大值 - 最小值
- 四分位距 (IQR): Q3 - Q1，衡量中间50%数据的分散程度
- 变异系数 (CV): 标准差/均值，用于比较不同量级数据的离散度

**分布形态**:
- 偏度 (Skewness): 分布的对称性
  - 正偏: 右尾长（mean > median）
  - 负偏: 左尾长（mean < median）
- 峰度 (Kurtosis): 分布的尖锐程度
  - 高峰: 数据集中在均值附近
  - 低峰: 数据分散

**Pandas实现**:
```python
# 基础统计
df.describe()  # 一次性获取所有统计量

# 单独计算
df['column'].mean()    # 均值
df['column'].median()  # 中位数
df['column'].mode()    # 众数
df['column'].std()     # 标准差
df['column'].var()     # 方差
df['column'].quantile([0.25, 0.5, 0.75])  # 分位数

# 高级统计
df['column'].skew()    # 偏度
df['column'].kurt()    # 峰度
```

**应用场景**:
- 数据质量检查：发现异常值
- 业务理解：了解指标的典型值和波动范围
- 特征选择：识别方差过小的无效特征

</details>

---

### 2. 探索性数据分析 (EDA)

<details>
<summary><strong>核心概念</strong></summary>

**EDA的目标**:
1. 理解数据结构和特征
2. 发现数据中的模式和关系
3. 识别异常值和数据质量问题
4. 形成建模假设

**EDA的步骤**:

**Step 1: 数据概览**
```python
# 查看数据形状和类型
print(df.shape)
print(df.dtypes)
print(df.info())

# 查看缺失值
print(df.isnull().sum())

# 查看前几行
print(df.head())
```

**Step 2: 单变量分析**
```python
# 数值型变量
df['numeric_col'].describe()
df['numeric_col'].hist(bins=50)  # 分布直方图
df['numeric_col'].plot(kind='box')  # 箱线图识别异常值

# 类别型变量
df['category_col'].value_counts()
df['category_col'].value_counts().plot(kind='bar')
```

**Step 3: 双变量分析**
```python
# 数值 vs 数值：散点图
df.plot(x='var1', y='var2', kind='scatter')

# 数值 vs 类别：分组统计
df.groupby('category')['numeric'].mean().plot(kind='bar')

# 相关性分析
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True)
```

**Step 4: 多变量分析**
```python
# 成对关系图
sns.pairplot(df, hue='target')

# 分组箱线图
sns.boxplot(data=df, x='category', y='numeric', hue='target')
```

**异常值识别方法**:
1. **IQR方法**: 超出 [Q1-1.5*IQR, Q3+1.5*IQR] 范围
2. **Z-score方法**: |z| > 3 (假设正态分布)
3. **可视化**: 箱线图、散点图

```python
# IQR方法
Q1 = df['column'].quantile(0.25)
Q3 = df['column'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df['column'] < lower_bound) | (df['column'] > upper_bound)]

# Z-score方法
from scipy import stats
z_scores = np.abs(stats.zscore(df['column']))
outliers = df[z_scores > 3]
```

**为什么重要？**
- EDA是建模前的必经步骤，能避免"垃圾进，垃圾出"
- 好的EDA能节省大量后续调试时间
- 很多数据科学竞赛的冠军都强调EDA的重要性

</details>

---

### 3. 数据合并与拼接

<details>
<summary><strong>核心概念</strong></summary>

**merge() - SQL风格的连接**:
```python
# 内连接 (INNER JOIN)
pd.merge(df1, df2, on='key', how='inner')

# 左连接 (LEFT JOIN)
pd.merge(df1, df2, on='key', how='left')

# 右连接 (RIGHT JOIN)
pd.merge(df1, df2, on='key', how='right')

# 全外连接 (FULL OUTER JOIN)
pd.merge(df1, df2, on='key', how='outer')

# 多键连接
pd.merge(df1, df2, on=['key1', 'key2'])

# 不同列名连接
pd.merge(df1, df2, left_on='id', right_on='user_id')
```

**concat() - 按轴拼接**:
```python
# 垂直拼接（增加行）
pd.concat([df1, df2], axis=0, ignore_index=True)

# 水平拼接（增加列）
pd.concat([df1, df2], axis=1)

# 保留来源标记
pd.concat([df1, df2], keys=['source1', 'source2'])
```

**join() - 基于索引连接**:
```python
df1.join(df2, how='left', lsuffix='_left', rsuffix='_right')
```

**选择哪种方法？**
- `merge()`: 基于列值连接（最常用）
- `concat()`: 简单拼接多个DataFrame
- `join()`: 基于索引连接（较少使用）

**常见问题**:
- 重复键导致笛卡尔积爆炸
- 连接后数据量异常（检查连接键的唯一性）
- 列名冲突（使用suffixes参数）

</details>

---

### 4. 数据清洗与标准化

<details>
<summary><strong>核心概念</strong></summary>

**缺失值处理策略**:
1. **删除**: 数据量大、缺失比例小时可行
2. **填充**:
   - 数值型: 均值、中位数、众数、插值
   - 类别型: 众数、"Unknown"
   - 时间序列: 前向填充 (ffill)、后向填充 (bfill)
3. **预测**: 使用机器学习模型预测缺失值
4. **标记**: 创建"是否缺失"的二值特征

```python
# 删除缺失值
df.dropna()  # 删除任意列有缺失的行
df.dropna(subset=['col1', 'col2'])  # 删除指定列有缺失的行
df.dropna(thresh=5)  # 至少有5个非缺失值才保留

# 填充缺失值
df['col'].fillna(df['col'].mean())  # 均值填充
df['col'].fillna(df['col'].median())  # 中位数填充
df['col'].fillna(method='ffill')  # 前向填充
df['col'].fillna(method='bfill')  # 后向填充
df['col'].interpolate()  # 插值填充
```

**数据标准化与归一化**:

**Min-Max归一化** (缩放到[0, 1]):
```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['normalized'] = scaler.fit_transform(df[['column']])
# 公式: (x - min) / (max - min)
```

**Z-score标准化** (均值0，标准差1):
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df['standardized'] = scaler.fit_transform(df[['column']])
# 公式: (x - mean) / std
```

**何时使用？**
- Min-Max: 数据有明确边界，不受异常值影响时
- Z-score: 数据接近正态分布，需要保留分布形态时
- 决策树/随机森林: 不需要标准化
- 线性模型/神经网络/KNN: 需要标准化

**正则表达式清洗文本**:
```python
import re

# 提取数字
df['numeric'] = df['text_col'].str.extract(r'(\d+)', expand=False)

# 替换特殊字符
df['clean'] = df['text_col'].str.replace(r'[^\w\s]', '', regex=True)

# 验证格式（如邮箱）
df['is_valid_email'] = df['email'].str.match(r'^[\w\.-]+@[\w\.-]+\.\w+$')

# 分割字符串
df[['first', 'last']] = df['name'].str.split(' ', expand=True)
```

</details>

---

### 5. 特征工程

<details>
<summary><strong>核心概念</strong></summary>

**类别特征编码**:

**1. Label Encoding** (序号编码):
```python
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['encoded'] = le.fit_transform(df['category'])
# 适用于有序类别：低/中/高 → 0/1/2
```

**2. One-Hot Encoding** (独热编码):
```python
pd.get_dummies(df, columns=['category'], drop_first=True)
# 适用于无序类别：红/绿/蓝 → [1,0,0], [0,1,0], [0,0,1]
```

**3. Frequency Encoding** (频率编码):
```python
freq_map = df['category'].value_counts().to_dict()
df['frequency'] = df['category'].map(freq_map)
# 高基数类别特征（如城市名）
```

**数值特征分箱**:
```python
# 等宽分箱
df['age_bin'] = pd.cut(df['age'], bins=5, labels=['A', 'B', 'C', 'D', 'E'])

# 等频分箱
df['age_qcut'] = pd.qcut(df['age'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

# 自定义分箱
bins = [0, 18, 35, 60, 100]
df['age_group'] = pd.cut(df['age'], bins=bins, labels=['少年', '青年', '中年', '老年'])
```

**派生特征**:
```python
# 数学运算
df['BMI'] = df['weight'] / (df['height'] / 100) ** 2

# 时间特征
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['dayofweek'] = df['date'].dt.dayofweek
df['is_weekend'] = df['dayofweek'].isin([5, 6]).astype(int)

# 聚合特征
df['total_purchase'] = df.groupby('user_id')['amount'].transform('sum')
df['avg_purchase'] = df.groupby('user_id')['amount'].transform('mean')

# 交互特征
df['price_per_sqm'] = df['price'] / df['area']
```

**为什么重要？**
- "数据和特征决定了机器学习的上限，而模型和算法只是逼近这个上限而已" - Andrew Ng
- 好的特征工程能让简单模型胜过复杂模型

</details>

---

## 📓 配套Notebook

按顺序学习以下Notebook：

| Notebook | 主题 | 时长 | 难度 |
|----------|------|------|------|
| [04-descriptive-analysis.ipynb](../../../notebooks/stage3/04-descriptive-analysis.ipynb) | 描述性统计、探索性分析、异常值检测 | 25分钟 | ⭐⭐ |
| [05-data-preprocessing.ipynb](../../../notebooks/stage3/05-data-preprocessing.ipynb) | 数据合并、清洗、标准化、特征工程 | 30分钟 | ⭐⭐ |

**学习建议**:
1. 先完成Module M01的3个基础Notebook
2. 按顺序运行每个cell，理解每个操作的含义
3. 尝试修改参数，观察结果变化
4. 完成Notebook末尾的综合练习
5. 可选：将学到的技能应用到自己的数据集

---

## 🛠️ 实战练习

### 练习1: 电商用户行为分析

**数据描述**: 包含10万条用户行为记录（浏览、收藏、加购、购买）

**任务**:
1. 进行完整的EDA：数据概览、缺失值、分布、相关性
2. 计算用户行为漏斗转化率（浏览→收藏→加购→购买）
3. 分析不同时间段的用户活跃度
4. 识别高价值用户（RFM分析）

<details>
<summary><strong>提示</strong></summary>

```python
import pandas as pd
import numpy as np

# 生成模拟数据
np.random.seed(42)
n = 100000

data = {
    'user_id': np.random.randint(1000, 5000, n),
    'behavior': np.random.choice(['view', 'fav', 'cart', 'buy'], n, p=[0.6, 0.2, 0.15, 0.05]),
    'category': np.random.choice(['电子', '服装', '食品', '图书'], n),
    'timestamp': pd.date_range('2024-01-01', periods=n, freq='30s'),
    'price': np.random.exponential(100, n)
}
df = pd.DataFrame(data)

# 1. EDA
print(df.info())
print(df.describe())
print(df['behavior'].value_counts())

# 2. 漏斗分析
funnel = df['behavior'].value_counts()
print("\n转化漏斗:")
print(f"浏览: {funnel.get('view', 0)}")
print(f"收藏: {funnel.get('fav', 0)} ({funnel.get('fav', 0)/funnel.get('view', 1)*100:.2f}%)")
print(f"加购: {funnel.get('cart', 0)} ({funnel.get('cart', 0)/funnel.get('view', 1)*100:.2f}%)")
print(f"购买: {funnel.get('buy', 0)} ({funnel.get('buy', 0)/funnel.get('view', 1)*100:.2f}%)")

# 3. 时间分析
df['hour'] = df['timestamp'].dt.hour
hourly = df.groupby('hour').size()
hourly.plot(kind='line', title='每小时活跃度')

# 4. RFM分析（仅购买行为）
buy_df = df[df['behavior'] == 'buy'].copy()
now = df['timestamp'].max()

rfm = buy_df.groupby('user_id').agg({
    'timestamp': lambda x: (now - x.max()).days,  # Recency
    'user_id': 'count',  # Frequency
    'price': 'sum'  # Monetary
})
rfm.columns = ['Recency', 'Frequency', 'Monetary']

# 分段
rfm['R_Score'] = pd.qcut(rfm['Recency'], 4, labels=[4, 3, 2, 1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 4, labels=[1, 2, 3, 4])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 4, labels=[1, 2, 3, 4])
rfm['RFM_Score'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)

print("\nRFM Top 10 用户:")
print(rfm.sort_values('Monetary', ascending=False).head(10))
```

</details>

---

### 练习2: 房价数据清洗与特征工程

**数据描述**: 房价数据集，包含位置、面积、房龄、配置等特征，存在数据质量问题

**任务**:
1. 处理缺失值（至少使用3种不同策略）
2. 识别和处理异常值（使用IQR和Z-score两种方法）
3. 数据标准化（比较Min-Max和Z-score的效果）
4. 特征工程：
   - 类别特征编码（朝向、装修等）
   - 时间特征派生（建造年份→房龄、房龄分段）
   - 交互特征（单价、总价/面积比）
5. 创建最终的建模数据集

<details>
<summary><strong>示例数据</strong></summary>

```python
# 创建模拟房价数据（含数据质量问题）
np.random.seed(42)
n = 500

data = {
    'price': np.random.normal(500, 150, n),  # 万元
    'area': np.random.normal(100, 30, n),  # 平米
    'rooms': np.random.choice([1, 2, 3, 4], n, p=[0.1, 0.3, 0.4, 0.2]),
    'build_year': np.random.randint(1990, 2024, n),
    'floor': np.random.randint(1, 33, n),
    'direction': np.random.choice(['南', '北', '东', '西', '南北'], n),
    'decoration': np.random.choice(['毛坯', '简装', '精装', '豪装'], n),
    'district': np.random.choice(['朝阳', '海淀', '西城', '东城', '丰台'], n)
}
df = pd.DataFrame(data)

# 引入缺失值
df.loc[np.random.choice(df.index, 50), 'price'] = np.nan
df.loc[np.random.choice(df.index, 30), 'area'] = np.nan
df.loc[np.random.choice(df.index, 20), 'build_year'] = np.nan

# 引入异常值
df.loc[np.random.choice(df.index, 5), 'price'] = np.random.uniform(2000, 5000, 5)  # 超高房价
df.loc[np.random.choice(df.index, 3), 'area'] = np.random.uniform(500, 1000, 3)  # 超大面积

print("原始数据形状:", df.shape)
print("\n缺失值统计:")
print(df.isnull().sum())
print("\n数据预览:")
print(df.head())
```

</details>

---

## 🎓 进阶拓展

完成基础学习后，可选择深入以下主题：

1. **时间序列分析**
   - 移动平均、指数平滑
   - 季节性分解
   - ARIMA模型

2. **文本数据处理**
   - 分词、词频统计
   - TF-IDF向量化
   - 情感分析

3. **大数据处理**
   - Dask: Pandas的分布式版本
   - Polars: 更快的DataFrame库
   - Apache Spark: 大规模数据处理

4. **自动化特征工程**
   - Featuretools: 自动生成特征
   - TPOT/AutoGluon: 自动机器学习

---

## 📖 推荐资源

### 书籍
- 《Python数据分析实战》- Fabio Nelli
- 《Feature Engineering for Machine Learning》- Alice Zheng

### 课程
- Kaggle Learn: [Pandas](https://www.kaggle.com/learn/pandas)
- Kaggle Learn: [Data Cleaning](https://www.kaggle.com/learn/data-cleaning)
- Kaggle Learn: [Feature Engineering](https://www.kaggle.com/learn/feature-engineering)

### 实战项目
- Kaggle竞赛: [Titanic](https://www.kaggle.com/c/titanic) (入门级)
- Kaggle竞赛: [House Prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)

---

## ✅ 自测清单

完成本模块后，你应该能够：

- [ ] 计算并解释描述性统计量（均值、中位数、标准差、偏度、峰度）
- [ ] 进行完整的EDA流程（单变量、双变量、多变量分析）
- [ ] 识别和处理异常值（IQR、Z-score方法）
- [ ] 使用merge/concat合并多个数据源
- [ ] 处理缺失值（删除、填充、标记）
- [ ] 应用数据标准化和归一化
- [ ] 使用正则表达式清洗文本数据
- [ ] 进行类别特征编码（Label Encoding、One-Hot Encoding）
- [ ] 创建派生特征和交互特征
- [ ] 独立完成端到端的数据预处理流程

**通过标准**: 完成2个实战练习，能清晰解释每个数据处理步骤的目的

---

## 🚀 下一步

完成本模块后，你可以：

1. **继续学习模块M03**: [AI数学基础](../03-ml-basics/README.md) - 统计学、线性代数、概率论速览
2. **开始项目实战**: [项目P01 - 朝阳医院数据分析](../projects/p01-healthcare/README.md)
3. **深入特征工程**: 学习更高级的特征构建技巧

**重要**: Pandas数据处理能力是数据科学家的核心竞争力，多练习、多实践！

---

## 💬 讨论与反馈

遇到问题？有改进建议？

- 💬 加入学习社群讨论
- 🐛 提交[GitHub Issue](https://github.com/shychee/py_ai_tutorial/issues)
- 📧 发送邮件至 shychee96@gmail.com

**掌握数据清洗，你就掌握了数据科学的80%！** 💪
