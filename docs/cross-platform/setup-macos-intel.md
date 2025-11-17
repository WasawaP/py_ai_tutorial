# macOS (Intel) 环境配置指南

**适用系统**: macOS 10.15+ (Intel x86_64架构)
**难度**: ⭐⭐ 中等
**预计时间**: 30-45分钟

---

## 📋 系统要求

### 硬件要求
- **处理器**: Intel Core i5或更高
- **内存**: 至少8GB RAM（推荐16GB）
- **存储**: 至少20GB可用空间
- **网络**: 稳定的互联网连接

### 软件要求
- **操作系统**: macOS 10.15 Catalina或更高版本
- **命令行工具**: 已安装Xcode Command Line Tools

---

## 🚀 快速开始（推荐路径）

### Step 1: 安装Homebrew

Homebrew是macOS的包管理器，简化软件安装。

```bash
# 安装Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 验证安装
brew --version
```

**预期输出**:
```
Homebrew 4.x.x
```

**常见问题**:
- 如果安装失败，检查网络连接或尝试使用国内镜像
- 安装后需要重启终端使环境变量生效

---

### Step 2: 安装Python 3.11

使用Homebrew安装Python 3.11（推荐版本）。

```bash
# 安装Python 3.11
brew install python@3.11

# 验证安装
python3.11 --version

# 创建符号链接（可选，方便使用）
echo 'export PATH="/usr/local/opt/python@3.11/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**预期输出**:
```
Python 3.11.x
```

**备选方案**: 使用pyenv管理多版本Python
```bash
# 安装pyenv
brew install pyenv

# 安装Python 3.11
pyenv install 3.11.9

# 设置全局版本
pyenv global 3.11.9

# 添加到shell配置
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
source ~/.zshrc
```

---

### Step 3: 安装uv（现代Python包管理器）

uv是比pip更快的Python包管理器，本教程推荐使用。

```bash
# 安装uv
brew install uv

# 验证安装
uv --version
```

**预期输出**:
```
uv 0.x.x
```

**为什么使用uv？**
- 速度快：比pip快10-100倍
- 兼容性好：支持pip的所有功能
- 依赖解析准确：避免依赖冲突

---

### Step 4: 克隆教程仓库

```bash
# 克隆仓库
git clone https://github.com/yourusername/py_ai_tutorial.git
cd py_ai_tutorial

# 验证项目结构
ls -la
```

**预期输出**:
```
docs/
notebooks/
scripts/
data/
pyproject.toml
README.md
...
```

---

### Step 5: 创建虚拟环境

使用uv创建项目的虚拟环境。

```bash
# 创建虚拟环境（自动使用Python 3.11）
uv venv

# 激活虚拟环境
source .venv/bin/activate

# 验证Python版本
python --version
```

**预期输出**:
```
Python 3.11.x
```

**提示**:
- 激活后命令行前缀会显示`(.venv)`
- 每次打开新终端都需要重新激活
- 退出虚拟环境: `deactivate`

---

### Step 6: 安装依赖

使用uv安装项目依赖（比pip快很多）。

```bash
# 安装Stage 3依赖（传统机器学习）
uv pip install -e ".[stage3]"

# 验证安装
python -c "import numpy, pandas, matplotlib, sklearn; print('✅ Stage 3依赖安装成功！')"
```

**预期输出**:
```
✅ Stage 3依赖安装成功！
```

**可选**: 安装其他阶段依赖
```bash
# Stage 4: 深度学习（需要更多时间）
uv pip install -e ".[stage4]"

# Stage 5: LLM应用
uv pip install -e ".[stage5]"

# 或一次性安装所有
uv pip install -e ".[all]"
```

---

### Step 7: 安装Jupyter Notebook

用于运行教程的交互式notebook。

```bash
# 安装Jupyter
uv pip install jupyter jupyterlab

# 启动Jupyter Lab
jupyter lab

# 或启动经典Notebook
jupyter notebook
```

**预期行为**:
- 浏览器自动打开`http://localhost:8888`
- 可以浏览和运行notebooks/目录下的教程

**推荐**: 使用VS Code的Jupyter扩展
```bash
# 安装VS Code（如果还没有）
brew install --cask visual-studio-code

# 在VS Code中打开项目
code .
```

然后在VS Code中:
1. 安装Python扩展
2. 安装Jupyter扩展
3. 点击.ipynb文件直接运行

---

## 🔧 高级配置（可选）

### 配置中文字体（解决matplotlib中文显示问题）

```bash
# 安装中文字体
brew install font-noto-sans-cjk

# 配置matplotlib
mkdir -p ~/.matplotlib
cat > ~/.matplotlib/matplotlibrc << EOF
font.sans-serif: Noto Sans CJK SC, Arial Unicode MS, DejaVu Sans
axes.unicode_minus: False
EOF

# 验证
python -c "import matplotlib.pyplot as plt; plt.rcParams['font.sans-serif']; print('✅ 中文字体配置成功')"
```

