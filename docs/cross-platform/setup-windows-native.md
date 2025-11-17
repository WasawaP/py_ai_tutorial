# Windows (原生) 环境配置指南

**适用系统**: Windows 10 (21H2+) / Windows 11
**难度**: ⭐⭐⭐ 中等-困难
**预计时间**: 45-60分钟

**推荐**: 如果你熟悉Linux，强烈推荐使用[WSL2配置](./setup-windows-wsl2.md)，体验更好！

---

## 📋 系统要求

### 硬件要求
- **处理器**: Intel/AMD x86_64, 2核心或更高
- **内存**: 至少8GB RAM
- **存储**: 至少20GB可用空间

### 软件要求
- **操作系统**: Windows 10 (版本21H2+) 或 Windows 11
- **PowerShell**: 5.1或更高（系统自带）

---

## 🚀 快速开始

### Step 1: 安装Python 3.11

#### 方法1: 使用官方安装程序（推荐新手）

1. 访问Python官网: https://www.python.org/downloads/
2. 下载Python 3.11.x Windows installer (64-bit)
3. 运行安装程序：
   - ✅ **勾选** "Add Python 3.11 to PATH"（重要！）
   - 选择"Customize installation"
   - ✅ 勾选所有Optional Features
   - ✅ 勾选"Install for all users"
   - 安装路径建议: `C:\Python311`
4. 点击"Install"完成安装

**验证安装**:
```powershell
# 打开PowerShell或CMD
python --version
pip --version
```

**预期输出**:
```
Python 3.11.x
pip 24.x from ...
```

#### 方法2: 使用Chocolatey包管理器（推荐进阶用户）

```powershell
# 以管理员身份运行PowerShell

# 安装Chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# 安装Python 3.11
choco install python311 -y

# 刷新环境变量
refreshenv

# 验证
python --version
```

---

### Step 2: 安装Git

```powershell
# 使用Chocolatey安装
choco install git -y

# 或下载安装程序
# https://git-scm.com/download/win
```

**配置Git**:
```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

### Step 3: 安装uv

```powershell
# 使用pip安装uv
pip install uv

# 验证
uv --version
```

**备选**: 使用Windows安装脚本
```powershell
# PowerShell
irm https://astral.sh/uv/install.ps1 | iex
```

---

### Step 4: 克隆仓库

```powershell
# 克隆到合适的位置（避免路径中有中文或空格）
cd C:\
git clone https://github.com/yourusername/py_ai_tutorial.git
cd py_ai_tutorial
```

**⚠️ Windows路径注意事项**:
- 避免中文路径：`C:\用户\文档` → 可能有问题
- 避免空格路径：`C:\My Documents` → 可能有问题
- 推荐路径：`C:\Projects`, `D:\Code`, `C:\py_ai_tutorial`

---

### Step 5: 创建虚拟环境

```powershell
# 方法1: 使用Python内置venv
python -m venv .venv

# 激活虚拟环境
.\.venv\Scripts\Activate.ps1

# 方法2: 使用uv（更快）
uv venv
.\.venv\Scripts\Activate.ps1
```

**如果遇到执行策略错误**:
```powershell
# 临时允许脚本执行
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 然后重新激活
.\.venv\Scripts\Activate.ps1
```

**激活成功标志**: 命令行前缀显示`(.venv)`

---

### Step 6: 安装依赖

```powershell
# 确保虚拟环境已激活
# 安装Stage 3依赖
uv pip install -e ".[stage3]"

# 或使用pip
pip install -e ".[stage3]"

# 验证安装
python -c "import numpy, pandas, matplotlib, sklearn; print('✅ Stage 3依赖安装成功！')"
```

**注意**: Windows上安装某些包（如scipy）可能需要C++编译器，如果失败：
```powershell
# 安装预编译的wheel包
pip install --only-binary :all: numpy scipy scikit-learn
```

---

### Step 7: 安装Jupyter

```powershell
# 安装Jupyter
uv pip install jupyter jupyterlab

# 启动Jupyter Lab
jupyter lab

# 或启动经典Notebook
jupyter notebook
```

**推荐**: 使用VS Code的Jupyter扩展：
1. 下载安装VS Code: https://code.visualstudio.com/
2. 安装Python扩展
3. 安装Jupyter扩展
4. 打开`.ipynb`文件直接运行

---

## 🔧 高级配置

### 配置中文字体

Windows上matplotlib中文显示相对简单：

```python
# 在代码中配置
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'SimSun']
plt.rcParams['axes.unicode_minus'] = False
```

或创建配置文件：
```powershell
# 找到matplotlib配置目录
python -c "import matplotlib; print(matplotlib.get_configdir())"

