# 机器学习进阶 (Advanced Machine Learning)

**模块ID**: M04
**所属阶段**: Stage 3 - 机器学习与数据挖掘
**预计学习时间**: 1.5-2小时
**难度**: ⭐⭐⭐ 中级

---

## 📖 模块简介

本模块将带你掌握经典机器学习算法：
- **监督学习**: 回归（线性回归、岭回归）、分类（逻辑回归、决策树、随机森林、XGBoost）
- **无监督学习**: 聚类（K-means、层次聚类）、降维（PCA）
- **集成学习**: Bagging、Boosting、Stacking
- **模型评估**: 交叉验证、评估指标、混淆矩阵、ROC曲线

这是Stage 3的核心模块，学完后你将具备完成实际机器学习项目的能力！

---

## 🎯 学习目标

完成本模块后，你将能够：

1. ✅ 理解并应用线性回归和逻辑回归
2. ✅ 使用决策树、随机森林、XGBoost解决分类问题
3. ✅ 应用K-means进行聚类分析
4. ✅ 理解集成学习的原理（Bagging、Boosting）
5. ✅ 进行模型评估（准确率、精确率、召回率、F1、AUC）
6. ✅ 使用交叉验证和网格搜索调参
7. ✅ 处理过拟合和欠拟合
8. ✅ 独立完成端到端的机器学习项目

---

## 📚 知识点清单

### 1. 监督学习 - 回归

<details>
<summary><strong>核心概念</strong></summary>

**线性回归 (Linear Regression)**:
- 目标: 找到最佳拟合直线 $y = wx + b$
- 损失函数: MSE (均方误差) = $\frac{1}{n}\sum(y_i - \hat{y}_i)^2$
- 求解方法: 正规方程、梯度下降
- 应用: 房价预测、销售预测

**岭回归 (Ridge Regression)**:
- 在损失函数中加入L2正则化: $MSE + \alpha \sum w^2$
- 作用: 防止过拟合，权重不会过大
- 应用: 高维数据、特征多重共线性

**多项式回归**:
- 将线性模型扩展到非线性: $y = w_0 + w_1x + w_2x^2 + ...$
- 注意: 容易过拟合，需要正则化

```python
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures

# 线性回归
model = LinearRegression()
model.fit(X_train, y_train)

# 岭回归
model = Ridge(alpha=1.0)
model.fit(X_train, y_train)

# 多项式回归
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model = LinearRegression().fit(X_poly, y)
```

</details>

---

### 2. 监督学习 - 分类

<details>
<summary><strong>核心概念</strong></summary>

**逻辑回归 (Logistic Regression)**:
- 用于二分类问题
- 模型: $P(y=1|x) = \frac{1}{1+e^{-(wx+b)}}$ (Sigmoid函数)
- 损失函数: 交叉熵损失
- 应用: 垃圾邮件分类、疾病诊断

**决策树 (Decision Tree)**:
- 通过一系列if-else规则进行分类
- 分裂标准: 信息增益(ID3)、信息增益比(C4.5)、基尼指数(CART)
- 优点: 可解释性强、可处理非线性
- 缺点: 容易过拟合

**随机森林 (Random Forest)**:
- 集成多个决策树（Bagging）
- 每棵树训练时随机选择特征子集
- 预测时投票决定（分类）或平均（回归）
- 优点: 准确率高、抗过拟合、可提供特征重要性

**XGBoost (Extreme Gradient Boosting)**:
- 基于梯度提升的集成算法
- 核心思想: 每棵新树纠正前面树的错误
- 特点: 速度快、效果好、支持并行
- 应用: Kaggle竞赛常胜将军

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

# 逻辑回归
model = LogisticRegression()
model.fit(X_train, y_train)

# 决策树
model = DecisionTreeClassifier(max_depth=5)
model.fit(X_train, y_train)

