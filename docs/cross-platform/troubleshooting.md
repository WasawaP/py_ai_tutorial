# 故障排查指南 (Troubleshooting Guide)

**目标**: 快速自助解决常见环境配置和运行问题，平均停滞时间 ≤ 30分钟

**使用方法**: 按症状查找对应的解决方案。如果30分钟内未解决，考虑切换到[云端GPU方案](#逃生舱云端gpu方案)。

---

## 📋 目录

1. [Python环境问题](#1-python环境问题)
2. [包管理与依赖问题](#2-包管理与依赖问题)
3. [数据下载与验证问题](#3-数据下载与验证问题)
4. [Jupyter Notebook问题](#4-jupyter-notebook问题)
5. [GPU相关问题](#5-gpu相关问题)
6. [性能问题](#6-性能问题)
7. [编码与路径问题](#7-编码与路径问题)
8. [权限问题](#8-权限问题)
9. [内存不足问题](#9-内存不足问题)
10. [逃生舱：云端GPU方案](#逃生舱云端gpu方案)

---

## 1. Python环境问题

### ❌ 症状: `python`命令无法识别 (command not found)

**原因**: Python未安装或未添加到PATH

**解决方案**:

```bash
# macOS/Linux: 检查Python是否已安装
which python3
python3 --version

# 若未安装，按平台安装:
# macOS: brew install python@3.11
# Ubuntu: sudo apt install python3.11
# Windows: 从 python.org 下载安装包，勾选 "Add Python to PATH"

# Windows PowerShell: 检查Python
where.exe python
python --version
```

---

### ❌ 症状: 虚拟环境激活后，仍使用系统Python

**原因**: 虚拟环境未正确激活

**解决方案**:

```bash
# 验证虚拟环境是否激活
which python  # 应输出 .venv/bin/python，而非 /usr/bin/python

# 若未激活，重新激活:
# macOS/Linux:
source .venv/bin/activate

# Windows PowerShell:
.venv\Scripts\Activate.ps1

# Windows CMD:
.venv\Scripts\activate.bat

# 验证成功后，提示符前应显示 (.venv)
```

---

### ❌ 症状: Python版本不符合要求 (需要 ≥3.9)

**原因**: 系统Python版本过旧

**解决方案**:

```bash
# 检查当前版本
python3 --version

# 若版本<3.9，安装Python 3.11:
# macOS:
brew install python@3.11
python3.11 --version

# Ubuntu:
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11 python3.11-venv

# 重新创建虚拟环境
uv venv --python 3.11
source .venv/bin/activate
```

---

## 2. 包管理与依赖问题

### ❌ 症状: `uv`命令无法识别 (command not found)

**原因**: uv未安装或未添加到PATH

**解决方案**:

```bash
# 方案1: 使用官方安装脚本
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env
uv --version

# 方案2: 使用pipx安装
python3 -m pip install --user pipx
pipx install uv

# 方案3: 直接使用pip (备选)
python3 -m pip install uv

# 验证安装
uv --version
# 输出: uv 0.x.x
```

---

### ❌ 症状: 安装依赖时超时或失败

**原因**: 网络问题或PyPI镜像源不可达

**解决方案**:

```bash
# 使用国内PyPI镜像源
uv pip install -e . -i https://pypi.tuna.tsinghua.edu.cn/simple

# 或配置为默认镜像源 (创建 ~/.config/pip/pip.conf):
mkdir -p ~/.config/pip
cat > ~/.config/pip/pip.conf << EOF
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
EOF

# Windows: 创建 %APPDATA%\pip\pip.ini
```

**其他可用镜像**:
- 清华: `https://pypi.tuna.tsinghua.edu.cn/simple`
- 阿里云: `https://mirrors.aliyun.com/pypi/simple/`
- 中科大: `https://pypi.mirrors.ustc.edu.cn/simple/`

---

### ❌ 症状: 依赖冲突 (conflict resolution failed)

**原因**: 包版本不兼容

**解决方案**:

```bash
# 查看冲突详情
uv pip install -e . --resolution=lowest-direct

# 清理缓存并重新安装
uv cache clean
rm -rf .venv
uv venv --python 3.11
source .venv/bin/activate
uv pip install -e ".[stage3]"

# 若仍失败，尝试分步安装
uv pip install numpy pandas matplotlib
uv pip install scikit-learn
uv pip install -e .
```

---

### ❌ 症状: `ModuleNotFoundError: No module named 'xxx'`

**原因**: 模块未安装或虚拟环境未激活

**解决方案**:

```bash
# 1. 确认虚拟环境已激活
which python  # 应输出 .venv/bin/python

# 2. 检查包是否已安装
pip list | grep xxx

# 3. 重新安装项目依赖
uv pip install -e ".[stage3]"

# 4. 验证模块可导入
python -c "import xxx; print(xxx.__version__)"
```

---

## 3. 数据下载与验证问题

### ❌ 症状: 数据下载失败 (HTTP 404 / Timeout)

**原因**: 网络问题或数据源不可达

**解决方案**:

```bash
# 方案1: 使用代理 (若在公司内网)
export HTTP_PROXY=http://proxy.company.com:8080
export HTTPS_PROXY=http://proxy.company.com:8080
python scripts/data/download-stage3.py

# 方案2: 下载离线数据包
# 从百度网盘/阿里云盘下载 stage3-data.tar.gz
# 解压到 data/ 目录
tar -xzf stage3-data.tar.gz -C data/

# 方案3: 手动下载
# 查看 configs/content/datasets.yaml 中的下载链接
# 手动下载后放到 data/stage3/ 目录

# 验证数据完整性
python scripts/data/verify.py --stage 3
```

---

### ❌ 症状: 数据校验失败 (SHA256 mismatch)

**原因**: 数据文件损坏或下载不完整

**解决方案**:

```bash
# 删除损坏的数据文件
rm data/stage3/healthcare_sales.csv

# 重新下载
python scripts/data/download-stage3.py --project p01-healthcare

# 验证校验和
python scripts/data/verify.py --stage 3 --verbose
```

---

## 4. Jupyter Notebook问题

### ❌ 症状: `jupyter lab`命令无法识别

**原因**: JupyterLab未安装

**解决方案**:

```bash
# 安装JupyterLab
uv pip install jupyterlab

# 启动Jupyter Lab
jupyter lab

# 若端口被占用，指定其他端口
jupyter lab --port=8889
```

---

### ❌ 症状: Jupyter Notebook内核崩溃 (Kernel died)

**原因**: 内存不足或代码错误

**解决方案**:

```bash
# 1. 重启内核: Kernel -> Restart Kernel

# 2. 检查内存使用
# macOS/Linux:
free -h  # 或 top

# Windows:
# 任务管理器 -> 性能 -> 内存

# 3. 若内存不足，减小数据集大小或batch size

# 4. 查看内核日志
jupyter lab --debug
```

---

### ❌ 症状: Notebook中导入模块失败，但命令行可以

**原因**: Jupyter使用了错误的Python内核

**解决方案**:

```bash
# 1. 确保在虚拟环境中安装了ipykernel
source .venv/bin/activate
uv pip install ipykernel

# 2. 注册虚拟环境为Jupyter内核
python -m ipykernel install --user --name=py_ai_tutorial --display-name="Python (py_ai_tutorial)"

# 3. 在Jupyter中切换内核:
# Kernel -> Change Kernel -> Python (py_ai_tutorial)

# 4. 验证内核路径
import sys
print(sys.executable)
# 应输出: /path/to/.venv/bin/python
```

---

## 5. GPU相关问题

### ❌ 症状: `torch.cuda.is_available()` 返回 `False`

**原因**: CUDA未安装或PyTorch版本不匹配

**解决方案**:

```bash
# 1. 检查NVIDIA驱动和CUDA版本
nvidia-smi
# 查看右上角的 CUDA Version (如 12.1)

# 2. 安装对应版本的PyTorch
# CUDA 11.8:
uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

# CUDA 12.1:
uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121

# 3. 验证CUDA可用
python -c "import torch; print(torch.cuda.is_available()); print(torch.version.cuda)"
# 输出: True, 11.8 (或 12.1)
```

---

### ❌ 症状: Apple Silicon上 `torch.backends.mps.is_available()` 返回 `False`

**原因**: PyTorch版本过旧或MPS后端不支持

**解决方案**:

```bash
# 安装最新版PyTorch (≥2.0)
uv pip install --upgrade torch torchvision

# 验证MPS可用
python -c "import torch; print(torch.backends.mps.is_available())"
# 输出: True

# 若仍不可用，检查macOS版本 (需要 ≥12.3)
sw_vers
```

---

### ❌ 症状: 训练时报错 `CUDA out of memory`

**原因**: GPU显存不足

**解决方案**:

```python
# 方案1: 减小batch size
# 将 batch_size=64 改为 batch_size=16 或 batch_size=8

# 方案2: 使用梯度累积
# 将 batch_size=64 拆分为 4次 batch_size=16 + 梯度累积

# 方案3: 清理GPU缓存
import torch
torch.cuda.empty_cache()

# 方案4: 使用混合精度训练
from torch.cuda.amp import autocast, GradScaler
scaler = GradScaler()

# 方案5: 降级到CPU (慢但稳定)
device = 'cpu'
```

---

## 6. 性能问题

### ❌ 症状: 训练速度非常慢 (CPU版本 >30分钟/epoch)

**原因**: 未使用GPU加速或数据加载效率低

**解决方案**:

```python
# 1. 确认是否使用GPU
import torch
print(f"Using device: {torch.cuda.current_device() if torch.cuda.is_available() else 'cpu'}")

# 2. 优化DataLoader
from torch.utils.data import DataLoader
train_loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True,
    num_workers=4,  # 增加数据加载线程
    pin_memory=True  # 加速数据传输到GPU
)

# 3. 使用编译优化 (PyTorch 2.0+)
model = torch.compile(model)

# 4. 若无GPU，减小数据集 (快速验证)
# 使用前10%数据快速迭代
train_data = train_data[:len(train_data)//10]
```

---

### ❌ 症状: Pandas操作很慢 (大数据集 >1GB)

**原因**: 数据未优化或内存不足

**解决方案**:

```python
# 1. 使用Parquet格式 (比CSV快5-10倍)
import pandas as pd

# 转换CSV为Parquet
df = pd.read_csv('data.csv')
df.to_parquet('data.parquet', compression='snappy')

# 后续使用Parquet
df = pd.read_parquet('data.parquet')

# 2. 优化数据类型
# 将int64降级为int32，float64降级为float32
df['age'] = df['age'].astype('int32')
df['price'] = df['price'].astype('float32')

# 3. 分块处理大文件
for chunk in pd.read_csv('large_file.csv', chunksize=100000):
    process(chunk)

# 4. 使用Dask处理超大数据集 (>内存)
import dask.dataframe as dd
df = dd.read_parquet('large_data.parquet')
result = df.groupby('category').mean().compute()
```

---

## 7. 编码与路径问题

### ❌ 症状: Windows上报错 `UnicodeDecodeError: 'gbk' codec can't decode`

**原因**: Windows默认使用GBK编码

**解决方案**:

```python
# 方案1: 显式指定UTF-8编码
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 方案2: 在PowerShell中切换到UTF-8
chcp 65001

# 方案3: 设置环境变量 (永久)
# 在系统环境变量中添加:
PYTHONIOENCODING=utf-8
```

---

### ❌ 症状: Windows上路径报错 (反斜杠转义问题)

**原因**: Python字符串中的`\`被解释为转义字符

**解决方案**:

```python
# 方案1: 使用原始字符串
path = r'C:\Users\username\project\data.csv'

# 方案2: 使用正斜杠 (Windows也支持)
path = 'C:/Users/username/project/data.csv'

# 方案3: 使用pathlib (推荐)
from pathlib import Path
path = Path('C:/Users/username/project') / 'data.csv'
```

---

## 8. 权限问题

### ❌ 症状: `Permission denied` 安装包或运行脚本

**原因**: 权限不足

**解决方案**:

```bash
# 不要使用sudo安装到虚拟环境！
# ❌ 错误: sudo pip install xxx
# ✅ 正确: pip install xxx (在虚拟环境中)

# 脚本权限不足
chmod +x scripts/data/download-stage3.py
./scripts/data/download-stage3.py

# 若文件被占用 (Windows)
# 关闭占用该文件的程序 (如Excel、Jupyter)
```

---

## 9. 内存不足问题

### ❌ 症状: `MemoryError` 或系统卡死

**原因**: 数据集或模型超过可用内存

**解决方案**:

```python
# 1. 减小batch size
batch_size = 16  # 原本64

# 2. 使用生成器而非一次性加载
def data_generator():
    for file in file_list:
        yield load_data(file)

# 3. 删除不再使用的变量
del large_dataframe
import gc
gc.collect()

# 4. 监控内存使用
import psutil
print(f"Memory usage: {psutil.virtual_memory().percent}%")

# 5. 使用内存映射 (memory-mapped files)
import numpy as np
data = np.load('data.npy', mmap_mode='r')
```

---

## 逃生舱：云端GPU方案

**触发条件**: 本地环境问题超过30分钟未解决，或CPU训练 >30分钟/epoch

### 快速启动路径

#### 选项A: Google Colab (免费)

1. 访问 https://colab.research.google.com/
2. 上传Notebook: `File -> Upload notebook`
3. 启用GPU: `Runtime -> Change runtime type -> GPU (T4)`
4. 运行第一个cell安装依赖:
   ```python
   !pip install -q pandas numpy matplotlib scikit-learn
   ```
5. 运行项目代码

**优点**: 免费、即开即用
**缺点**: 会话时限12小时、GPU配额有限

---

#### 选项B: Kaggle Notebooks (免费)

1. 访问 https://www.kaggle.com/code
2. 创建新Notebook，启用GPU
3. 上传数据到Kaggle Datasets
4. 运行代码

**优点**: 免费、社区活跃
**缺点**: 每周GPU配额30小时

---

#### 选项C: 云主机 (AWS/阿里云)

1. 创建GPU实例 (AWS EC2 g4dn.xlarge / 阿里云GPU实例)
2. 选择预配置镜像: `Deep Learning AMI`
3. SSH登录并克隆项目
4. 按快速开始指南安装依赖
5. 运行训练

**成本**: AWS g4dn.xlarge ~$0.5/小时 (按需), Spot实例更便宜

---

## 📞 获取帮助

如果以上方案都无法解决问题：

1. **查看详细文档**: `docs/cross-platform/setup-<your-os>.md`
2. **提交GitHub Issue**: https://github.com/yourusername/py_ai_tutorial/issues
   - 附上错误日志
   - 环境信息 (`python --version`, `pip list`, `nvidia-smi`)
3. **加入学习社群**: [Discord/微信群链接]
4. **邮件支持**: tutorial@example.com

---

## 🎯 预防性建议

- ✅ 定期更新依赖: `uv pip install --upgrade -e .`
- ✅ 使用虚拟环境，避免污染系统Python
- ✅ 提交代码前运行验证: `python scripts/validation/validate-entities.py`
- ✅ 定期清理缓存: `uv cache clean`
- ✅ 备份实验输出: `outputs/` 目录

**记住**: 遇到问题是学习的一部分！这份故障排查指南会持续更新，欢迎贡献你遇到的新问题和解决方案。
