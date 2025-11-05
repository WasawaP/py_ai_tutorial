# 离线数据包目录 (Offline Data Packages)

本目录用于存放离线数据包，供无法直接访问互联网或网络受限的学习环境使用。

---

## 📦 目录结构

```
offline/
├── README.md                          # 本文件
├── stage3/                            # 阶段3数据包
│   ├── datasets-stage3-v1.0.tar.gz    # 完整数据集包 (~2GB)
│   ├── checksums.txt                  # SHA256校验和
│   └── README.md                      # 阶段3数据说明
├── stage4/                            # 阶段4数据包
│   ├── datasets-stage4-v1.0.tar.gz    # 完整数据集包 (~5GB)
│   ├── models-pretrained-v1.0.tar.gz  # 预训练模型包 (~3GB)
│   ├── checksums.txt                  # SHA256校验和
│   └── README.md                      # 阶段4数据说明
└── stage5/                            # 阶段5数据包
    ├── datasets-stage5-v1.0.tar.gz    # 完整数据集包 (~1GB)
    ├── models-llm-v1.0.tar.gz         # LLM模型包 (~10GB)
    ├── checksums.txt                  # SHA256校验和
    └── README.md                      # 阶段5数据说明
```

---

## 🔽 下载链接

### 阶段3：机器学习与数据挖掘 (Stage 3)

| 文件名 | 大小 | 下载链接 | 校验和 (SHA256) |
|-------|------|---------|----------------|
| datasets-stage3-v1.0.tar.gz | ~2GB | [待发布] | 待生成 |

**包含数据集**:
- P01: 朝阳医院销售数据 (hospital_sales.csv, ~50MB)
- P02: 服装零售数据 (clothing_retail.csv, ~100MB)
- P03: 银行营销数据 (bank_marketing.csv, ~200MB)
- P04: 通讯公司客户数据 (telecom_customer.csv, ~150MB)
- P05: 零售超市数据 (retail_supermarket.csv, ~300MB)
- P06: 滴滴运营数据 (didi_operations.csv, ~400MB)
- P07: 淘宝用户行为数据 (taobao_user_behavior.csv, ~500MB)
- P08: 航空公司客户数据 (airline_customer.csv, ~200MB)
- P09: 信贷数据 (credit_loan.csv, ~100MB)

### 阶段4：深度学习 (Stage 4)

| 文件名 | 大小 | 下载链接 | 校验和 (SHA256) |
|-------|------|---------|----------------|
| datasets-stage4-v1.0.tar.gz | ~5GB | [待发布] | 待生成 |
| models-pretrained-v1.0.tar.gz | ~3GB | [待发布] | 待生成 |

**包含数据集**:
- P01: 工业视觉检测图像 (industrial_vision/, ~500MB)
- P02: COCO目标检测数据集子集 (coco_subset/, ~1GB)
- P03: 票据OCR图像 (receipt_ocr/, ~300MB)
- P04: 自动驾驶场景数据 (autonomous_driving/, ~1.5GB)
- P05: 医学影像数据 (medical_imaging/, ~800MB)
- P06: 翻译语料库 (translation_corpus/, ~400MB)
- P07: 信息提取数据集 (info_extraction/, ~500MB)

**包含预训练模型**:
- ResNet50 (PyTorch & TensorFlow, ~100MB each)
- YOLOv11 weights (~200MB)
- PaddleOCR models (~150MB)
- BERT-base-chinese (~400MB)
- Transformer translation model (~300MB)

### 阶段5：AIGC与大模型 (Stage 5)

| 文件名 | 大小 | 下载链接 | 校验和 (SHA256) |
|-------|------|---------|----------------|
| datasets-stage5-v1.0.tar.gz | ~1GB | [待发布] | 待生成 |
| models-llm-v1.0.tar.gz | ~10GB | [待发布] | 待生成 |

**包含数据集**:
- P01: 对话系统知识库 (dialogue_kb/, ~500MB)
- P01: RAG文档库 (rag_corpus/, ~500MB)

**包含LLM模型**:
- DeepSeek-7B (GGUF格式, ~4GB)
- ChatGLM3-6B (GGUF格式, ~3.5GB)
- Qwen-7B (GGUF格式, ~4GB)

