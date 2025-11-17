#!/usr/bin/env python3
"""
生成P04-Telecom项目的模拟客户数据 (纯Python版本,无需pandas)
telecom_customer_data.csv
"""

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

# 设置随机种子
random.seed(42)

# 数据规模
N_CUSTOMERS = 100000
CHURN_RATE = 0.15

print(f"开始生成{N_CUSTOMERS}条客户数据...")

# 数据定义
service_types = ["移动套餐", "宽带", "固话", "移动+宽带", "全业务"]
service_weights = [0.45, 0.25, 0.10, 0.15, 0.05]

contract_types = ["月付", "年付", "按量付费"]
contract_weights = [0.50, 0.30, 0.20]

age_groups = ["18-25", "26-35", "36-45", "46-55", "56+"]
age_weights = [0.15, 0.35, 0.25, 0.15, 0.10]

regions = ["华东", "华北", "华南", "华中", "西南", "西北", "东北"]
region_weights = [0.25, 0.20, 0.20, 0.15, 0.10, 0.05, 0.05]


def weighted_choice(choices, weights):
    """加权随机选择"""
    total = sum(weights)
    r = random.uniform(0, total)
    cumsum = 0
    for choice, weight in zip(choices, weights):
        cumsum += weight
        if r <= cumsum:
            return choice
    return choices[-1]


def gamma_sample(shape, scale):
    """简单的Gamma分布采样 (使用正态分布近似)"""
    return abs(random.gauss(shape * scale, (shape * scale) ** 0.5))


def poisson_sample(lam):
    """泊松分布采样"""
    L = 2.71828 ** (-lam)
    k = 0
    p = 1.0
    while p > L:
        k += 1
        p *= random.random()
    return k - 1


# 准备输出目录
output_dir = Path(__file__).parent.parent.parent / "data" / "stage3"
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "telecom_customer_data.csv"

# 打开CSV文件写入
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    # 写入表头
    headers = [
        'customer_id', 'registration_date', 'last_transaction_date',
        'transaction_count', 'total_amount', 'avg_amount_per_transaction',
        'service_type', 'contract_type', 'complaint_count',
        'service_call_count', 'churn', 'age_group', 'region'
    ]
    writer.writerow(headers)

    # 生成数据
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 6, 30)
    date_range_days = (end_date - start_date).days
    analysis_date = datetime(2024, 12, 31)

    churn_count = 0

    for i in range(1, N_CUSTOMERS + 1):
        if i % 10000 == 0:
            print(f"  已生成 {i}/{N_CUSTOMERS} 条记录...")

        # 1. 客户ID
        customer_id = f"C{str(i).zfill(6)}"

        # 2. 注册日期
        reg_days = random.randint(0, date_range_days)
        registration_date = start_date + timedelta(days=reg_days)

        # 3. 服务类型
        service_type = weighted_choice(service_types, service_weights)

        # 4. 合约类型
        contract_type = weighted_choice(contract_types, contract_weights)

        # 5. 年龄段
        age_group = weighted_choice(age_groups, age_weights)

        # 6. 地区
        region = weighted_choice(regions, region_weights)

        # 7. 流失标签
        churn = 1 if random.random() < CHURN_RATE else 0
        if churn == 1:
            churn_count += 1

        # 8. 交易次数 (Gamma分布近似)
        transaction_count = max(1, min(100, int(gamma_sample(2, 15))))

        # 9. 平均单次消费
        avg_amount = max(10, min(500, gamma_sample(4, 25)))

        # 10. 总消费金额
        total_amount = round(transaction_count * avg_amount, 2)
        avg_amount = round(avg_amount, 2)

        # 11. 最后交易日期
        if churn == 1:
            # 流失客户: 90-365天未交易
            days_ago = random.randint(90, 365)
        else:
            # 活跃客户: 0-90天内有交易
            days_ago = random.randint(0, 90)

        last_transaction_date = analysis_date - timedelta(days=days_ago)
        # 确保不早于注册日期
        if last_transaction_date < registration_date:
            last_transaction_date = registration_date + timedelta(days=random.randint(1, 30))

        # 12. 投诉次数
        if churn == 1:
            complaint_count = min(10, poisson_sample(2))
        else:
            complaint_count = min(10, poisson_sample(0.5))

        # 13. 客服呼叫次数
        if churn == 1:
            service_call_count = min(20, poisson_sample(4))
        else:
            service_call_count = min(20, poisson_sample(2))

        # 写入行
        row = [
            customer_id,
            registration_date.strftime('%Y-%m-%d'),
            last_transaction_date.strftime('%Y-%m-%d'),
            transaction_count,
            total_amount,
            avg_amount,
            service_type,
            contract_type,
            complaint_count,
            service_call_count,
            churn,
            age_group,
            region
        ]
        writer.writerow(row)

print(f"\n数据生成完成!")
print(f"  总记录数: {N_CUSTOMERS}")
print(f"  流失客户数: {churn_count}")
print(f"  实际流失率: {churn_count/N_CUSTOMERS:.2%}")
print(f"\n数据已保存至: {output_file}")

file_size_mb = output_file.stat().st_size / 1024 / 1024
print(f"文件大小: {file_size_mb:.2f} MB")

print("\n数据生成成功! 🎉")
print("\n现在可以运行P04-Telecom项目了:")
print("  cd docs/stage3/projects/p04-telecom")
print("  python src/analyze.py --config configs/default.yaml")
