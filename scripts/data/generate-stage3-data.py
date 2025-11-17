#!/usr/bin/env python3
"""
Stage 3 Synthetic Data Generation Script
生成阶段3的合成数据集

Usage:
    uv run python scripts/data/generate-stage3-data.py
    uv run python scripts/data/generate-stage3-data.py --dataset P01
    uv run python scripts/data/generate-stage3-data.py --quick  # 生成小规模测试数据
"""

import argparse
import hashlib
import sys
from pathlib import Path
from datetime import datetime, timedelta
import random

import pandas as pd
import numpy as np

# 项目根目录
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "stage3"


class DataGenerator:
    """数据生成器基类"""

    def __init__(self, quick_mode: bool = False):
        self.quick_mode = quick_mode
        self.data_dir = DATA_DIR
        self.data_dir.mkdir(parents=True, exist_ok=True)

        # 设置随机种子保证可复现
        np.random.seed(42)
        random.seed(42)

    def calculate_checksum(self, file_path: Path) -> str:
        """计算文件SHA256校验和"""
        sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                sha256.update(chunk)
        return sha256.hexdigest()

    def save_and_report(self, df: pd.DataFrame, filename: str, description: str):
        """保存数据并报告统计信息"""
        file_path = self.data_dir / filename

        print(f"\n{'='*60}")
        print(f"生成数据集: {description}")
        print(f"{'='*60}")
        print(f"文件名: {filename}")
        print(f"行数: {len(df):,}")
        print(f"列数: {len(df.columns)}")
        print(f"内存占用: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

        # 保存为CSV
        df.to_csv(file_path, index=False, encoding='utf-8')
        file_size_mb = file_path.stat().st_size / (1024**2)
        checksum = self.calculate_checksum(file_path)

        print(f"文件大小: {file_size_mb:.2f} MB")
        print(f"SHA256: {checksum}")
        print(f"保存位置: {file_path}")
        print(f"✅ 完成")

        return checksum, file_size_mb


class P01HospitalDataGenerator(DataGenerator):
    """P01: 朝阳医院销售数据生成器"""

    def generate(self):
        """生成医院销售数据"""
        n_rows = 1000 if self.quick_mode else 50000  # 快速模式1K，完整模式50K（原计划500K太大）

        print(f"\n生成 P01 医院销售数据 ({n_rows:,} 行)...")

        # 日期范围
        start_date = datetime(2022, 1, 1)
        end_date = datetime(2024, 12, 31)
        date_range = (end_date - start_date).days

        # 药品分类和名称
        categories = [
            "抗生素", "心血管药物", "消化系统药物", "呼吸系统药物", "神经系统药物",
            "内分泌药物", "维生素", "中成药", "外用药", "急救药品",
            "抗肿瘤药物", "免疫调节药物", "血液系统药物", "抗病毒药物", "镇痛药物"
        ]

        products_by_category = {
            "抗生素": ["阿莫西林胶囊", "头孢克肟胶囊", "阿奇霉素片", "青霉素注射液"],
            "心血管药物": ["硝苯地平缓释片", "阿托伐他汀钙片", "阿司匹林肠溶片", "美托洛尔片"],
            "消化系统药物": ["奥美拉唑肠溶胶囊", "多潘立酮片", "蒙脱石散", "复方消化酶胶囊"],
            "呼吸系统药物": ["氨溴索口服液", "复方甘草片", "孟鲁司特钠片", "布地奈德混悬液"],
            "神经系统药物": ["谷维素片", "维生素B1片", "加巴喷丁胶囊", "卡马西平片"],
            "内分泌药物": ["二甲双胍片", "格列美脲片", "甲状腺片", "胰岛素注射液"],
            "维生素": ["维生素C片", "维生素B族片", "钙片", "鱼肝油"],
            "中成药": ["感冒清热颗粒", "板蓝根颗粒", "藿香正气水", "六味地黄丸"],
            "外用药": ["红霉素软膏", "云南白药气雾剂", "碘伏消毒液", "创可贴"],
            "急救药品": ["硝酸甘油片", "肾上腺素注射液", "阿托品注射液", "地塞米松注射液"],
            "抗肿瘤药物": ["紫杉醇注射液", "顺铂注射液", "吉非替尼片", "伊马替尼片"],
            "免疫调节药物": ["转移因子口服液", "胸腺肽注射液", "左旋咪唑片", "匹多莫德口服液"],
            "血液系统药物": ["叶酸片", "维生素K1注射液", "右旋糖酐铁片", "华法林钠片"],
            "抗病毒药物": ["奥司他韦胶囊", "阿昔洛韦片", "利巴韦林片", "干扰素注射液"],
            "镇痛药物": ["布洛芬缓释胶囊", "对乙酰氨基酚片", "塞来昔布胶囊", "曲马多片"]
        }

        customer_types = ["个人", "机构"]
        departments = ["内科", "外科", "儿科", "妇科", "骨科", "神经科", "心血管科", "呼吸科", "消化科", "肿瘤科"]
        regions = ["北京市朝阳区", "北京市海淀区", "北京市东城区", "北京市西城区", "北京市丰台区"]
        payment_methods = ["医保", "自费", "商业保险"]

        # 生成数据
        data = []
        for i in range(n_rows):
            # 随机日期
            order_date = start_date + timedelta(days=random.randint(0, date_range))

            # 随机选择类别和产品
            category = random.choice(categories)
            product_name = random.choice(products_by_category[category])

            # 价格范围根据类别不同
            if category in ["抗肿瘤药物", "免疫调节药物"]:
                unit_price = round(random.uniform(50, 500), 2)
            elif category in ["急救药品", "抗病毒药物"]:
                unit_price = round(random.uniform(20, 200), 2)
            elif category in ["维生素", "外用药"]:
                unit_price = round(random.uniform(5, 50), 2)
            else:
                unit_price = round(random.uniform(10, 150), 2)

            # 数量
            quantity = random.randint(1, 20)

            # 总金额
            total_amount = round(unit_price * quantity, 2)

            # 折扣率（90%-100%）
            discount_rate = round(random.uniform(0.90, 1.00), 2)
            total_amount = round(total_amount * discount_rate, 2)

            # 有效期（1-3年后）
            expiry_date = order_date + timedelta(days=random.randint(365, 1095))

            data.append({
                'order_id': f"ORD{order_date.strftime('%Y%m%d')}{i:06d}",
                'order_date': order_date.strftime('%Y-%m-%d'),
                'product_name': product_name,
                'category': category,
                'quantity': quantity,
                'unit_price': unit_price,
                'total_amount': total_amount,
                'customer_type': random.choice(customer_types),
                'department': random.choice(departments),
                'doctor_name': f"医生{random.randint(1, 100)}",
                'manufacturer': f"制药厂{random.randint(1, 50)}",
                'batch_number': f"B{random.randint(202201, 202412)}{random.randint(1000, 9999)}",
                'expiry_date': expiry_date.strftime('%Y-%m-%d'),
                'payment_method': random.choice(payment_methods),
                'discount_rate': discount_rate,
                'sales_rep': f"代表{random.randint(1, 30)}",
                'region': random.choice(regions),
                'notes': "" if random.random() > 0.005 else f"备注{random.randint(1, 100)}"
            })

        df = pd.DataFrame(data)

        # 引入一些数据质量问题
        if not self.quick_mode:
            # 缺失值 (0.5%)
            missing_indices = np.random.choice(df.index, size=int(len(df) * 0.005), replace=False)
            df.loc[missing_indices, 'notes'] = np.nan

            # 重复值 (0.2%)
            duplicate_indices = np.random.choice(df.index, size=int(len(df) * 0.002), replace=False)
            df = pd.concat([df, df.loc[duplicate_indices]], ignore_index=True)

            # 异常值 (1%)
            outlier_indices = np.random.choice(df.index, size=int(len(df) * 0.01), replace=False)
            df.loc[outlier_indices, 'unit_price'] = df.loc[outlier_indices, 'unit_price'] * random.uniform(5, 10)

        return self.save_and_report(df, "hospital_sales.csv", "朝阳医院销售数据")


class P02EcommerceDataGenerator(DataGenerator):
    """P02: 服装零售销售数据生成器"""

    def generate(self):
        """生成服装零售数据"""
        n_rows = 2000 if self.quick_mode else 30000
        n_customers = 500 if self.quick_mode else 5000
        n_products = 200 if self.quick_mode else 2000

        print(f"\n生成 P02 服装零售数据 ({n_rows:,} 行)...")

        # 商品类别
        categories = ["上衣", "裤子", "裙子", "外套", "鞋类", "配饰", "内衣", "运动装"]
        brands = ["优衣库", "ZARA", "H&M", "GAP", "无印良品", "UR", "ONLY", "VERO MODA"]
        sizes = ["XS", "S", "M", "L", "XL", "XXL"]
        colors = ["黑色", "白色", "蓝色", "灰色", "红色", "卡其色", "绿色", "黄色"]

        # 生成日期范围
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2024, 12, 31)
        date_range = (end_date - start_date).days

        data = []
        for i in range(n_rows):
            order_date = start_date + timedelta(days=random.randint(0, date_range))
            category = random.choice(categories)

            # 价格根据类别
            price_ranges = {
                "上衣": (59, 299), "裤子": (99, 399), "裙子": (79, 499),
                "外套": (199, 999), "鞋类": (129, 699), "配饰": (29, 199),
                "内衣": (39, 159), "运动装": (89, 499)
            }
            price = round(random.uniform(*price_ranges[category]), 2)
            quantity = random.randint(1, 5)

            data.append({
                'order_id': f"EC{order_date.strftime('%Y%m%d')}{i:08d}",
                'customer_id': f"C{random.randint(1, n_customers):06d}",
                'order_date': order_date.strftime('%Y-%m-%d'),
                'product_id': f"P{random.randint(1, n_products):06d}",
                'product_name': f"{random.choice(brands)} {category}",
                'category': category,
                'brand': random.choice(brands),
                'size': random.choice(sizes),
                'color': random.choice(colors),
                'price': price,
                'quantity': quantity,
                'total_amount': round(price * quantity, 2),
                'discount': round(random.uniform(0, 0.3), 2),
                'payment_method': random.choice(["支付宝", "微信", "银行卡", "现金"]),
                'shipping_method': random.choice(["快递", "自提", "同城配送"]),
                'region': random.choice(["华北", "华东", "华南", "华中", "西南", "东北"]),
                'customer_age': random.randint(18, 65),
                'customer_gender': random.choice(["男", "女"]),
                'is_member': random.choice([True, False]),
                'channel': random.choice(["线上", "线下", "小程序", "APP"]),
                'status': random.choice(["已完成", "已完成", "已完成", "已退货"])
            })

        df = pd.DataFrame(data)
        return self.save_and_report(df, "clothing_retail.csv", "服装零售销售数据")