---

## 📥 使用方式

### 方式1：自动解压脚本（推荐）

```bash
# 下载并解压阶段3数据包
cd /path/to/py_ai_tutorial
python scripts/data/install-offline.py --stage 3 --offline-dir offline/

# 下载并解压阶段4数据包（含预训练模型）
python scripts/data/install-offline.py --stage 4 --offline-dir offline/ --include-models

# 下载并解压阶段5数据包（含LLM模型）
python scripts/data/install-offline.py --stage 5 --offline-dir offline/ --include-models
```

### 方式2：手动解压

```bash
# 解压阶段3数据包
cd /path/to/py_ai_tutorial
tar -xzf offline/stage3/datasets-stage3-v1.0.tar.gz -C data/

# 解压阶段4数据包
tar -xzf offline/stage4/datasets-stage4-v1.0.tar.gz -C data/
tar -xzf offline/stage4/models-pretrained-v1.0.tar.gz -C models/

# 解压阶段5数据包
tar -xzf offline/stage5/datasets-stage5-v1.0.tar.gz -C data/
tar -xzf offline/stage5/models-llm-v1.0.tar.gz -C models/
```

### 方式3：校验数据完整性

```bash
# 校验阶段3数据包
cd offline/stage3
sha256sum -c checksums.txt

# 校验阶段4数据包
cd offline/stage4
sha256sum -c checksums.txt

# 校验阶段5数据包
cd offline/stage5
sha256sum -c checksums.txt
```

---

## 🔄 更新策略

离线数据包版本号遵循语义化版本规范 (Semantic Versioning):
- **主版本号 (Major)**: 数据结构发生重大变化
- **次版本号 (Minor)**: 新增数据集或模型
- **修订号 (Patch)**: 数据修正或补充

**当前版本**: v1.0.0 (初始版本)

**更新检查**:
```bash
python scripts/data/check-updates.py --offline-mode
```

---

## 🌐 在线下载脚本（联网环境）

如果您处于联网环境，可以使用在线下载脚本自动获取数据：

```bash
# 下载阶段3数据（在线）
python scripts/data/download-stage3.py

# 下载阶段4数据（在线）
python scripts/data/download-stage4.py

# 下载阶段5数据（在线）
python scripts/data/download-stage5.py
```

---

## 📊 数据集许可证

所有数据集均遵循各自的许可证协议：
- 开源数据集：遵循原始许可证（MIT, Apache 2.0, CC-BY等）
- 自定义数据集：遵循项目MIT许可证
- 预训练模型：遵循模型发布方的许可证

**详细许可证信息**: 请参阅各阶段的 `offline/stageX/README.md` 文件

---

## 🆘 故障排查

### 问题1：下载速度慢

**解决方案**:
- 使用国内镜像源（待发布）
- 使用BT/磁力链接（待发布）
- 联系教程维护团队获取U盘/硬盘拷贝

### 问题2：解压失败

**错误信息**: `tar: Error is not recoverable: exiting now`

**解决方案**:
```bash
# 重新下载数据包
wget -c [下载链接] -O offline/stageX/datasets-stageX-vX.X.tar.gz

# 校验完整性
sha256sum -c offline/stageX/checksums.txt

# 使用verbose模式解压
tar -xzvf offline/stageX/datasets-stageX-vX.X.tar.gz -C data/
```

### 问题3：磁盘空间不足

**检查磁盘空间**:
```bash
df -h .
```

**最小空间要求**:
- 阶段3: 5GB (数据2GB + 解压缓冲3GB)
- 阶段4: 15GB (数据5GB + 模型3GB + 解压缓冲7GB)
- 阶段5: 20GB (数据1GB + 模型10GB + 解压缓冲9GB)

**解决方案**: 清理不必要的文件或使用外接存储设备

---

## 📞 联系方式

如需获取离线数据包或遇到问题，请通过以下方式联系：

- **GitHub Issues**: [提交问题](https://github.com/yourusername/py_ai_tutorial/issues)
- **邮件**: tutorial@example.com
- **社区**: [讨论区](https://github.com/yourusername/py_ai_tutorial/discussions)

---

**最后更新**: 2025-01-15
