# 先修要求 (Prerequisites)

**目标学员**: 具备3-5年Python后端开发经验的工程师，希望系统学习AI技术

本教程适合你，如果你:
- ✅ 熟悉Python语法（函数、类、模块、异常处理）
- ✅ 有命令行使用经验（Linux/macOS Terminal 或 Windows PowerShell）
- ✅ 理解基本的版本控制（Git）
- ✅ 能阅读英文技术文档
- ❌ **不需要**AI/机器学习背景（从零开始）

---

## 📋 必需技能清单

### 1. Python编程 (必需)

**期望水平**: 能独立编写中等规模的Python应用

<details>
<summary><strong>自测清单</strong> (点击展开)</summary>

- [ ] 熟练使用Python基础语法 (变量、循环、条件、函数)
- [ ] 理解面向对象编程 (类、继承、多态)
- [ ] 会使用Python标准库 (os, sys, pathlib, json, csv)
- [ ] 理解异常处理与上下文管理器 (try/except, with)
- [ ] 会使用第三方包 (pip install, import)
- [ ] 能阅读和调试他人的Python代码

**推荐资源** (若需要补习):
- 官方教程: https://docs.python.org/3/tutorial/
- 《Python Cookbook》(中文版)
- Real Python: https://realpython.com/

</details>

---

### 2. 命令行基础 (必需)

**期望水平**: 能在终端中完成文件操作、运行脚本、管理环境

<details>
<summary><strong>自测清单</strong></summary>

- [ ] 会使用基本命令 (cd, ls, mkdir, cp, rm)
- [ ] 理解文件路径 (绝对路径 vs 相对路径)
- [ ] 会运行Python脚本 (`python script.py`)
- [ ] 会查看帮助文档 (`man`, `--help`)
- [ ] 会使用环境变量 (export, PATH)

**速成指南**:
```bash
# macOS/Linux
cd ~                    # 进入用户主目录
ls -la                  # 列出所有文件（含隐藏）
mkdir projects          # 创建目录
cd projects             # 进入目录
pwd                     # 显示当前路径
python3 --version       # 查看Python版本

# Windows PowerShell
cd ~
ls -Force               # 列出所有文件
mkdir projects
cd projects
pwd
python --version
```

</details>

---

### 3. 数学基础 (推荐，非必需)

**期望水平**: 高中数学 + 基础概率统计

<details>
<summary><strong>核心概念</strong> (教程会逐步讲解)</summary>

**阶段3 (机器学习) 需要**:
- 线性代数: 矩阵运算、向量点积 (教程中有NumPy实现)
- 概率统计: 均值、方差、正态分布、假设检验
- 微积分: 导数概念 (理解梯度下降，无需手算)

**阶段4 (深度学习) 需要**:
- 链式法则 (反向传播原理)
- 矩阵乘法 (神经网络前向传播)
- 凸优化基础 (损失函数最小化)

**阶段5 (LLM/AIGC) 需要**:
- 概率论 (语言模型、采样策略)
- 信息论基础 (交叉熵、KL散度)

**推荐资源**:
- 3Blue1Brown (YouTube): 线性代数与微积分可视化
- Khan Academy (可汗学院): 统计学与概率论
- 《程序员的数学》(日本，中文翻译版)

**重要提示**:
- 📚 教程会提供**通俗化数学讲解**，配合Python实现与可视化
- 🔢 不需要记忆公式，理解**直觉与应用**即可
- 💻 强调代码实现，数学公式作为补充

</details>

---

### 4. 英语阅读 (推荐)

**期望水平**: 能阅读技术文档、论文摘要、错误信息

<details>
<summary><strong>为什么需要英语？</strong></summary>

- 📚 主流框架文档 (PyTorch, TensorFlow) 以英文为主
- 📝 前沿论文 (arXiv) 多为英文
- 🐛 报错信息与Stack Overflow问答以英文为主
- 🚀 最新技术动态 (博客、GitHub) 英文更新最快

