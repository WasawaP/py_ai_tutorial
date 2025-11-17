# 科学计算库 (Scientific Computing Libraries)

**模块ID**: M01
**所属阶段**: Stage 3 - 机器学习与数据挖掘
**预计学习时间**: 1-1.5小时
**难度**: ⭐ 入门级

---

## 📖 模块简介

本模块是AI学习的基石，将带你掌握Python数据分析的核心工具链：
- **NumPy**: 高效数组运算与数值计算
- **Pandas**: 数据清洗、处理与分析
- **Matplotlib/Seaborn**: 数据可视化

这些工具是所有机器学习项目的前置依赖，贯穿整个教程。

---

## 🎯 学习目标

完成本模块后，你将能够：

1. ✅ 使用NumPy创建和操作多维数组
2. ✅ 使用NumPy进行统计计算与数学运算
3. ✅ 使用Pandas创建和操作DataFrame
4. ✅ 使用Pandas进行数据清洗、筛选、分组、聚合
5. ✅ 使用Matplotlib绘制基础图表（折线图、柱状图、散点图）
6. ✅ 使用Seaborn绘制高级可视化（热力图、分布图）
7. ✅ 理解向量化运算的性能优势

---

## 📚 知识点清单

### 1. NumPy基础

<details>
<summary><strong>核心概念</strong></summary>

- **Ndarray数组**: 多维数组对象，高效的数值运算容器
- **数组创建**: `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`
- **数组属性**: `shape`, `dtype`, `ndim`, `size`
- **索引与切片**: 一维/多维数组的访问方式
- **数组运算**: 加减乘除、点积、矩阵乘法
- **统计函数**: `mean()`, `std()`, `sum()`, `max()`, `min()`, `percentile()`
- **广播机制** (Broadcasting): 不同形状数组的自动对齐
- **随机数生成**: `np.random.rand()`, `np.random.randn()`, `np.random.choice()`

**为什么重要？**
- NumPy是Python科学计算的基础，比原生Python列表快10-100倍
- 机器学习模型的输入输出都是NumPy数组
- 深度学习框架（PyTorch、TensorFlow）的API设计深受NumPy影响

</details>

---

### 2. Pandas数据处理

<details>
<summary><strong>核心概念</strong></summary>

- **Series**: 一维标签数组（类似带索引的列表）
- **DataFrame**: 二维表格数据（类似Excel表格或SQL表）
- **数据读取**: `pd.read_csv()`, `pd.read_excel()`, `pd.read_parquet()`
- **数据查看**: `head()`, `tail()`, `info()`, `describe()`
- **索引与选择**: `loc[]`, `iloc[]`, 布尔索引
- **数据清洗**:
  - 缺失值处理: `isnull()`, `dropna()`, `fillna()`
  - 重复值处理: `duplicated()`, `drop_duplicates()`
  - 类型转换: `astype()`, `pd.to_datetime()`
- **数据转换**:
  - 列操作: `apply()`, `map()`, `lambda`
  - 合并: `merge()`, `concat()`, `join()`
  - 分组: `groupby()` + `agg()`, `transform()`, `filter()`
  - 透视: `pivot_table()`, `crosstab()`
- **时间序列**: `DatetimeIndex`, `resample()`, `rolling()`

**为什么重要？**
- Pandas是数据分析师的主力工具
- 90%的数据预处理工作由Pandas完成
- 理解Pandas是理解数据清洗流程的关键

</details>

---

### 3. Matplotlib/Seaborn可视化

<details>
<summary><strong>核心概念</strong></summary>

**Matplotlib基础**:
- **绘图基础**: `plt.plot()`, `plt.bar()`, `plt.scatter()`, `plt.hist()`
- **图表元素**: 标题、标签、图例、网格
- **子图**: `plt.subplot()`, `plt.subplots()`
- **样式设置**: 颜色、线型、标记、字体

**Seaborn高级可视化**:
- **分布图**: `histplot()`, `kdeplot()`, `violinplot()`, `boxplot()`
- **关系图**: `scatterplot()`, `lineplot()`, `regplot()`
- **分类图**: `barplot()`, `countplot()`, `boxplot()`
- **矩阵图**: `heatmap()`, `clustermap()`
- **主题与调色板**: `sns.set_style()`, `sns.set_palette()`

**为什么重要？**
- "一图胜千言" - 可视化是理解数据的最快方式
- 数据探索性分析（EDA）的核心技能
- 向非技术人员展示分析结果的必备工具

</details>

---

## 📓 配套Notebook

按顺序学习以下Notebook：

| Notebook | 主题 | 时长 | 难度 |
|----------|------|------|------|
| [01-numpy-basics.ipynb](../../../notebooks/stage3/01-numpy-basics.ipynb) | NumPy数组操作、统计函数 | 20分钟 | ⭐ |
| [02-pandas-intro.ipynb](../../../notebooks/stage3/02-pandas-intro.ipynb) | Series、DataFrame、增删查改 | 25分钟 | ⭐⭐ |
| [03-visualization.ipynb](../../../notebooks/stage3/03-visualization.ipynb) | Matplotlib基础绘图、Seaborn样式 | 20分钟 | ⭐ |

**学习建议**:
1. 按顺序运行每个Notebook的cell
2. 修改参数，观察输出变化（动手是最好的学习方式）
3. 完成Notebook末尾的练习题
4. 若某个概念不理解，查看[术语表](../../glossary.md)

---

## 🛠️ 实战练习

### 练习1: NumPy数组操作

