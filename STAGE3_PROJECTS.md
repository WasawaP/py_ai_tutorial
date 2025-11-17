# Stage 3 项目位置索引

> **重要提示**: 所有Stage 3项目统一存放在 `specs/002-ai-tutorial-stages/docs/stage3/projects/`

## 📍 快速导航

### 项目目录
```bash
cd specs/002-ai-tutorial-stages/docs/stage3/projects/
```

### 三个已完成项目

| 项目 | 完整路径 | 快速命令 |
|-----|---------|---------|
| **P01 医院销售** | `specs/002-ai-tutorial-stages/docs/stage3/projects/p01-healthcare/` | `cd specs/002-ai-tutorial-stages/docs/stage3/projects/p01-healthcare` |
| **P02 服装零售** | `specs/002-ai-tutorial-stages/docs/stage3/projects/p02-ecommerce/` | `cd specs/002-ai-tutorial-stages/docs/stage3/projects/p02-ecommerce` |
| **P03 银行营销** | `specs/002-ai-tutorial-stages/docs/stage3/projects/p03-bank-marketing/` | `cd specs/002-ai-tutorial-stages/docs/stage3/projects/p03-bank-marketing` |

### 数据文件位置
```bash
# 所有数据在项目根目录
data/stage3/
├── hospital_sales.csv      # P01: 1,000行
├── clothing_retail.csv     # P02: 2,000行
└── bank_marketing.csv      # P03: 45,211行
```

## 🎯 项目详情

### P01 医院销售分析
- **路径**: `specs/002-ai-tutorial-stages/docs/stage3/projects/p01-healthcare/`
- **类型**: EDA探索性数据分析
- **文件**:
  - `README.md` - 11.5KB，详细文档
  - `src/analyze.py` - 620行，完整分析脚本
  - `notebooks/analysis.ipynb` - 30+图表交互式教程
  - `outputs/` - 6张图表 + 完整报告

### P02 服装零售RFM分析
- **路径**: `specs/002-ai-tutorial-stages/docs/stage3/projects/p02-ecommerce/`
- **类型**: RFM客户价值分析
- **文件**:
  - `README.md` - 11.3KB，RFM模型详解
  - `src/analyze.py` - 150行，RFM分群脚本
  - `notebooks/analysis.ipynb` - 10章节完整教程
  - `outputs/` - 客户细分图 + RFM热力图 + 营销报告

### P03 银行营销分类预测
- **路径**: `specs/002-ai-tutorial-stages/docs/stage3/projects/p03-bank-marketing/`
- **类型**: 二分类机器学习
- **文件**:
  - `README.md` - 详细算法原理（含公式）
  - `src/analyze.py` - 500行，分类模型脚本
  - `notebooks/analysis.ipynb` - 11章节，36+图表
  - `outputs/models/` - 3个训练好的模型（逻辑回归、决策树、scaler）
  - `outputs/figures/` - 5张图表（混淆矩阵、ROC曲线、特征重要性×2、相关性）
  - `outputs/reports/` - 分类报告

## 🚀 运行项目

### 方法1: 命令行运行

```bash
# P01
cd specs/002-ai-tutorial-stages/docs/stage3/projects/p01-healthcare
uv run --no-project --with pandas --with numpy --with matplotlib --with seaborn --with pyyaml \
  python src/analyze.py --config configs/default.yaml

# P02
cd specs/002-ai-tutorial-stages/docs/stage3/projects/p02-ecommerce
uv run --no-project --with pandas --with numpy --with matplotlib --with seaborn --with pyyaml \
  python src/analyze.py --config configs/default.yaml

# P03
cd specs/002-ai-tutorial-stages/docs/stage3/projects/p03-bank-marketing
uv run --no-project --with pandas --with numpy --with scikit-learn --with matplotlib --with seaborn --with pyyaml \
  python src/analyze.py --config configs/default.yaml
```

### 方法2: Jupyter Notebook

```bash
# 进入任意项目
cd specs/002-ai-tutorial-stages/docs/stage3/projects/p01-healthcare

# 启动notebook
jupyter notebook notebooks/analysis.ipynb
```

## 📊 验证报告位置

```bash
/tmp/p01_verification.md  # P01验证报告
/tmp/p02_verification.md  # P02验证报告
/tmp/p03_verification.md  # P03验证报告
```

## ⚙️ 数据生成脚本

```bash
scripts/data/generate-stage3-data.py  # P01-P03数据生成器
```

运行命令：
```bash
python scripts/data/generate-stage3-data.py --quick  # 快速模式
python scripts/data/generate-stage3-data.py          # 完整模式
```

## 📂 项目结构模板

每个项目都遵循统一结构：
```
pXX-project/
├── README.md           # 项目文档
├── pyproject.toml      # 依赖配置
├── src/
│   ├── __init__.py
│   └── analyze.py      # 主脚本
├── notebooks/
│   └── analysis.ipynb  # 教程
├── configs/
│   └── default.yaml    # 配置
└── outputs/            # 自动生成
    ├── analysis.log
    ├── figures/
    ├── reports/
    └── models/         # 仅P03有
```

## ✅ 完成状态

| 项目 | 状态 | 数据 | 脚本 | Notebook | 验证 |
|-----|------|-----|------|---------|------|
| P01 医院销售 | ✅ | ✅ 1K | ✅ 620行 | ✅ 30+图表 | ✅ |
| P02 服装零售 | ✅ | ✅ 2K | ✅ 150行 | ✅ 10章节 | ✅ |
| P03 银行营销 | ✅ | ✅ 45K | ✅ 500行 | ✅ 11章节 | ✅ |
| P04 电信客户 | ⏳ | - | - | - | - |
| P05 零售超市 | ⏳ | - | - | - | - |
| P06 滴滴运营 | ⏳ | - | - | - | - |
| P07 淘宝电商 | ⏳ | - | - | - | - |
| P08 航空客户 | ⏳ | - | - | - | - |
| P09 信贷风险 | ⏳ | - | - | - | - |

**总进度**: 3/9 (33.3%)

## 🔍 常见问题

### Q: 找不到项目文件？
**A**: 所有项目在 `specs/002-ai-tutorial-stages/docs/stage3/projects/`，不在 `docs/stage3/projects/`

### Q: 数据文件在哪？
**A**: 项目根目录的 `data/stage3/` 下（不在specs目录内）

### Q: Notebook报错找不到数据？
**A**: Notebook中数据路径已更新为 `../../../../../../../data/stage3/xxx.csv`（向上7层到项目根目录）

### Q: 如何验证项目完整性？
**A**: 查看 `/tmp/pXX_verification.md` 验证报告

---

**最后更新**: 2025-11-13 18:10
**维护**: Claude Code Assistant

**重要提醒**: 🚨 **所有Stage 3项目都在 `specs/002-ai-tutorial-stages/docs/stage3/projects/`**