**本教程的语言策略**:
- ✅ 核心教学内容: 中文
- ✅ 代码注释: 中文
- ✅ 术语首次出现: 中英对照 (如: 准确率 Accuracy)
- ✅ 提供完整术语表: `docs/glossary.md`

**英语能力不足怎么办？**:
- 使用翻译工具 (DeepL, Google Translate)
- 查阅本教程的术语表
- 在学习社群提问

</details>

---

## 🛠️ 环境要求

### 硬件要求

| 组件 | 最低配置 | 推荐配置 | 说明 |
|------|---------|---------|------|
| **CPU** | 2核 | 4核+ | 阶段3可在2核运行 |
| **内存** | 8 GB | 16 GB | 阶段4/5推荐16GB |
| **硬盘** | 20 GB可用空间 | 50 GB | 含数据集与模型缓存 |
| **GPU** | 不需要 | NVIDIA GPU (4GB+ VRAM) 或 Apple Silicon | 阶段3不需要GPU；阶段4推荐GPU (可云端) |

---

### 软件要求

| 软件 | 版本要求 | 安装指引 |
|------|---------|---------|
| **操作系统** | macOS 10.15+, Ubuntu 20.04+, Windows 10/11 | - |
| **Python** | ≥3.9 (推荐3.11) | [快速开始指南](../specs/002-ai-tutorial-stages/quickstart.md) |
| **Git** | ≥2.20 | [Git官网](https://git-scm.com/) |
| **uv** | 最新版 | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| **Jupyter Lab** | ≥3.0 | `uv pip install jupyterlab` (安装依赖后) |

---

### 网络要求

- ✅ 能访问PyPI (Python包索引) - 若无法访问，可使用[国内镜像](troubleshooting.md#2-包管理与依赖问题)
- ✅ 能访问GitHub - 若无法访问，可使用Gitee镜像或离线数据包
- ⚠️ 阶段5需访问LLM API (DeepSeek/OpenAI) - 需API密钥

---

## 📚 推荐前置学习资源

### 若Python基础薄弱

**在线课程**:
- [Python官方教程](https://docs.python.org/zh-cn/3/tutorial/) (中文)
- [廖雪峰Python教程](https://www.liaoxuefeng.com/wiki/1016959663602400)
- [Real Python](https://realpython.com/) (英文，质量高)

**书籍**:
- 《Python编程：从入门到实践》(第2版)
- 《流畅的Python》(进阶)

**时间投入**: 1-2周 (每天2-3小时)

---

### 若数学基础薄弱

**线性代数**:
- 3Blue1Brown: [线性代数的本质](https://www.bilibili.com/video/BV1ys411472E) (视频，强烈推荐)
- 课程: MIT 18.06 Linear Algebra (中文字幕)

**概率统计**:
- Khan Academy: [统计与概率论](https://www.khanacademy.org/math/statistics-probability) (中文)
- 书籍: 《深入浅出统计学》(Head First Statistics)

**微积分**:
- 3Blue1Brown: [微积分的本质](https://www.bilibili.com/video/BV1qW411N7FU)
- 仅需理解导数概念，无需手算微积分

**时间投入**: 1周 (重点看视频，理解概念)

---

### 若Git不熟悉

**速成指南**:
```bash
# 克隆项目
git clone https://github.com/yourusername/py_ai_tutorial.git
cd py_ai_tutorial

# 查看状态
git status

# 拉取最新代码
git pull

# 创建分支（可选，用于实验）
git checkout -b my-experiments

# 提交更改（可选）
git add .
git commit -m "完成项目P01"
git push origin my-experiments
```

**推荐资源**:
- [Git简明指南](https://rogerdudler.github.io/git-guide/index.zh.html)
- [Learn Git Branching](https://learngitbranching.js.org/?locale=zh_CN) (交互式教学)

**时间投入**: 1-2小时 (学会克隆、拉取、提交即可)

---

## 🎯 学前自测

在开始学习前，请确认你能完成以下任务：

### 环境配置自测

```bash
# 1. 检查Python版本
python3 --version  # 应输出 Python 3.9+ (推荐3.11)

# 2. 创建虚拟环境
python3 -m venv test_env
source test_env/bin/activate  # Windows: test_env\Scripts\activate

# 3. 安装测试包
pip install numpy pandas matplotlib

# 4. 运行测试脚本
python -c "import numpy as np; import pandas as pd; import matplotlib.pyplot as plt; print('✅ 环境正常')"

# 5. 清理测试环境
deactivate
rm -rf test_env
```

**预期输出**: `✅ 环境正常`

---

### Python能力自测

运行以下代码，确保能理解每一行的含义：

```python
# 1. 数据处理
import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'score': [85, 90, 95]
}
df = pd.DataFrame(data)

# 2. 筛选与聚合
high_scorers = df[df['score'] >= 90]
avg_age = df['age'].mean()

# 3. 可视化
import matplotlib.pyplot as plt
plt.bar(df['name'], df['score'])
plt.title('Score Distribution')
plt.show()

# 4. 函数定义
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    else:
        return 'C'

df['grade'] = df['score'].apply(calculate_grade)
print(df)
```

**若能理解80%以上**: ✅ 可以开始学习
**若有困难**: 📚 建议先补习Python基础 (1-2周)

---

## 🚀 准备好了吗？

如果你:
- ✅ 有Python基础 (能写函数、能用pip安装包)
- ✅ 有命令行经验 (能cd、能运行脚本)
- ✅ 能阅读英文报错信息 (或会用翻译工具)
- ✅ 有8GB+内存的电脑
- ✅ 每天能投入1-3小时

那么**你已经准备好了**！ 🎉

---

## 📖 开始学习

**第一步**: 跟随[快速开始指南](../specs/002-ai-tutorial-stages/quickstart.md)完成环境配置 (30-60分钟)

**第二步**: 运行 `notebooks/stage3/00-quick-start.ipynb`，5分钟体验机器学习 🚀

**第三步**: 查看[学习路线图](learning-path.md)，规划你的学习路径

**遇到问题？** 查看[故障排查指南](cross-platform/troubleshooting.md)

---

## ❓ 常见问题

### Q1: 我没有数学背景，能学吗？

**A**: 可以！本教程强调**代码实现 + 直觉理解**，数学公式作为补充。高中数学 + 教程中的讲解足够应对阶段3和阶段4。

---

### Q2: 我没有GPU，能学吗？

**A**: 可以！
- **阶段3** (机器学习): CPU完全够用 (<5分钟/项目)
- **阶段4** (深度学习): 提供CPU版本配置 (<30分钟/项目)，或使用[云端GPU](cross-platform/troubleshooting.md#逃生舱云端gpu方案) (免费)
- **阶段5** (LLM): 使用API调用，无需本地GPU

---

### Q3: 我用Windows，会有问题吗？

**A**: 不会！教程覆盖Windows原生环境与WSL2 (推荐)。遇到问题查看[Windows故障排查](cross-platform/troubleshooting.md#7-编码与路径问题)。

---

### Q4: 完成全部教程需要多久？

**A**: 取决于你的节奏：
- **快速路径** (仅核心项目): 12-18小时 (1周，每天2-3小时)
- **标准路径** (推荐): 25-35小时 (2-3周，每天2-3小时)
- **深入路径** (所有项目 + 拓展): 50-80小时 (1-2个月)

详见[学习路线图](learning-path.md)。

---

### Q5: 我是数据分析师 / 算法工程师 / 学生，适合这个教程吗？

**A**:
- **数据分析师**: ✅ 适合！可快速过阶段3（可能已掌握），重点学阶段4/5
- **算法工程师**: ✅ 适合！可作为系统化复习，补充跨平台实战经验
- **学生**: ✅ 适合！但需确保有Python基础（建议先学1-2个月Python）

---

**准备好开始你的AI学习之旅了吗？** 🚀

→ [快速开始指南](../specs/002-ai-tutorial-stages/quickstart.md)
