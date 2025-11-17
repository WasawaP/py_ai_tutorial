# Windows WSL2 环境配置指南

**适用系统**: Windows 10 (21H2+) / Windows 11
**难度**: ⭐⭐ 中等
**预计时间**: 40-50分钟

**强烈推荐**: 如果你是Windows用户且熟悉Linux,WSL2是最佳选择!体验接近原生Linux,兼容性好。

---

## 📋 系统要求

### 硬件要求
- **处理器**: Intel/AMD x86_64, 支持虚拟化技术
- **内存**: 至少8GB RAM(推荐16GB)
- **存储**: 至少30GB可用空间

### 软件要求
- **操作系统**: Windows 10 版本21H2+ 或 Windows 11
- **PowerShell**: 5.1或更高(系统自带)
- **Windows Terminal**: 推荐安装(可选但体验更好)

---

## 🚀 快速开始

### Step 1: 启用WSL2

**方法1: 一键安装(Windows 10 19041+/Windows 11)**

```powershell
# 以管理员身份运行PowerShell
wsl --install

# 重启计算机
# 重启后会自动安装Ubuntu
```

**方法2: 手动启用(适用于旧版本)**

```powershell
# 以管理员身份运行PowerShell

# 启用WSL功能
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

# 启用虚拟机平台
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# 重启计算机
Restart-Computer

# 下载并安装WSL2 Linux内核更新包
# https://aka.ms/wsl2kernel

# 设置WSL2为默认版本
wsl --set-default-version 2
```

---

### Step 2: 安装Ubuntu发行版

```powershell
# 查看可用发行版
wsl --list --online

# 安装Ubuntu 22.04(推荐)
wsl --install -d Ubuntu-22.04

# 或安装Ubuntu 20.04
wsl --install -d Ubuntu-20.04
```

**首次启动配置**:
1. 设置用户名(建议小写,无空格)
2. 设置密码(输入时不显示,正常)
3. 记住密码(用于sudo命令)

**验证安装**:
```powershell
# 查看已安装的发行版
wsl --list --verbose

# 应显示类似:
#   NAME            STATE           VERSION
# * Ubuntu-22.04    Running         2
```

---

### Step 3: 进入WSL2环境

```powershell
# 方法1: 启动默认发行版
wsl

# 方法2: 启动特定发行版
wsl -d Ubuntu-22.04

# 方法3: 使用Windows Terminal(推荐)
# 打开Windows Terminal → 选择Ubuntu标签
```

---

### Step 4: 更新Ubuntu系统

```bash
# 在WSL2 Ubuntu中运行

# 更新包列表
sudo apt update

# 升级已安装的包
sudo apt upgrade -y

# 安装常用工具
sudo apt install -y build-essential wget curl git vim
```

---

### Step 5: 安装Python 3.11

```bash
# 添加deadsnakes PPA
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update

# 安装Python 3.11
sudo apt install -y python3.11 python3.11-venv python3.11-dev

# 验证
python3.11 --version
```

---

### Step 6: 安装uv

```bash
# 安装uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 配置PATH
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# 验证
uv --version
```

---

### Step 7: 克隆仓库并配置环境

```bash
# 克隆仓库(推荐克隆到WSL文件系统,性能更好)
cd ~
git clone https://github.com/yourusername/py_ai_tutorial.git
cd py_ai_tutorial

# 创建虚拟环境
uv venv

# 激活虚拟环境
source .venv/bin/activate

# 安装依赖
uv pip install -e ".[stage3]"

# 安装Jupyter
uv pip install jupyter jupyterlab

# 验证
python -c "import numpy, pandas, matplotlib, sklearn; print('✅ 安装成功!')"
```

---

## 🔧 高级配置

### 访问Windows文件系统

WSL2可以访问Windows文件,但性能较差(跨文件系统)。

```bash
# Windows C:\ 盘在WSL2中的路径
cd /mnt/c/

# 访问用户文档
cd /mnt/c/Users/YourUsername/Documents

# 查看当前Windows路径
explorer.exe .
```

