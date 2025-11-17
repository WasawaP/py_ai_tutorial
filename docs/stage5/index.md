# 阶段5：AIGC与大模型

## 🎯 学习目标

掌握大语言模型（LLM）应用开发技术，能够完成端到端的对话系统和 AI Agent 开发。通过本阶段学习，你将能够：

- 理解大语言模型的工作原理与应用场景
- 掌握 Prompt Engineering（提示工程）技术
- 使用 LangChain 构建 LLM 应用
- 实现 RAG（检索增强生成）系统
- 开发 AI Agent（智能代理）
- 完成生产级对话系统的开发与部署

## 📚 课程模块

### [M01：AIGC 与 LLM 概述](01-aigc-llm-intro/README.md)

大语言模型基础理论与生态：

- **AIGC 发展史**：从 GPT-1 到 GPT-4、Claude、Gemini
- **LLM 工作原理**：Transformer 架构、预训练与微调、涌现能力
- **主流 LLM 对比**：OpenAI GPT 系列、Anthropic Claude、Google Gemini、DeepSeek、通义千问、文心一言
- **应用场景**：文本生成、问答系统、代码助手、多模态交互
- **API 调用**：OpenAI API、DeepSeek API、开源模型部署

**学习时长**：2-3 小时

### [M02：大模型开发](02-llm-dev/README.md)

LLM 应用开发核心技术：

- **Prompt Engineering**：Zero-shot、Few-shot、Chain-of-Thought、Self-Consistency
- **LangChain 框架**：LLM 封装、Prompt 模板、输出解析、链式调用
- **RAG 系统**：向量数据库、文档切片、相似度检索、上下文增强
- **AI Agent**：ReAct 框架、工具调用、多轮对话、记忆管理
- **Fine-tuning**：LoRA、QLoRA、指令微调、RLHF
- **模型评估**：困惑度、BLEU、ROUGE、人工评估

**学习时长**：5-8 小时

## 🚀 项目实战

本阶段包含 **1 个综合性大模型应用项目**，涵盖 RAG、Agent、多轮对话等核心技术：

| 项目 | 名称 | 技术栈 | 难度 |
|------|------|--------|------|
| [P01](projects/p01-dialogue-system/README.md) | 基于 LLM 的对话系统 | DeepSeek + LangChain + RAG + Agent | ⭐⭐⭐⭐⭐ |

### 项目亮点

✅ **完整的对话系统**：
- 多轮对话管理
- 上下文记忆机制
- 意图识别与槽位填充
- 知识库检索增强

✅ **企业级 RAG 系统**：
- 支持多种文档格式（PDF、Markdown、TXT）
- 文档智能分块（Semantic Chunking）
- 向量数据库（Chroma/Qdrant）
- 混合检索（稠密向量 + 稀疏向量）

✅ **功能丰富的 AI Agent**：
- 工具调用（搜索、计算、数据查询）
- ReAct 推理框架
- 错误处理与重试机制
- 多 Agent 协作

✅ **生产级部署**：
- FastAPI Web 服务
- WebSocket 流式输出
- Docker 容器化
- 性能监控与日志

## ⏱️ 学习时长

- **理论学习**：7-11 小时（2 个模块）
- **项目实战**：16-24 小时（1 个综合项目）
- **总计**：23-35 小时

建议学习节奏：
- **速通模式**（1-2周）：完成核心模块 + 基础对话功能
- **深度学习模式**（3-4周）：完成所有模块 + 全部项目功能 + 生产部署

## 🛠️ 环境准备

### 系统要求

- Python ≥3.9（推荐 3.11+）
- 内存：16GB+（本地部署大模型需要 32GB+）
- 磁盘空间：约 10GB（向量数据库 + 文档）
- GPU：**可选**（本地部署大模型需要，API 调用无需 GPU）

### 快速安装

```bash
# 1. 创建虚拟环境
uv venv --python 3.11
source .venv/bin/activate

# 2. 安装阶段5依赖
uv pip install -e ".[stage5]"

# 3. 配置 API Keys（二选一）
# 方案1：使用 DeepSeek API（推荐，性价比高）
export DEEPSEEK_API_KEY="your-deepseek-api-key"

# 方案2：使用 OpenAI API
export OPENAI_API_KEY="your-openai-api-key"

# 4. 验证环境
python scripts/env/check-stage5.py
```

### LLM 选择建议

本教程优先使用 **DeepSeek API**，原因：
- ✅ 性价比极高（比 GPT-4 便宜 90%+）
- ✅ 中文能力强（中国团队开发）
- ✅ 推理能力优秀（数学、编程能力接近 GPT-4）
- ✅ 无需科学上网

**其他选项**：
- **OpenAI GPT-4/GPT-3.5**：性能最强，但价格较高，需要科学上网
- **通义千问/文心一言**：国内大厂模型，中文能力强
- **开源模型（本地部署）**：LLaMA 3、Qwen、GLM-4（需要高性能 GPU）

### 数据准备