class P03BankMarketingDownloader(DataGenerator):
    """P03: 银行营销数据下载器（使用UCI真实数据）"""

    def generate(self):
        """尝试下载UCI银行数据，失败则生成模拟数据"""
        print(f"\n尝试下载 P03 银行营销数据 (UCI数据集)...")

        # UCI数据集的直接下载链接
        urls = [
            "https://archive.ics.uci.edu/ml/machine-learning-databases/00222/bank.zip",
            "https://raw.githubusercontent.com/madmashup/targeted-marketing-predictive-engine/master/banking.csv"
        ]

        import urllib.request
        import zipfile
        import io

        for url in urls:
            try:
                print(f"尝试从 {url} 下载...")
                response = urllib.request.urlopen(url, timeout=30)

                if url.endswith('.zip'):
                    # 处理ZIP文件
                    zip_data = io.BytesIO(response.read())
                    with zipfile.ZipFile(zip_data) as z:
                        # 找到CSV文件
                        csv_files = [f for f in z.namelist() if f.endswith('.csv')]
                        if csv_files:
                            with z.open(csv_files[0]) as f:
                                df = pd.read_csv(f, sep=';')
                                print(f"✅ 成功下载UCI数据集")
                                return self.save_and_report(df, "bank_marketing.csv", "银行营销数据 (UCI)")
                else:
                    # 直接CSV
                    df = pd.read_csv(response)
                    print(f"✅ 成功下载数据集")
                    return self.save_and_report(df, "bank_marketing.csv", "银行营销数据")

            except Exception as e:
                print(f"下载失败: {e}")
                continue

        # 如果下载失败，生成模拟数据
        print("⚠️  下载失败，生成模拟数据...")
        return self._generate_synthetic()

    def _generate_synthetic(self):
        """生成模拟银行营销数据"""
        n_rows = 500 if self.quick_mode else 5000

        data = []
        for i in range(n_rows):
            age = random.randint(18, 80)
            data.append({
                'age': age,
                'job': random.choice(['admin.', 'technician', 'services', 'management', 'retired', 'blue-collar', 'unemployed', 'entrepreneur', 'housemaid', 'self-employed', 'student']),
                'marital': random.choice(['married', 'single', 'divorced']),
                'education': random.choice(['primary', 'secondary', 'tertiary', 'unknown']),
                'default': random.choice(['no', 'yes']),
                'balance': random.randint(-5000, 50000),
                'housing': random.choice(['no', 'yes']),
                'loan': random.choice(['no', 'yes']),
                'contact': random.choice(['cellular', 'telephone', 'unknown']),
                'day': random.randint(1, 31),
                'month': random.choice(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']),
                'duration': random.randint(0, 3000),
                'campaign': random.randint(1, 10),
                'pdays': random.randint(-1, 500),
                'previous': random.randint(0, 5),
                'poutcome': random.choice(['unknown', 'failure', 'success', 'other']),
                'y': random.choice(['no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes'])  # 不平衡
            })

        df = pd.DataFrame(data)
        return self.save_and_report(df, "bank_marketing.csv", "银行营销数据 (模拟)")


def main():
    parser = argparse.ArgumentParser(description="生成Stage 3合成数据集")
    parser.add_argument('--dataset', type=str, help='仅生成指定数据集 (如: P01, P02, P03)')
    parser.add_argument('--quick', action='store_true', help='快速模式：生成小规模测试数据')
    args = parser.parse_args()

    print("="*60)
    print("Stage 3 数据生成工具")
    print("="*60)
    print(f"模式: {'快速测试' if args.quick else '完整数据'}")
    print(f"输出目录: {DATA_DIR}")
    print()

    # 定义生成器
    generators = {
        'P01': P01HospitalDataGenerator,
        'P02': P02EcommerceDataGenerator,
        'P03': P03BankMarketingDownloader,
    }

    # 如果指定了特定数据集
    if args.dataset:
        dataset = args.dataset.upper()
        if dataset not in generators:
            print(f"❌ 错误: 未知数据集 '{dataset}'")
            print(f"可用数据集: {', '.join(generators.keys())}")
            sys.exit(1)

        generator = generators[dataset](quick_mode=args.quick)
        generator.generate()
    else:
        # 生成所有已实现的数据集
        for name, generator_class in generators.items():
            try:
                generator = generator_class(quick_mode=args.quick)
                generator.generate()
            except Exception as e:
                print(f"\n❌ 生成 {name} 失败: {e}")
                import traceback
                traceback.print_exc()

    print("\n" + "="*60)
    print("✅ 数据生成完成")
    print("="*60)
    print(f"\n💡 提示: 使用以下命令验证数据:")
    print(f"   uv run python scripts/data/verify.py --stage 3")


if __name__ == '__main__':
    main()