**⚠️ 重要提示**:
- **推荐**: 将项目放在WSL文件系统(如`~/py_ai_tutorial`),性能更好
- **避免**: 跨文件系统频繁读写(如`/mnt/c/`下运行Python),会很慢

---

### 配置VS Code与WSL2集成

VS Code是使用WSL2的最佳方式!

**安装步骤**:

1. 在Windows上安装VS Code: https://code.visualstudio.com/
2. 安装"Remote - WSL"扩展
3. 在WSL2中打开项目:

```bash
# 在WSL2的项目目录中
cd ~/py_ai_tutorial
code .
```

**首次使用**:
- VS Code会自动在WSL2中安装服务端
- 窗口左下角显示"WSL: Ubuntu-22.04"表示已连接
- 所有操作都在WSL2中执行(终端、文件、扩展)

**推荐扩展**:
- Python
- Jupyter
- Pylance
- GitLens

---

### 配置Jupyter访问

**方法1: 在WSL2中启动,Windows浏览器访问**

```bash
# 在WSL2中启动Jupyter
jupyter lab

# 复制输出的URL(形如 http://localhost:8888/lab?token=...)
# 在Windows浏览器中打开即可
```

**方法2: 使用VS Code的Jupyter扩展(推荐)**

1. 在VS Code中通过Remote-WSL打开项目
2. 打开`.ipynb`文件
3. 选择WSL中的Python内核
4. 直接在VS Code中运行

---

### 配置中文字体

```bash
# 安装中文字体
sudo apt install -y fonts-noto-cjk

# 配置matplotlib
mkdir -p ~/.config/matplotlib
cat > ~/.config/matplotlib/matplotlibrc << EOF
font.sans-serif: Noto Sans CJK SC, DejaVu Sans
axes.unicode_minus: False
EOF
```

---

### WSL2性能优化

**创建`.wslconfig`文件(限制资源使用)**:

在Windows用户目录创建 `.wslconfig` 文件(路径: `C:\Users\YourUsername\.wslconfig`):

```ini
[wsl2]
memory=8GB          # 限制最大内存
processors=4        # 限制CPU核心数
swap=4GB            # swap大小
localhostForwarding=true  # 允许Windows访问WSL服务
```

**重启WSL2使配置生效**:
```powershell
# 在PowerShell中
wsl --shutdown
wsl
```

---

### GPU支持(NVIDIA CUDA)

如果你有NVIDIA显卡,可以在WSL2中使用GPU加速!

**前提条件**:
- NVIDIA显卡(GTX 10系列及以上)
- 安装最新的NVIDIA驱动(Windows端)
- Windows 11 或 Windows 10 (21H2+)

**安装CUDA(在WSL2中)**:

```bash
# 安装CUDA Toolkit
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt update
sudo apt install -y cuda-toolkit-12-3

# 配置环境变量
echo 'export PATH=/usr/local/cuda/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc

# 验证
nvidia-smi  # 应显示GPU信息
```

**安装PyTorch with CUDA**:
```bash
# 激活虚拟环境
source .venv/bin/activate

# 安装PyTorch(CUDA 12.1)
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# 验证GPU可用
python -c "import torch; print('CUDA可用:', torch.cuda.is_available()); print('GPU数量:', torch.cuda.device_count())"
```

---

## ✅ 验证安装

```bash
# 完整验证脚本
python -c "
import sys
import platform
import numpy as np
import pandas as pd
import matplotlib
import sklearn

print(f'✅ Python版本: {sys.version}')
print(f'✅ 系统: {platform.system()} (WSL2)')
print(f'✅ 架构: {platform.machine()}')
print(f'✅ NumPy版本: {np.__version__}')
print(f'✅ Pandas版本: {pd.__version__}')
print(f'✅ Matplotlib版本: {matplotlib.__version__}')
print(f'✅ Scikit-learn版本: {sklearn.__version__}')
print('\n🎉 WSL2环境配置成功!')
"
```

---

## 🐛 常见问题

### 问题1: WSL安装失败