---

### 配置Git（如果还没有）

```bash
# 设置用户信息
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 配置默认编辑器
git config --global core.editor "nano"  # 或 "vim" 或 "code --wait"

# 验证配置
git config --list
```

---

### 性能优化建议

**加速包下载（使用国内镜像）**:
```bash
# 配置pip镜像（如果不使用uv）
mkdir -p ~/.pip
cat > ~/.pip/pip.conf << EOF
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
EOF

# 配置uv镜像
export UV_INDEX_URL="https://pypi.tuna.tsinghua.edu.cn/simple"
echo 'export UV_INDEX_URL="https://pypi.tuna.tsinghua.edu.cn/simple"' >> ~/.zshrc
```

**增加Shell历史记录**:
```bash
# 增加命令历史
echo 'export HISTSIZE=10000' >> ~/.zshrc
echo 'export SAVEHIST=10000' >> ~/.zshrc
source ~/.zshrc
```

---

## ✅ 验证安装

运行完整的环境验证脚本：

```bash
# 进入项目目录
cd py_ai_tutorial

# 运行验证脚本
python scripts/env/detect-platform.py

# 运行快速测试
python -c "
import sys
import numpy as np
import pandas as pd
import matplotlib
import sklearn

print(f'✅ Python版本: {sys.version}')
print(f'✅ NumPy版本: {np.__version__}')
print(f'✅ Pandas版本: {pd.__version__}')
print(f'✅ Matplotlib版本: {matplotlib.__version__}')
print(f'✅ Scikit-learn版本: {sklearn.__version__}')
print('\\n🎉 环境配置成功！可以开始学习了！')
"
```

**预期输出**:
```
✅ Python版本: 3.11.x
✅ NumPy版本: 1.26.x
✅ Pandas版本: 2.x.x
✅ Matplotlib版本: 3.x.x
✅ Scikit-learn版本: 1.x.x

🎉 环境配置成功！可以开始学习了！
```

---

## 📝 开始学习

环境配置完成后，从这里开始：

1. **阅读先决条件**: [docs/prerequisites.md](../prerequisites.md)
2. **查看学习路径**: [docs/learning-path.md](../learning-path.md)
3. **运行快速入门**: [notebooks/stage3/00-quick-start.ipynb](../../notebooks/stage3/00-quick-start.ipynb)
4. **开始Module M01**: [docs/stage3/01-scientific-computing/README.md](../stage3/01-scientific-computing/README.md)

---

## 🐛 常见问题

### 问题1: Homebrew安装失败

**症状**: `curl: (7) Failed to connect`

**解决方案**:
```bash
# 使用国内镜像安装
/bin/bash -c "$(curl -fsSL https://gitee.com/ineo6/homebrew-install/raw/master/install.sh)"
```

---

### 问题2: Python版本不匹配

**症状**: `python --version`显示的不是3.11

**解决方案**:
```bash
# 检查所有Python版本
which -a python python3 python3.11

# 使用完整路径或创建别名
alias python=/usr/local/bin/python3.11
```

---

### 问题3: 虚拟环境激活失败

**症状**: 激活后仍使用系统Python

**解决方案**:
```bash
# 删除旧环境重新创建
rm -rf .venv
uv venv
source .venv/bin/activate

# 确认使用虚拟环境的Python
which python  # 应显示 .venv/bin/python
```

---

### 问题4: Jupyter Notebook无法启动

**症状**: `jupyter: command not found`

**解决方案**:
```bash
# 确保虚拟环境已激活
source .venv/bin/activate

# 重新安装Jupyter
uv pip install --force-reinstall jupyter

# 或使用完整路径
.venv/bin/jupyter lab
```

---

### 问题5: matplotlib中文显示为方框

**症状**: 图表中文字显示为 □□□

**解决方案**: 参考上面的"配置中文字体"部分，或在代码中临时设置：
```python
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Songti SC']
plt.rcParams['axes.unicode_minus'] = False
```

---

## 🆘 获取帮助

如果遇到本文档未涵盖的问题：

1. **查看故障排除指南**: [troubleshooting.md](./troubleshooting.md)
2. **搜索已知问题**: [GitHub Issues](https://github.com/yourusername/py_ai_tutorial/issues)
3. **提问**: 在Issues中创建新问题，附上错误信息和系统配置
4. **社区支持**: 加入学习社群讨论

---

## 📚 相关文档

- [macOS Apple Silicon配置](./setup-macos-arm64.md) - M1/M2/M3 Mac用户
- [Linux环境配置](./setup-linux.md)
- [Windows环境配置](./setup-windows-native.md)
- [故障排除指南](./troubleshooting.md)

---

**最后更新**: 2025-11-10
**维护者**: py_ai_tutorial团队
