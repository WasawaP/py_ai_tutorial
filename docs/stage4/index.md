# 阶段4：深度学习

## 🎯 学习目标

掌握深度学习框架（PyTorch/TensorFlow），能够完成计算机视觉（CV）和自然语言处理（NLP）的迁移学习项目。通过本阶段学习，你将能够：

- 理解深度学习核心概念（神经网络、反向传播、优化器）
- 熟练使用 PyTorch 和 TensorFlow 构建深度学习模型
- 掌握 CNN（卷积神经网络）在计算机视觉中的应用
- 掌握 Transformer 在自然语言处理中的应用
- 完成工业级 CV/NLP 项目的开发与部署

## 📚 课程模块

### [M01：深度学习基础](01-dl-basics/README.md)

深度学习核心理论与实践：

- **神经网络基础**：感知机、多层感知机、激活函数
- **反向传播算法**：梯度计算、链式法则
- **优化器**：SGD、Adam、学习率调度
- **正则化技术**：Dropout、Batch Normalization、权重衰减
- **PyTorch vs TensorFlow**：框架对比与选择

**学习时长**：3-4 小时

### [M02：计算机视觉基础](02-cv-basics/README.md)

深度学习在图像领域的应用：

- **CNN 架构**：卷积层、池化层、全连接层
- **经典网络**：LeNet、AlexNet、VGG、ResNet、EfficientNet
- **目标检测**：YOLO 系列、Faster R-CNN、DETR
- **图像分割**：U-Net、Mask R-CNN、Segment Anything
- **迁移学习**：预训练模型、微调技巧

**学习时长**：4-6 小时

### [M03：自然语言处理基础](03-nlp-basics/README.md)

深度学习在文本领域的应用：

- **词嵌入**：Word2Vec、GloVe、FastText
- **RNN 架构**：LSTM、GRU、双向 RNN
- **Transformer**：Self-Attention、Multi-Head Attention、位置编码
- **预训练模型**：BERT、GPT、T5
- **下游任务**：文本分类、命名实体识别、机器翻译

**学习时长**：4-6 小时

## 🚀 项目实战

本阶段包含 **7 个工业级深度学习项目**，其中 **4 个核心项目提供 PyTorch 和 TensorFlow 双框架实现**：

| 项目 | 名称 | 技术栈 | 框架 | 难度 |
|------|------|--------|------|------|
| [P01](projects/p01-industrial-vision/README.md) | 工业视觉检测 | CNN + 迁移学习 | TensorFlow + TF Lite | ⭐⭐⭐ |
| [P02](projects/p02-yolov11-realtime/README.md) | 基于YOLOv11的视频实时检测系统 ⭐ | YOLO + 实时推理 | **双框架** | ⭐⭐⭐⭐ |
| [P03](projects/p03-ocr/README.md) | OCR票据识别 | PaddleOCR + 后处理 | PaddlePaddle | ⭐⭐⭐ |
| [P04](projects/p04-image-segmentation/README.md) | 自动驾驶场景图像分割 ⭐ | U-Net + DeepLab | **双框架** | ⭐⭐⭐⭐ |
| [P05](projects/p05-medical-imaging/README.md) | 医学影像分析 | 3D CNN + MONAI | PyTorch | ⭐⭐⭐⭐ |
| [P06](projects/p06-transformer-translation/README.md) | 基于Transformer的翻译系统 ⭐ | Transformer + BPE | **双框架** | ⭐⭐⭐⭐ |
| [P07](projects/p07-pretrained-info-extraction/README.md) | 基于预训练模型的信息提取系统 ⭐ | BERT + NER/RE | **双框架** | ⭐⭐⭐⭐ |

### 项目特点

✅ **工业标准**：遵循业界最佳实践，代码可直接用于生产环境
✅ **双框架实现**：核心项目提供 PyTorch 和 TensorFlow 两种实现，对比学习
✅ **端到端**：从数据预处理到模型部署的完整流程
✅ **GPU 加速**：充分利用 GPU 并行计算能力（CPU 也可运行，速度较慢）
✅ **模型部署**：包含 ONNX 导出、TensorRT 优化、移动端部署示例

## ⏱️ 学习时长

- **理论学习**：11-16 小时（3 个模块）
- **项目实战**：21-35 小时（7 个项目，每个 3-5 小时）
- **总计**：32-51 小时

建议学习节奏：
- **速通模式**（2-3周）：专注核心模块 + 4 个双框架项目
- **深度学习模式**（4-6周）：完成所有模块 + 全部 7 个项目

## 🛠️ 环境准备

### 系统要求

- Python ≥3.9（推荐 3.11+）
- 内存：16GB+（GPU 训练推荐 32GB+）
- 磁盘空间：约 20GB（数据集 + 预训练模型）
- GPU：**推荐**（NVIDIA GPU 6GB+ 显存，支持 CUDA 11.8+）
  - CPU 也可运行，但速度慢 5-10 倍