# 手动创建 matplotlibrc 文件，添加：
# font.sans-serif: SimHei, Microsoft YaHei, SimSun
# axes.unicode_minus: False
```

---

### 配置国内镜像（加速下载）

```powershell
# 创建pip配置文件
mkdir ~\pip
New-Item -Path ~\pip\pip.ini -ItemType File -Force

# 添加内容
@"
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
"@ | Set-Content ~\pip\pip.ini
```

---

### 安装Visual C++ Build Tools（可选）

某些包需要编译，可能需要：

1. 下载：https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. 安装时选择"Desktop development with C++"
3. 重启计算机

---

## ✅ 验证安装

```powershell
# 运行验证脚本
python scripts\env\detect-platform.py

# 快速测试
python -c "import sys; import numpy as np; import pandas as pd; import matplotlib; import sklearn; print(f'✅ Python: {sys.version}'); print(f'✅ NumPy: {np.__version__}'); print(f'✅ Pandas: {pd.__version__}'); print(f'✅ Matplotlib: {matplotlib.__version__}'); print(f'✅ Scikit-learn: {sklearn.__version__}'); print('\n🎉 Windows环境配置成功！')"
```

---

## 🐛 常见问题

### 问题1: Python未添加到PATH

**症状**: `python: command not found`

**解决方案**:
1. 重新运行Python安装程序
2. 选择"Modify"
3. 勾选"Add Python to environment variables"
4. 或手动添加到PATH:
   - 搜索"环境变量" → 编辑系统环境变量
   - Path → 添加`C:\Python311`和`C:\Python311\Scripts`

---

### 问题2: PowerShell无法运行脚本

**症状**: `无法加载文件，因为在此系统上禁止运行脚本`

**解决方案**:
```powershell
# 以管理员运行PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine

# 或仅当前用户
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

### 问题3: pip安装慢或超时

**症状**: 下载速度慢，连接超时

**解决方案**:
```powershell
# 临时使用镜像
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple <package-name>

# 或永久配置（见上面"配置国内镜像"）
```

---

### 问题4: numpy/scipy安装失败

**症状**: `error: Microsoft Visual C++ 14.0 is required`

**解决方案**:
```powershell
# 方法1: 使用预编译wheel
pip install --only-binary :all: numpy scipy

# 方法2: 安装Visual C++ Build Tools（见上面）

# 方法3: 使用conda（备选方案）
# 下载Miniconda: https://docs.conda.io/en/latest/miniconda.html
conda install numpy scipy scikit-learn
```

---

### 问题5: Jupyter Notebook中文路径问题

**症状**: 无法打开中文路径下的文件

**解决方案**:
1. 将项目移到纯英文路径
2. 或在启动Jupyter时指定目录：
```powershell
jupyter lab --notebook-dir=C:\py_ai_tutorial
```

---

## 🔄 Windows vs WSL2

| 特性 | Windows原生 | WSL2 |
|------|-------------|------|
| 安装难度 | 中等 | 简单 |
| 性能 | 原生性能 | 接近原生（略慢5-10%） |
| 兼容性 | 可能遇到编译问题 | 完美兼容Linux包 |
| 文件系统 | NTFS（大小写不敏感） | ext4（大小写敏感） |
| GUI应用 | 原生支持 | 需要配置X Server |
| 适合人群 | Windows深度用户 | 熟悉Linux用户 |

**建议**: 如果你熟悉Linux或遇到兼容性问题，尝试[WSL2配置](./setup-windows-wsl2.md)！

---

## 📝 开始学习

环境配置完成后：

1. [docs/prerequisites.md](../prerequisites.md)
2. [docs/learning-path.md](../learning-path.md)
3. [notebooks/stage3/00-quick-start.ipynb](../../notebooks/stage3/00-quick-start.ipynb)

---

## 📚 相关文档

- [WSL2配置](./setup-windows-wsl2.md) - 推荐Windows用户使用
- [macOS配置](./setup-macos-intel.md)
- [Linux配置](./setup-linux.md)
- [故障排除](./troubleshooting.md)

---

**最后更新**: 2025-11-10
**维护者**: py_ai_tutorial团队