# 随机森林
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# XGBoost
model = XGBClassifier(n_estimators=100, learning_rate=0.1)
model.fit(X_train, y_train)
```

</details>

---

### 3. 无监督学习 - 聚类

<details>
<summary><strong>核心概念</strong></summary>

**K-means聚类**:
- 将数据分为K个簇
- 算法:
  1. 随机初始化K个中心点
  2. 分配每个点到最近的中心
  3. 更新中心为簇内点的均值
  4. 重复2-3直到收敛
- 超参数: K（簇数量）
- 选择K: 肘部法则、轮廓系数

**层次聚类**:
- 自底向上（凝聚）或自顶向下（分裂）
- 生成树状图（Dendrogram）
- 不需要预先指定K

```python
from sklearn.cluster import KMeans, AgglomerativeClustering

# K-means
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X)

# 层次聚类
hierarchical = AgglomerativeClustering(n_clusters=3)
clusters = hierarchical.fit_predict(X)
```

**应用场景**:
- 客户细分（RFM分析）
- 图像分割
- 异常检测
- 推荐系统

</details>

---

### 4. 模型评估

<details>
<summary><strong>核心概念</strong></summary>

**回归评估指标**:
- **MSE (均方误差)**: 平均误差的平方
- **RMSE (均方根误差)**: MSE的平方根，与y同单位
- **MAE (平均绝对误差)**: 平均绝对误差
- **R² (决定系数)**: 1 - (残差平方和/总平方和)，范围[0, 1]

**分类评估指标**:
- **准确率 (Accuracy)**: 预测正确的比例
- **精确率 (Precision)**: 预测为正的样本中真正为正的比例
- **召回率 (Recall)**: 真正为正的样本中被预测为正的比例
- **F1分数**: 精确率和召回率的调和平均
- **混淆矩阵**: 真正例、假正例、真负例、假负例
- **ROC曲线和AUC**: 不同阈值下的TPR vs FPR

```python
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score

# 回归指标
mse = mean_squared_error(y_true, y_pred)
r2 = r2_score(y_true, y_pred)

# 分类指标
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

# 混淆矩阵
cm = confusion_matrix(y_true, y_pred)

# AUC
auc = roc_auc_score(y_true, y_pred_proba)
```

**交叉验证**:
- K折交叉验证: 将数据分为K份，轮流作为验证集
- 作用: 更可靠的模型评估，充分利用数据

</details>

---

## 📓 配套Notebook

按顺序学习以下Notebook：

| Notebook | 主题 | 时长 | 难度 |
|----------|------|------|------|
| [08-ml-algorithms.ipynb](../../../notebooks/stage3/08-ml-algorithms.ipynb) | 回归、分类、聚类、集成学习、模型评估 | 40分钟 | ⭐⭐⭐ |

**学习建议**:
1. 先理解算法原理（看文档和可视化）
2. 运行代码，观察不同算法的效果
3. 尝试调整超参数，观察性能变化
4. 完成综合练习（端到端项目）

---

## ✅ 自测清单

完成本模块后，你应该能够：

- [ ] 使用线性回归进行房价预测
- [ ] 理解正则化（L1/L2）的作用
- [ ] 使用逻辑回归进行二分类
- [ ] 理解决策树的分裂规则
- [ ] 使用随机森林和XGBoost解决分类问题
- [ ] 应用K-means进行客户细分
- [ ] 计算并解释各种评估指标
- [ ] 绘制混淆矩阵和ROC曲线
- [ ] 使用交叉验证评估模型
- [ ] 独立完成机器学习项目全流程

**通过标准**: 完成综合练习，理解算法原理和应用场景

---

## 🚀 下一步

完成本模块后，你可以：

1. **开始Stage 3项目实战**: [项目P01-P09](../projects/) - 9个真实数据分析项目
2. **继续Stage 4**: [深度学习基础](../../stage4/) - CNN、RNN、Transformer
3. **参加Kaggle竞赛**: 应用所学知识

**恭喜！你已完成Stage 3的所有模块教程！** 🎉

---

## 💬 讨论与反馈

遇到问题？有改进建议？

- 💬 加入学习社群讨论
- 🐛 提交[GitHub Issue](https://github.com/shychee/py_ai_tutorial/issues)
- 📧 发送邮件至 tutorial@example.com

**机器学习是实践的艺术 - 多做项目，多参加竞赛！** 💪