### 快速安装

#### CPU 版本（适合测试与学习）

```bash
# 1. 创建虚拟环境
uv venv --python 3.11
source .venv/bin/activate

# 2. 安装阶段4依赖（CPU版本）
uv pip install -e ".[stage4]"
```

#### GPU 版本（推荐用于实际训练）

**NVIDIA GPU (Linux/Windows)**:
```bash
# 1. 确认 CUDA 版本（需要 11.8+）
nvidia-smi

# 2. 安装阶段4依赖（GPU版本）
uv pip install -e ".[stage4,gpu]"

# 3. 验证 GPU 可用性
python -c "import torch; print(torch.cuda.is_available())"
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```

**Apple Silicon (macOS M1/M2/M3)**:
```bash
# 使用 MPS (Metal Performance Shaders) 加速
uv pip install -e ".[stage4]"

# 验证 MPS 可用性
python -c "import torch; print(torch.backends.mps.is_available())"
```

### 数据集下载

```bash
# 下载阶段4数据集（~15GB，包含预训练模型）
python scripts/data/download-stage4.py

# 验证数据完整性
python scripts/data/verify.py --stage 4
```

详细的跨平台配置指引：
- [macOS Apple Silicon](../cross-platform/setup-macos-arm64.md)（MPS GPU 加速）
- [Linux](../cross-platform/setup-linux.md)（CUDA GPU 加速）
- [Windows WSL2](../cross-platform/setup-windows-wsl2.md)（推荐）
- [云端 GPU](../cross-platform/setup-cloud-gpu.md)（Google Colab、AWS、自托管）

## 📖 学习路径建议

### 新手路径（按顺序学习）

1. **M01 深度学习基础** → 理解神经网络原理
2. **P01 工业视觉检测** → 第一个 CNN 项目（TensorFlow）
3. **M02 计算机视觉基础** → 深入 CNN 架构
4. **P02 YOLOv11实时检测** → 实战目标检测（双框架对比）
5. **M03 自然语言处理基础** → 学习 Transformer
6. **P06 Transformer翻译** → 实战 Transformer（双框架对比）
7. **P07 信息提取系统** → 实战预训练模型微调
8. 选做其他 3 个项目巩固技能

### 有经验者路径（可跳过部分模块）

- 如果熟悉 PyTorch/TensorFlow → 直接从项目开始
- 如果只关注 CV → 完成 P01-P05
- 如果只关注 NLP → 完成 M03 + P06-P07
- 如果想快速进入大模型开发 → 完成 P06-P07 后进入[阶段5](../stage5/index.md)

### 双框架学习策略

本阶段的 4 个核心项目（P02、P04、P06、P07）提供 PyTorch 和 TensorFlow 双框架实现：

**推荐学习顺序**：
1. 先用一个框架完成项目（如 PyTorch）
2. 对比另一个框架的实现（TensorFlow）
3. 总结两个框架的异同点

**框架选择建议**：
- **学术研究/灵活性** → 优先 PyTorch
- **工业部署/移动端** → 优先 TensorFlow
- **求职竞争力** → 两者都学

## 🎓 前置知识要求

✅ **必须掌握**：
- [阶段3：机器学习与数据挖掘](../stage3/index.md)（建议完成 P01-P03）
- Python 科学计算栈（NumPy、Pandas、Matplotlib）
- 线性代数基础（矩阵运算、向量空间）
- 微积分基础（求导、梯度）

❓ **有帮助但非必须**：
- Linux 命令行（GPU 环境配置）
- Docker（容器化部署）
- Git（版本控制）

不满足前置要求？建议先完成[阶段3](../stage3/index.md)

## 🔗 相关资源

### 官方文档
- [PyTorch 官方教程](https://pytorch.org/tutorials/)
- [TensorFlow 官方教程](https://www.tensorflow.org/tutorials)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers/)

### 项目资源
- [官方文档](https://shychee.github.io/py_ai_tutorial/)
- [GitHub 仓库](https://github.com/shychee/py_ai_tutorial)
- [问题反馈](https://github.com/shychee/py_ai_tutorial/issues)
- [贡献指南](../contributing.md)

## ⏭️ 下一步

完成阶段4后，继续学习：
- **[阶段5：AIGC与大模型](../stage5/index.md)** - LangChain + RAG + Agent
- 或深入研究特定领域：
  - 计算机视觉：目标跟踪、3D 视觉、视频理解
  - 自然语言处理：大语言模型、多模态模型

---

**准备好了吗？从 [M01：深度学习基础](01-dl-basics/README.md) 开始你的深度学习之旅！** 🚀
