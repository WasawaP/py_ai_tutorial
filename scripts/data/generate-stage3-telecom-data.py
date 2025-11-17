#!/usr/bin/env python3
"""
生成P04-Telecom项目的模拟客户数据
telecom_customer_data.csv

数据特点:
- 约100,000条客户记录
- 流失率约15%
- 包含RFM分析所需的时间、交易、金额字段
- 包含流失预测所需的服务质量指标
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path

# 设置随机种子确保可复现
np.random.seed(42)

# 数据规模
N_CUSTOMERS = 100000
CHURN_RATE = 0.15  # 流失率15%

print(f"开始生成{N_CUSTOMERS}条客户数据...")

# 1. 生成客户ID
customer_ids = [f"C{str(i).zfill(6)}" for i in range(1, N_CUSTOMERS + 1)]

# 2. 生成注册日期 (2023年1月 - 2024年6月)
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 6, 30)
date_range = (end_date - start_date).days

registration_dates = [
    start_date + timedelta(days=np.random.randint(0, date_range))
    for _ in range(N_CUSTOMERS)
]

# 3. 生成服务类型 (移动套餐、宽带、固话)
service_types = np.random.choice(
    ["移动套餐", "宽带", "固话", "移动+宽带", "全业务"],
    size=N_CUSTOMERS,
    p=[0.45, 0.25, 0.10, 0.15, 0.05]
)

# 4. 生成合约类型
contract_types = np.random.choice(
    ["月付", "年付", "按量付费"],
    size=N_CUSTOMERS,
    p=[0.50, 0.30, 0.20]
)

# 5. 生成年龄段
age_groups = np.random.choice(
    ["18-25", "26-35", "36-45", "46-55", "56+"],
    size=N_CUSTOMERS,
    p=[0.15, 0.35, 0.25, 0.15, 0.10]
)

# 6. 生成地区
regions = np.random.choice(
    ["华东", "华北", "华南", "华中", "西南", "西北", "东北"],
    size=N_CUSTOMERS,
    p=[0.25, 0.20, 0.20, 0.15, 0.10, 0.05, 0.05]
)

# 7. 生成交易次数 (24个月内，正态分布)
# 活跃客户: 平均每月2-3次
transaction_counts = np.random.gamma(shape=2, scale=15, size=N_CUSTOMERS).astype(int)
transaction_counts = np.clip(transaction_counts, 1, 100)  # 限制在1-100次

# 8. 生成平均单次消费金额 (正态分布，均值100元)
avg_amounts = np.random.gamma(shape=4, scale=25, size=N_CUSTOMERS)
avg_amounts = np.clip(avg_amounts, 10, 500)  # 限制在10-500元

# 9. 计算总消费金额
total_amounts = transaction_counts * avg_amounts

# 10. 生成最后交易日期
# 流失客户: 90-365天未交易
# 活跃客户: 0-90天内有交易
analysis_date = datetime(2024, 12, 31)

# 先生成流失标签
churn_labels = np.random.binomial(1, CHURN_RATE, N_CUSTOMERS)

last_transaction_dates = []
for i, churned in enumerate(churn_labels):
    if churned == 1:
        # 流失客户: 90-365天未交易
        days_ago = np.random.randint(90, 366)
    else:
        # 活跃客户: 0-90天内有交易
        days_ago = np.random.randint(0, 91)

    last_date = analysis_date - timedelta(days=days_ago)
    # 确保最后交易日期晚于注册日期
    if last_date < registration_dates[i]:
        last_date = registration_dates[i] + timedelta(days=np.random.randint(1, 30))
    last_transaction_dates.append(last_date)

# 11. 生成投诉次数 (泊松分布，流失客户投诉更多)
complaint_counts = []
for churned in churn_labels:
    if churned == 1:
        # 流失客户平均投诉2次
        count = np.random.poisson(2)
    else:
        # 活跃客户平均投诉0.5次
        count = np.random.poisson(0.5)
    complaint_counts.append(min(count, 10))  # 最多10次

# 12. 生成客服呼叫次数 (泊松分布)
service_call_counts = []
for churned in churn_labels:
    if churned == 1:
        # 流失客户呼叫更频繁
        count = np.random.poisson(4)
    else:
        count = np.random.poisson(2)
    service_call_counts.append(min(count, 20))  # 最多20次

# 13. 创建DataFrame
df = pd.DataFrame({
    'customer_id': customer_ids,
    'registration_date': registration_dates,
    'last_transaction_date': last_transaction_dates,
    'transaction_count': transaction_counts,
    'total_amount': total_amounts.round(2),
    'avg_amount_per_transaction': avg_amounts.round(2),
    'service_type': service_types,
    'contract_type': contract_types,
    'complaint_count': complaint_counts,
    'service_call_count': service_call_counts,
    'churn': churn_labels,
    'age_group': age_groups,
    'region': regions
})

# 14. 数据质量检查
print("\n数据生成完成! 数据质量检查:")
print(f"  总记录数: {len(df)}")
print(f"  流失率: {df['churn'].mean():.2%}")
print(f"  平均交易次数: {df['transaction_count'].mean():.1f}")
print(f"  平均总消费: {df['total_amount'].mean():.2f}元")
print(f"  缺失值: {df.isnull().sum().sum()}")

# 15. 保存数据
output_dir = Path(__file__).parent.parent.parent / "data" / "stage3"
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "telecom_customer_data.csv"
df.to_csv(output_file, index=False, encoding="utf-8")

print(f"\n数据已保存至: {output_file}")
print(f"文件大小: {output_file.stat().st_size / 1024 / 1024:.2f} MB")

# 16. 生成数据摘要
print("\n=== 数据集摘要 ===")
print("\n数值型特征统计:")
print(df[['transaction_count', 'total_amount', 'avg_amount_per_transaction',
         'complaint_count', 'service_call_count']].describe())

print("\n类别型特征分布:")
print(f"\n服务类型分布:")
print(df['service_type'].value_counts())

print(f"\n合约类型分布:")
print(df['contract_type'].value_counts())

print(f"\n流失情况:")
print(f"  未流失: {(df['churn']==0).sum()}人 ({(df['churn']==0).sum()/len(df)*100:.1f}%)")
print(f"  已流失: {(df['churn']==1).sum()}人 ({(df['churn']==1).sum()/len(df)*100:.1f}%)")

print("\n数据生成成功! 🎉")
print("现在可以运行P04-Telecom项目了:")
print("  python docs/stage3/projects/p04-telecom/src/analyze.py --config configs/default.yaml")