**症状**: `Error: 0x80370102`

**解决方案**:
```powershell
# 确保启用了虚拟化
# 在BIOS中启用Intel VT-x 或 AMD-V

# 确保启用了Hyper-V(Windows 11/Pro)
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
```

---

### 问题2: WSL2网络问题

**症状**: 无法访问互联网

**解决方案**:
```bash
# 在WSL2中
# 方法1: 重启WSL
wsl --shutdown
wsl

# 方法2: 配置DNS
sudo bash -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'
```

---

### 问题3: 文件权限问题

**症状**: Windows创建的文件在WSL2中权限为777

**解决方案**:
```bash
# 配置 /etc/wsl.conf
sudo bash -c 'cat > /etc/wsl.conf << EOF
[automount]
options = "metadata,umask=22,fmask=11"
EOF'

# 重启WSL
wsl --shutdown
wsl
```

---

### 问题4: VS Code连接WSL失败

**症状**: "Failed to connect to WSL"

**解决方案**:
```powershell
# 方法1: 重启WSL
wsl --shutdown
wsl

# 方法2: 重新安装VS Code Server
# 在WSL2中删除
rm -rf ~/.vscode-server

# 重新用VS Code打开,会自动安装
```

---

### 问题5: Jupyter内核死亡

**症状**: Kernel dies immediately

**解决方案**:
```bash
# 重新注册内核
python -m ipykernel install --user --name=py311 --display-name="Python 3.11"

# 重启Jupyter
```

---

## 🚀 性能优化建议

1. **项目放在WSL文件系统**: 使用`~/py_ai_tutorial`而不是`/mnt/c/...`
2. **限制WSL2内存**: 配置`.wslconfig`避免占用过多内存
3. **使用Windows Terminal**: 比CMD/PowerShell体验更好
4. **启用GPU**: 如有NVIDIA显卡,配置CUDA加速
5. **定期清理**: `docker system prune`(如使用Docker)

---

## 📊 WSL2 vs 原生Windows对比

| 特性 | WSL2 | Windows原生 |
|------|------|-------------|
| 安装难度 | ⭐⭐ 中等 | ⭐⭐⭐ 较难 |
| 性能 | 接近原生Linux | Windows原生 |
| 兼容性 | 完美兼容Linux包 | 可能有编译问题 |
| GPU支持 | ✅ 支持CUDA | ✅ 支持 |
| 文件访问 | 双向访问 | 仅Windows |
| 工具链 | Linux生态 | Windows生态 |
| 推荐度 | ⭐⭐⭐⭐⭐ 强烈推荐 | ⭐⭐⭐ 可选 |

**结论**: WSL2是Windows用户学习AI的最佳选择!

---

## 📝 常用命令速查

```bash
# WSL管理(PowerShell)
wsl --list --verbose        # 查看所有发行版
wsl --shutdown              # 关闭所有WSL实例
wsl --terminate Ubuntu-22.04  # 终止特定发行版
wsl --unregister Ubuntu-22.04  # 删除发行版

# 文件访问
cd /mnt/c/Users/YourName    # Windows用户目录
explorer.exe .              # 在Windows文件管理器中打开

# 虚拟环境
source .venv/bin/activate   # 激活
deactivate                  # 退出

# Jupyter
jupyter lab                 # 启动Jupyter Lab
jupyter notebook list       # 查看运行中的服务
```

---

## 📝 开始学习

环境配置完成后:

1. [docs/prerequisites.md](../prerequisites.md)
2. [docs/learning-path.md](../learning-path.md)
3. [notebooks/stage3/00-quick-start.ipynb](../../notebooks/stage3/00-quick-start.ipynb)

---

## 📚 相关文档

- [Windows原生配置](./setup-windows-native.md) - 不使用WSL的方案
- [Linux配置](./setup-linux.md) - 原生Linux
- [macOS配置](./setup-macos-intel.md)
- [故障排除](./troubleshooting.md)

---

**最后更新**: 2025-11-10
**维护者**: py_ai_tutorial团队