**任务**: 创建一个10x10的矩阵，随机填充0-100的整数，计算每行的平均值和每列的最大值。

<details>
<summary><strong>提示</strong></summary>

```python
import numpy as np

# 创建随机矩阵
matrix = np.random.randint(0, 101, size=(10, 10))

# 计算每行平均值
row_means = matrix.mean(axis=1)

# 计算每列最大值
col_maxs = matrix.max(axis=0)

print(f"每行平均值: {row_means}")
print(f"每列最大值: {col_maxs}")
```

</details>

---

### 练习2: Pandas数据清洗

**任务**: 给定一个包含缺失值和重复值的CSV文件，完成以下操作：
1. 删除重复行
2. 填充数值列的缺失值（用均值）
3. 删除字符串列的缺失值
4. 按某列分组并计算统计量

<details>
<summary><strong>示例数据</strong></summary>

```python
import pandas as pd

# 创建示例数据
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Alice', None, 'Eve'],
    'age': [25, 30, None, 25, 28, 32],
    'score': [85, 90, 88, 85, None, 95]
}
df = pd.DataFrame(data)

# 1. 删除重复行
df = df.drop_duplicates()

# 2. 填充数值列缺失值
df['age'] = df['age'].fillna(df['age'].mean())
df['score'] = df['score'].fillna(df['score'].mean())

# 3. 删除字符串列缺失值
df = df.dropna(subset=['name'])

# 4. 按age分组计算平均分
grouped = df.groupby('age')['score'].mean()
print(grouped)
```

</details>

---

### 练习3: 数据可视化

**任务**: 使用Matplotlib绘制一个2x2的子图，分别展示：
1. 折线图：时间序列数据
2. 柱状图：类别统计
3. 散点图：两变量关系
4. 直方图：数据分布

<details>
<summary><strong>示例代码</strong></summary>

```python
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 子图1: 折线图
axes[0, 0].plot([1, 2, 3, 4, 5], [10, 15, 13, 17, 20])
axes[0, 0].set_title('时间序列')
axes[0, 0].set_xlabel('时间')
axes[0, 0].set_ylabel('值')

# 子图2: 柱状图
categories = ['A', 'B', 'C', 'D']
values = [25, 40, 30, 50]
axes[0, 1].bar(categories, values)
axes[0, 1].set_title('类别统计')

# 子图3: 散点图
x = np.random.randn(100)
y = 2 * x + np.random.randn(100)
axes[1, 0].scatter(x, y, alpha=0.6)
axes[1, 0].set_title('相关性')

# 子图4: 直方图
data = np.random.randn(1000)
axes[1, 1].hist(data, bins=30, edgecolor='black')
axes[1, 1].set_title('数据分布')

plt.tight_layout()
plt.show()
```

</details>

---

## 🎓 进阶拓展

完成基础学习后，可选择深入以下主题：

1. **NumPy高级技巧**
   - 矩阵分解 (SVD, QR, Cholesky)
   - 线性代数应用 (`np.linalg`)
   - FFT快速傅里叶变换

2. **Pandas性能优化**
   - 使用Parquet格式加速IO
   - 向量化操作替代循环
   - 使用`category`类型节省内存

3. **可视化进阶**
   - Plotly交互式可视化
   - Altair声明式可视化
   - Matplotlib动画

---

## 📖 推荐资源

### 官方文档
- [NumPy官方文档](https://numpy.org/doc/stable/) (中文翻译版)
- [Pandas官方文档](https://pandas.pydata.org/docs/) (部分中文)
- [Matplotlib官方文档](https://matplotlib.org/stable/contents.html)

### 书籍
- 《利用Python进行数据分析》(第3版) - Wes McKinney (Pandas作者)
- 《Python数据科学手册》- Jake VanderPlas

### 视频教程
- Corey Schafer: [Pandas Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS)
- sentdex: [Data Analysis with Python and Pandas](https://www.youtube.com/playlist?list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-)

---

## ✅ 自测清单

完成本模块后，你应该能够：

- [ ] 创建NumPy数组并进行基础运算（加减乘除、统计）
- [ ] 理解NumPy广播机制并正确使用
- [ ] 使用Pandas读取CSV/Excel文件
- [ ] 使用Pandas进行数据清洗（处理缺失值、重复值、类型转换）
- [ ] 使用`groupby()`进行分组聚合分析
- [ ] 使用`merge()`合并多个DataFrame
- [ ] 使用Matplotlib绘制基础图表（折线图、柱状图、散点图）
- [ ] 使用Seaborn绘制统计图表（箱线图、热力图）
- [ ] 为图表添加标题、标签、图例等元素
- [ ] 理解向量化操作的性能优势（相比Python循环）

**通过标准**: 完成3个实战练习，能独立运行并理解输出

---

## 🚀 下一步

完成本模块后，你可以：

1. **继续学习模块M02**: [Pandas项目实战](../02-pandas-practice/README.md) - 完整的数据分析项目
2. **跳转到项目实战**: [项目P01 - 朝阳医院数据分析](../projects/p01-healthcare/README.md)
3. **深入数学基础**: [模块M03 - AI数学基础](../03-ml-basics/README.md)

**建议**: 不要急于跳过，扎实掌握NumPy和Pandas是后续学习的基础！

---

## 💬 讨论与反馈

遇到问题？有改进建议？

- 💬 加入学习社群讨论
- 🐛 提交[GitHub Issue](https://github.com/shychee/py_ai_tutorial/issues)
- 📧 发送邮件至 shychee96@gmail.com

**让我们一起打好AI学习的基础！** 💪
