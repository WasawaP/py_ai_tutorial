# Linux 环境配置指南

**适用系统**: Ubuntu 20.04+, Debian 11+, CentOS/RHEL 8+, Fedora 35+
**难度**: ⭐⭐ 中等
**预计时间**: 30-45分钟

---

## 📋 系统要求

### 硬件要求
- **处理器**: x86_64或ARM64架构
- **内存**: 至少4GB RAM（推荐8GB+）
- **存储**: 至少20GB可用空间

### 软件要求
- **操作系统**: Ubuntu 20.04+ / Debian 11+ / CentOS 8+ / Fedora 35+
- **权限**: sudo访问权限
- **网络**: 稳定的互联网连接

---

## 🚀 快速开始

### 判断你的Linux发行版

```bash
# 查看发行版信息
cat /etc/os-release

# 或使用
lsb_release -a
```

根据输出选择对应的安装方式（Ubuntu/Debian或CentOS/Fedora）。

---

## 方式A: Ubuntu/Debian系统

### Step 1: 更新系统

```bash
# 更新包列表
sudo apt update

# 升级已安装的包（可选）
sudo apt upgrade -y
```

---

### Step 2: 安装系统依赖

```bash
# 安装编译工具和开发库
sudo apt install -y \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    curl \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    python3-openssl \
    git
```

---

### Step 3: 安装Python 3.11

**方法1: 使用deadsnakes PPA（推荐）**

```bash
# 添加deadsnakes PPA
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update

# 安装Python 3.11
sudo apt install -y python3.11 python3.11-venv python3.11-dev

# 验证安装
python3.11 --version
```

**方法2: 从源码编译（适用于没有PPA的系统）**

```bash
# 下载Python 3.11源码
cd /tmp
wget https://www.python.org/ftp/python/3.11.9/Python-3.11.9.tgz
tar -xzf Python-3.11.9.tgz
cd Python-3.11.9

# 配置并编译
./configure --enable-optimizations --with-ensurepip=install
make -j $(nproc)
sudo make altinstall

# 验证
python3.11 --version
```

---

### Step 4: 安装uv

```bash
# 安装uv（使用官方安装脚本）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 配置PATH（添加到~/.bashrc或~/.zshrc）
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# 验证
uv --version
```

---

### Step 5-7: 克隆、配置、安装依赖

```bash
# 克隆仓库
git clone https://github.com/yourusername/py_ai_tutorial.git
cd py_ai_tutorial

# 创建虚拟环境
python3.11 -m venv .venv
# 或使用uv
uv venv

# 激活虚拟环境
source .venv/bin/activate

# 安装依赖
uv pip install -e ".[stage3]"

# 安装Jupyter
uv pip install jupyter jupyterlab

# 验证
python -c "import numpy, pandas, matplotlib, sklearn; print('✅ 安装成功！')"
```

---

## 方式B: CentOS/RHEL/Fedora系统

### Step 1: 更新系统

```bash
# CentOS/RHEL 8+
sudo dnf update -y

# 或 Fedora
sudo dnf update -y

# 或 CentOS 7（使用yum）
sudo yum update -y
```

---

### Step 2: 安装开发工具

```bash
# CentOS/RHEL 8+
sudo dnf groupinstall "Development Tools" -y
sudo dnf install -y \
    openssl-devel \
    bzip2-devel \
    libffi-devel \
    zlib-devel \
    wget \
    git

# CentOS 7
sudo yum groupinstall "Development Tools" -y
sudo yum install -y \
    openssl-devel \
    bzip2-devel \
    libffi-devel \
    zlib-devel \
    wget \
    git
```

---

### Step 3: 安装Python 3.11

CentOS/RHEL通常需要从源码编译Python 3.11：

```bash
# 下载并编译Python 3.11
cd /tmp
wget https://www.python.org/ftp/python/3.11.9/Python-3.11.9.tgz
tar -xzf Python-3.11.9.tgz
cd Python-3.11.9

./configure --enable-optimizations --with-ensurepip=install
make -j $(nproc)
sudo make altinstall

# 验证
python3.11 --version
```

---

### Step 4-7: 同Ubuntu

安装uv、克隆仓库、创建环境、安装依赖的步骤与Ubuntu相同。

---

## 🔧 高级配置

### 配置中文字体

```bash
# Ubuntu/Debian
sudo apt install -y fonts-noto-cjk

# CentOS/RHEL
sudo yum install -y google-noto-sans-cjk-fonts

# 配置matplotlib
mkdir -p ~/.config/matplotlib
cat > ~/.config/matplotlib/matplotlibrc << EOF
font.sans-serif: Noto Sans CJK SC, DejaVu Sans
axes.unicode_minus: False
EOF
```