```bash
# 下载示例文档库（可选，~500MB）
python scripts/data/download-stage5.py

# 或使用自己的文档
mkdir -p data/stage5/documents
cp your_documents/* data/stage5/documents/
```

## 📖 学习路径建议

### 推荐学习路径（按顺序）

1. **M01 AIGC与LLM概述** → 理解大模型原理与生态
2. **简单对话 Demo** → 快速体验 LLM API 调用
3. **M02 大模型开发** → 系统学习开发技术
4. **P01 对话系统（第1部分）** → 实现基础对话功能
5. **P01 对话系统（第2部分）** → 实现 RAG 知识库
6. **P01 对话系统（第3部分）** → 实现 AI Agent
7. **P01 对话系统（第4部分）** → 生产部署与优化

### 进阶方向

完成阶段5后，可以选择以下方向深入：

**技术方向**：
- **多模态 LLM**：GPT-4V、Claude 3、Gemini（图像理解、视频分析）
- **本地化部署**：vLLM、TensorRT-LLM、LLaMA.cpp（高性能推理）
- **Fine-tuning**：LoRA、QLoRA（领域模型定制）
- **多 Agent 系统**：AutoGPT、MetaGPT（复杂任务分解）

**应用方向**：
- **企业知识库**：内部文档检索、FAQ 问答
- **代码助手**：代码生成、代码审查、Bug 修复
- **创意写作**：小说、剧本、广告文案生成
- **数据分析**：自然语言查询数据库、报表生成

## 🎓 前置知识要求

✅ **必须掌握**：
- [阶段3：机器学习与数据挖掘](../stage3/index.md)（理解基础 ML 概念）
- [阶段4：深度学习](../stage4/index.md)（建议完成 M03 NLP 模块 + P06 Transformer 项目）
- Python 异步编程（async/await）
- RESTful API 开发（FastAPI/Flask）

❓ **有帮助但非必须**：
- Transformer 架构深入理解
- 向量数据库（Chroma、Qdrant、Milvus）
- Docker 容器化部署
- 前端开发（React/Vue，用于构建 UI）

不满足前置要求？建议先完成[阶段4](../stage4/index.md)的 NLP 模块

## 💡 常见问题

### Q1: 一定要用 GPU 吗？
**A**: 不需要！使用 API 调用（DeepSeek/OpenAI）无需 GPU。只有本地部署大模型时才需要高性能 GPU（如 A100、4090）。

### Q2: API 费用大概多少？
**A**:
- **DeepSeek**: ~¥1.5/百万 tokens（输入），~¥2/百万 tokens（输出）
- **OpenAI GPT-4**: ~$15/百万 tokens（输入），~$30/百万 tokens（输出）
- 完成 P01 项目预估费用：¥5-20（DeepSeek）或 $10-50（OpenAI）

### Q3: 可以完全离线学习吗？
**A**: 可以，但需要：
- 本地部署开源模型（如 Qwen-7B、GLM-4-9B）
- 高性能 GPU（≥24GB 显存）
- 更多的环境配置工作

推荐先用 API 完成学习，再考虑本地部署。

### Q4: 如何保护 API Key 安全？
**A**:
- 使用环境变量，不要硬编码在代码中
- 不要将 `.env` 文件提交到 Git
- 使用 `.gitignore` 排除敏感文件
- 生产环境使用密钥管理服务（如 AWS Secrets Manager）

## 🔗 相关资源

### 官方文档
- [OpenAI API 文档](https://platform.openai.com/docs/)
- [LangChain 文档](https://python.langchain.com/)
- [DeepSeek 文档](https://platform.deepseek.com/docs)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers/)

### 推荐阅读
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [RAG 最佳实践](https://docs.llamaindex.ai/en/stable/optimizing/production_rag/)
- [AI Agent 设计模式](https://python.langchain.com/docs/modules/agents/)

### 项目资源
- [官方文档](https://shychee.github.io/py_ai_tutorial/)
- [GitHub 仓库](https://github.com/shychee/py_ai_tutorial)
- [问题反馈](https://github.com/shychee/py_ai_tutorial/issues)
- [贡献指南](../contributing.md)

## 🎓 学习路线总结

恭喜你来到最后一个阶段！回顾完整学习路径：

1. **[阶段3：机器学习与数据挖掘](../stage3/index.md)** - 数据分析 + 传统 ML
2. **[阶段4：深度学习](../stage4/index.md)** - CNN + Transformer + 迁移学习
3. **阶段5：AIGC与大模型**（当前）- LLM 应用开发

完成全部三个阶段后，你将具备：
- ✅ 端到端 AI 项目开发能力
- ✅ 传统 ML + 深度学习 + LLM 全栈技能
- ✅ 17 个真实项目经验
- ✅ PyTorch/TensorFlow/LangChain 多框架能力
- ✅ 工业级代码质量标准

---

**准备好了吗？从 [M01：AIGC与LLM概述](01-aigc-llm-intro/README.md) 开始你的大模型应用开发之旅！** 🚀
