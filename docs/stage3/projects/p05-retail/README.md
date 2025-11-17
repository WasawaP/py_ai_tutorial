# 项目P05：零售超市经营分析

> ⚠️ **项目状态**: 规划中（未实现）

## 📋 项目概述

本项目将通过分析零售超市的经营数据，运用 SWOT 分析方法，帮助超市管理者识别优势、劣势、机会和威胁，制定科学的经营策略。

### 项目目标

1. **销售趋势分析**：分析商品销售趋势，识别畅销品类和滞销品类
2. **SWOT 分析**：从数据角度评估超市的优势（Strengths）、劣势（Weaknesses）、机会（Opportunities）、威胁（Threats）
3. **客户行为分析**：分析购物篮数据，发现商品关联规则
4. **库存优化建议**：基于销售数据提供库存管理优化建议

### 业务价值

- 识别核心竞争优势，强化优势品类
- 发现运营短板，及时改进薄弱环节
- 捕捉市场机会，开拓新的增长点
- 应对竞争威胁，制定防御策略

## 📊 数据集说明

### 数据格式（规划）

- **文件名**: `retail_supermarket.csv`
- **样本数量**: 约 200,000 条交易记录
- **时间范围**: 2023年全年
- **数据维度**: 商品信息、销售记录、客户行为、库存数据

### 核心字段（规划）

| 字段名 | 类型 | 说明 |
|--------|------|------|
| transaction_id | string | 交易编号 |
| transaction_date | date | 交易日期 |
| product_id | string | 商品编号 |
| product_name | string | 商品名称 |
| category | string | 商品类别 |
| quantity | int | 购买数量 |
| unit_price | float | 单价 |
| total_amount | float | 总金额 |
| customer_id | string | 会员编号 |
| store_location | string | 门店位置 |

## 🎯 学习要点（规划）

### 数据分析技能
- 时间序列分析（销售趋势）
- SWOT 分析框架应用
- 关联规则挖掘（Apriori 算法）
- 库存周转率计算

### 可视化技能
- 销售仪表盘设计
- SWOT 矩阵图
- 商品关联网络图

## 🚀 快速开始

### 项目状态

本项目目前处于规划阶段，预计在 **v1.0.0** 版本中实现。

如果你对本项目感兴趣，欢迎：
- 查看 [GitHub Issues](https://github.com/shychee/py_ai_tutorial/issues) 了解开发进度
- 参与项目开发，提交 Pull Request
- 提供需求建议或数据集推荐

## 📚 相关资源

- [阶段3：机器学习与数据挖掘](../../index.md)
- [M02：Pandas 实战](../../02-pandas-practice/README.md)
- [M04：机器学习进阶](../../04-ml-advanced/README.md)

## 🔗 其他项目

- [P01：医疗数据分析](../p01-healthcare/README.md)
- [P02：服装零售分析](../p02-ecommerce/README.md)
- [P03：银行营销分析](../p03-finance/README.md)
- [P04：通讯客户响应](../p04-telecom/README.md)
- **P05：零售超市分析**（当前）
- [P06：滴滴运营分析](../p06-internet/README.md)

---

**想要提前学习？** 可以先完成 [P02：服装零售分析](../p02-ecommerce/README.md)，它包含类似的零售分析技能！