---

### 配置SSH（远程访问）

如果需要远程访问Jupyter：

```bash
# 生成Jupyter配置
jupyter notebook --generate-config

# 设置密码
jupyter notebook password

# 配置允许远程访问
cat >> ~/.jupyter/jupyter_notebook_config.py << EOF
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False
EOF

# 启动（后台运行）
nohup jupyter lab > jupyter.log 2>&1 &

# 访问：http://<服务器IP>:8888
```

**安全建议**:
- 使用强密码
- 配置防火墙只允许特定IP访问
- 或使用SSH隧道: `ssh -L 8888:localhost:8888 user@server`

---

### 使用tmux保持会话

```bash
# 安装tmux
sudo apt install -y tmux  # Ubuntu/Debian
sudo yum install -y tmux  # CentOS/RHEL

# 创建会话
tmux new -s ai-tutorial

# 在tmux中激活环境并运行Jupyter
source .venv/bin/activate
jupyter lab

# 分离会话: Ctrl+B, 然后按D
# 重新连接: tmux attach -t ai-tutorial
```

---

## ✅ 验证安装

```bash
# 运行验证脚本
python scripts/env/detect-platform.py

# 快速测试
python -c "
import sys
import platform
import numpy as np
import pandas as pd
import matplotlib
import sklearn

print(f'✅ Python版本: {sys.version}')
print(f'✅ 系统: {platform.system()} {platform.release()}')
print(f'✅ 架构: {platform.machine()}')
print(f'✅ NumPy版本: {np.__version__}')
print(f'✅ Pandas版本: {pd.__version__}')
print(f'✅ Matplotlib版本: {matplotlib.__version__}')
print(f'✅ Scikit-learn版本: {sklearn.__version__}')
print('\\n🎉 Linux环境配置成功！')
"
```

---

## 🐛 常见问题

### 问题1: add-apt-repository命令不存在

**症状**: `sudo: add-apt-repository: command not found`

**解决方案**:
```bash
sudo apt install -y software-properties-common
```

---

### 问题2: Python编译失败

**症状**: `configure: error: no acceptable C compiler found`

**解决方案**:
```bash
# 安装GCC编译器
sudo apt install -y gcc g++  # Ubuntu/Debian
sudo yum install -y gcc gcc-c++  # CentOS/RHEL
```

---

### 问题3: SSL证书错误

**症状**: `urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED]>`

**解决方案**:
```bash
# Ubuntu/Debian
sudo apt install -y ca-certificates
sudo update-ca-certificates

# CentOS/RHEL
sudo yum install -y ca-certificates
sudo update-ca-trust
```

---

### 问题4: 内存不足

**症状**: `MemoryError` 或系统卡死

**解决方案**:
```bash
# 创建swap空间（4GB）
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# 永久生效
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

# 验证
free -h
```

---

### 问题5: Jupyter无法访问（远程）

**症状**: 无法连接到`http://<服务器IP>:8888`

**解决方案**:
```bash
# 检查防火墙
sudo ufw status  # Ubuntu/Debian
sudo firewall-cmd --list-all  # CentOS/RHEL

# 开放8888端口
sudo ufw allow 8888  # Ubuntu/Debian
sudo firewall-cmd --permanent --add-port=8888/tcp  # CentOS/RHEL
sudo firewall-cmd --reload

# 检查Jupyter是否运行
ps aux | grep jupyter
netstat -tlnp | grep 8888
```

---

## 🚀 性能优化

### 使用国内镜像加速

```bash
# pip镜像
mkdir -p ~/.pip
cat > ~/.pip/pip.conf << EOF
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
EOF

# apt镜像（Ubuntu，替换为阿里云）
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
sudo sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list
sudo apt update
```

---

## 📝 开始学习

环境配置完成后：

1. [docs/prerequisites.md](../prerequisites.md)
2. [docs/learning-path.md](../learning-path.md)
3. [notebooks/stage3/00-quick-start.ipynb](../../notebooks/stage3/00-quick-start.ipynb)

---

## 📚 相关文档

- [macOS配置](./setup-macos-intel.md)
- [Windows配置](./setup-windows-native.md)
- [WSL2配置](./setup-windows-wsl2.md)
- [云端GPU配置](./setup-cloud-gpu.md)
- [故障排除](./troubleshooting.md)

---

**最后更新**: 2025-11-10
**维护者**: py_ai_tutorial团队
