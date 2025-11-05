# Implementation Guide: Python AI Tutorial Project

**Generated**: 2025-11-05
**Status**: Phase 1 Setup Completed (6/9 tasks)
**Estimated Remaining Effort**: 145 tasks, 6-8 weeks (1 FTE) or 3-4 weeks (3 FTE)

---

## 📋 Current Progress

### ✅ Completed Tasks (6/9)

| Task ID | Description | Status |
|---------|-------------|--------|
| T001 | Create project directory structure | ✅ DONE |
| T002 | Configure pyproject.toml | ✅ DONE |
| T003 | Create .python-version | ✅ DONE |
| T004 | Create .gitignore | ✅ DONE |
| T005 | Configure mkdocs.yml | ✅ DONE |
| T006 | Write README.md | ✅ DONE |

### 🔄 Remaining Phase 1 Tasks (3/9)

| Task ID | Description | Priority | Estimated Time |
|---------|-------------|----------|----------------|
| T007 | Configure CI/CD (GitHub Actions) | Medium | 30 min |
| T008 | Create offline data directory structure | Low | 10 min |
| T009 | Initialize Git repository and first commit | High | 10 min |

---

## 🎯 Recommended Implementation Paths

### Path A: MVP-First (Single Developer, 2-3 weeks)

**Goal**: Deliver a working MVP (User Story 1 - Stage 3) as quickly as possible

#### Week 1: Foundation & Setup
**Days 1-2**: Complete remaining setup + Foundation basics
- [ ] T007: Configure CI/CD
- [ ] T008-T009: Finalize setup
- [ ] T010-T013: Create YAML entity configurations (stages, modules, projects, datasets)
- [ ] T014-T021: Implement core scripts (env detection, data verification, validation)

**Days 3-5**: Foundation infrastructure + Cross-platform docs
- [ ] T022-T028: Write all 6 OS setup guides + troubleshooting
- [ ] T029-T032: Write auxiliary docs (glossary, prerequisites, learning path, framework comparison)

#### Week 2-3: Stage 3 Content Creation
**Week 2, Days 1-3**: Modules + Data prep
- [ ] T033-T044: Write all 4 module tutorials + create Notebooks (12 files)
- [ ] T045-T047: Implement stage 3 data download scripts + offline package

**Week 2, Days 4-5 + Week 3, Days 1-2**: First batch of projects
- [ ] T048-T053: Project P01 (Healthcare)
- [ ] T054-T058: Project P02 (Ecommerce)
- [ ] T059-T063: Project P03 (Finance)

**Week 3, Days 3-5**: Remaining projects + Evaluation
- [ ] T064-T082: Projects P04-P09 (6 projects, can parallelize)
- [ ] T083-T085: Create rubrics, metrics, evaluation scripts

**MVP Delivery**: End of Week 3
- Learners can complete Stage 3 on any OS
- 9 working projects with evaluation
- Full cross-platform support

---

### Path B: Team Parallel Development (3 Developers, 1 week MVP)

**Team Structure**:
- **Dev A (Foundation Lead)**: Infrastructure & cross-platform
- **Dev B (Content Creator 1)**: Stage 3 modules + first 3 projects
- **Dev C (Content Creator 2)**: Stage 3 last 6 projects + evaluation

#### Sprint 1 (Days 1-2): Foundation Sprint

**Dev A - Foundation Infrastructure**:
```bash
# Day 1 Morning
- T007: Configure .github/workflows/ci.yml
- T010-T013: Create configs/content/*.yaml (stages, modules, projects, datasets)

# Day 1 Afternoon
- T014: scripts/env/detect-platform.py
- T015: scripts/data/verify.py
- T018-T020: scripts/validation/*.py

# Day 2
- T022-T028: docs/cross-platform/*.md (6 OS guides + troubleshooting)
```

**Dev B - Module Content**:
```bash
# Day 1-2
- T033-T036: Module M01 docs + 3 notebooks (NumPy/Pandas/Viz)
- T037-T039: Module M02 docs + 2 notebooks (Pandas practice)
- T040-T042: Module M03 docs + 2 notebooks (Math basics)
- T043-T044: Module M04 docs + 1 notebook (ML advanced)
```

**Dev C - Support Infrastructure**:
```bash
# Day 1
- T016-T017: Create project templates
- T021: configs/content/environments.yaml
- T029-T032: Auxiliary docs (glossary, prerequisites, learning path, framework comparison)

# Day 2
- T045-T047: Stage 3 data scripts + offline package prep
```

#### Sprint 2 (Days 3-5): Content Creation Sprint

**Dev A - Review & Integration**:
```bash
# Day 3
- Review all foundation work
- T008-T009: Finalize setup & git commit
- Integration testing

# Day 4-5
- T083-T085: Evaluation system (rubrics, metrics, eval scripts)
- CI/CD pipeline testing
```

**Dev B - Projects P01-P03**:
```bash
# Day 3
- T048-T053: Project P01 Healthcare (6 tasks)

# Day 4
- T054-T058: Project P02 Ecommerce (5 tasks)

# Day 5
- T059-T063: Project P03 Finance (5 tasks)
```

**Dev C - Projects P04-P09**:
```bash
# Day 3
- T064-T067: Project P04 Telecom (4 tasks)
- T068-T070: Project P05 Retail (3 tasks)

# Day 4
- T071-T073: Project P06 Internet (3 tasks)
- T074-T076: Project P07 Ecommerce Annual (3 tasks)

# Day 5
- T077-T079: Project P08 Airline (3 tasks)
- T080-T082: Project P09 Credit (3 tasks)
```

**MVP Delivery**: End of Day 5
- Complete Stage 3 tutorial system
- All 9 projects working and tested
- Evaluation system functional

---

## 📝 Detailed Task Breakdown

### Phase 1: Remaining Setup (T007-T009)

#### T007: Configure CI/CD (.github/workflows/ci.yml)

**File**: `.github/workflows/ci.yml`

```yaml
name: CI

on:
  push:
    branches: [ main, develop, 002-ai-tutorial-stages ]
  pull_request:
    branches: [ main, develop ]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install uv
        run: |
          curl -LsSf https://astral.sh/uv/install.sh | sh
          echo "$HOME/.cargo/bin" >> $GITHUB_PATH

      - name: Install dependencies
        run: |
          uv venv
          source .venv/bin/activate
          uv pip install -e ".[dev]"

      - name: Validate data models
        run: |
          python scripts/validation/validate-entities.py
          python scripts/validation/validate-paths.py
          python scripts/validation/validate-relationships.py

      - name: Run tests
        run: |
          pytest tests/ --cov=scripts --cov-report=xml

      - name: Code quality checks
        run: |
          black --check scripts/ tests/
          ruff check scripts/ tests/
          mypy scripts/

  build-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -e ".[docs]"

      - name: Build MkDocs
        run: |
          mkdocs build --strict

      - name: Deploy to GitHub Pages (main branch only)
        if: github.ref == 'refs/heads/main'
        run: |
          mkdocs gh-deploy --force
```

**Estimated Time**: 30 minutes

---

#### T008: Create offline data directory structure

**Commands**:
```bash
mkdir -p offline/stage3-data
mkdir -p offline/stage4-data
mkdir -p offline/stage5-data
mkdir -p offline/stage4-models

# Create README for offline packages
cat > offline/README.md << 'EOF'
# Offline Data Packages

本目录包含离线数据包，用于网络受限环境。

## 下载链接

- **Stage 3 数据包** (~1.5GB): [百度网盘链接] | [阿里云盘链接]
- **Stage 4 数据包** (~6GB): [百度网盘链接] | [阿里云盘链接]
- **Stage 4 模型包** (~3GB): [百度网盘链接] | [阿里云盘链接]
- **Stage 5 数据包** (~2GB): [百度网盘链接] | [阿里云盘链接]

## 使用方法

1. 下载对应阶段的离线包（.tar.gz格式）
2. 解压到对应目录：
   ```bash
   tar -xzf stage3-data.tar.gz -C data/stage3/
   tar -xzf stage4-data.tar.gz -C data/stage4/
   ```
3. 验证完整性：
   ```bash
   python scripts/data/verify.py --stage 3 --offline
   ```

## 校验和

所有数据包附带 `checksums.txt` 文件（SHA256）。
EOF
```

**Estimated Time**: 10 minutes

---

#### T009: Initialize Git and first commit

**Commands**:
```bash
cd /Users/hanlinqi/Desktop/Code/AICode/py_ai_tutorial

# Check git status
git status

# Add all setup files
git add pyproject.toml .python-version .gitignore mkdocs.yml README.md
git add docs/ notebooks/ scripts/ data/ templates/ tests/ configs/ offline/
git add .github/

# Create first commit
git commit -m "feat: 初始化项目结构与配置

- 配置 pyproject.toml（uv包管理，阶段3/4/5依赖分组）
- 配置 MkDocs（Material主题，中文支持）
- 创建项目目录结构（docs, notebooks, scripts, data, templates, tests）
- 配置 CI/CD（GitHub Actions）
- 编写项目 README（快速开始指南、学习路径）

Co-authored-by: Claude <claude@anthropic.com>"

# Push to feature branch
git push origin 002-ai-tutorial-stages
```

**Estimated Time**: 10 minutes

---

### Phase 2: Foundation (T010-T032)

This phase is **critical** - all User Stories depend on it. Prioritize completion before starting any Stage 3 content.

#### High Priority Foundation Tasks (T010-T021)

**T010-T013: Create YAML Entity Configurations**

These files define the data model for the entire tutorial system.

**File**: `configs/content/stages.yaml`
```yaml
stages:
  - id: stage3
    name: 机器学习与数据挖掘
    name_en: Machine Learning & Data Mining
    description: 掌握传统机器学习算法（分类、回归、聚类、集成学习）及其在实际业务场景中的应用，熟练使用scikit-learn与数据分析工具栈。
    order: 1
    prerequisites: []
    estimated_hours:
      theory_min: 2
      theory_max: 3
      practice_min: 2
      practice_max: 3
    modules:
      - stage3-m01-scientific-computing
      - stage3-m02-pandas-practice
      - stage3-m03-ml-basics
      - stage3-m04-ml-advanced
    projects:
      - stage3-p01-healthcare
      - stage3-p02-ecommerce
      - stage3-p03-finance
      - stage3-p04-telecom
      - stage3-p05-retail
      - stage3-p06-internet
      - stage3-p07-ecommerce-annual
      - stage3-p08-airline
      - stage3-p09-credit
    learning_outcomes:
      - 能使用NumPy进行高效数组运算与数据预处理
      - 能使用Pandas完成数据清洗、探索性分析与特征工程
      - 理解分类、回归、聚类算法原理并能选择合适算法解决业务问题
      - 能使用scikit-learn训练模型、调参与评估，并解释模型结果
      - 能完成端到端的机器学习项目（从数据到模型交付）

  - id: stage4
    name: 深度学习
    name_en: Deep Learning
    description: 掌握深度学习框架（PyTorch/TensorFlow），能完成CV/NLP迁移学习项目，理解神经网络训练技巧。
    order: 2
    prerequisites:
      - stage3
    estimated_hours:
      theory_min: 3
      theory_max: 4
      practice_min: 3
      practice_max: 6
    modules:
      - stage4-m01-dl-basics
      - stage4-m02-cv-basics
      - stage4-m03-nlp-basics
    projects:
      - stage4-p01-industrial-vision
      - stage4-p02-yolov11-realtime
      - stage4-p03-ocr
      - stage4-p04-image-segmentation
      - stage4-p05-medical-imaging
      - stage4-p06-transformer-translation
      - stage4-p07-pretrained-info-extraction
    learning_outcomes:
      - 掌握PyTorch/TensorFlow框架，能定义与训练神经网络
      - 理解CNN原理，能完成图像分类、目标检测、图像分割任务
      - 理解RNN/Transformer原理，能完成文本分类、序列标注、翻译任务
      - 能使用预训练模型进行迁移学习，提升小数据集场景下的性能
      - 能在CPU/GPU环境部署深度学习模型

  - id: stage5
    name: AIGC与大模型
    name_en: AIGC & Large Language Models
    description: 掌握LLM应用开发（Prompt/RAG/Agent），能完成端到端对话系统，理解大模型微调技术。
    order: 3
    prerequisites:
      - stage4
    estimated_hours:
      theory_min: 2
      theory_max: 3
      practice_min: 6
      practice_max: 9
    modules:
      - stage5-m01-aigc-llm-intro
      - stage5-m02-llm-dev
    projects:
      - stage5-p01-dialogue-system
    learning_outcomes:
      - 理解GPT/LLM原理与应用场景，能选择合适的LLM API
      - 掌握Prompt Engineering技巧，能设计有效的提示词
      - 能搭建RAG系统，实现知识检索增强生成
      - 能设计Agent工作流，实现多步骤任务自动化
      - 能使用LoRA/QLoRA轻量微调LLM，适配特定领域
```

**Similar files needed**:
- `configs/content/modules.yaml` (define all 9 modules)
- `configs/content/projects.yaml` (define all 17 projects)
- `configs/content/datasets.yaml` (define all datasets with download URLs, checksums)

**Estimated Time**: 2-3 hours for all 4 YAML files

---

**T014-T020: Implement Core Scripts**

These scripts are essential for environment setup, data management, and validation.

**Priority Order**:
1. T014: `scripts/env/detect-platform.py` (helps learners identify their OS)
2. T015: `scripts/data/verify.py` (ensures data integrity)
3. T018-T020: Validation scripts (ensures YAML configs are correct)

**Example**: `scripts/env/detect-platform.py`

```python
#!/usr/bin/env python3
"""
环境检测脚本
自动检测操作系统、CPU架构、GPU可用性、Python版本等信息
"""

import platform
import sys
from pathlib import Path
from typing import Dict, Optional

def detect_os() -> str:
    """检测操作系统"""
    system = platform.system()
    if system == "Darwin":
        return "macOS"
    elif system == "Linux":
        return "Linux"
    elif system == "Windows":
        return "Windows"
    return "Unknown"

def detect_cpu_arch() -> str:
    """检测CPU架构"""
    machine = platform.machine().lower()
    if machine in ["x86_64", "amd64"]:
        return "x86_64"
    elif machine in ["arm64", "aarch64"]:
        return "arm64"
    return machine

def detect_gpu() -> Dict[str, Optional[str]]:
    """检测GPU类型与可用性"""
    gpu_info = {
        "available": False,
        "type": None,
        "device_name": None,
    }

    # Try NVIDIA GPU (CUDA)
    try:
        import subprocess
        result = subprocess.run(
            ["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0:
            gpu_info["available"] = True
            gpu_info["type"] = "NVIDIA CUDA"
            gpu_info["device_name"] = result.stdout.strip()
            return gpu_info
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Try Apple Metal (M1/M2/M3)
    if platform.system() == "Darwin" and platform.machine() == "arm64":
        try:
            import torch
            if torch.backends.mps.is_available():
                gpu_info["available"] = True
                gpu_info["type"] = "Apple MPS"
                gpu_info["device_name"] = "Apple Silicon GPU"
                return gpu_info
        except ImportError:
            pass

    return gpu_info

def detect_python_version() -> str:
    """检测Python版本"""
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"

def detect_memory() -> Optional[int]:
    """检测系统内存（GB）"""
    try:
        import psutil
        return round(psutil.virtual_memory().total / (1024**3))
    except ImportError:
        return None

def recommend_setup_doc(os_type: str, cpu_arch: str, gpu_available: bool) -> str:
    """推荐配置文档"""
    if os_type == "macOS":
        if cpu_arch == "x86_64":
            return "docs/cross-platform/setup-macos-intel.md"
        elif cpu_arch == "arm64":
            return "docs/cross-platform/setup-macos-arm64.md"
    elif os_type == "Linux":
        return "docs/cross-platform/setup-linux.md"
    elif os_type == "Windows":
        # TODO: Detect WSL2 vs native
        return "docs/cross-platform/setup-windows-wsl2.md"

    return "docs/cross-platform/troubleshooting.md"

def main():
    """主函数"""
    print("=" * 60)
    print("环境检测结果")
    print("=" * 60)

    os_type = detect_os()
    cpu_arch = detect_cpu_arch()
    python_version = detect_python_version()
    gpu_info = detect_gpu()
    memory_gb = detect_memory()

    print(f"\n操作系统: {os_type} {platform.release()}")
    print(f"CPU架构: {cpu_arch}")
    print(f"Python版本: {python_version}")

    if memory_gb:
        print(f"内存: {memory_gb} GB")

    if gpu_info["available"]:
        print(f"\nGPU: ✅ 检测到 {gpu_info['type']}")
        print(f"设备名称: {gpu_info['device_name']}")
    else:
        print(f"\nGPU: ❌ 未检测到（将使用CPU模式）")

    recommended_doc = recommend_setup_doc(os_type, cpu_arch, gpu_info["available"])
    print(f"\n推荐配置文档: {recommended_doc}")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
```

**Estimated Time**: 1-2 hours per script (6-12 hours total for T014-T020)

---

#### Medium Priority Foundation Tasks (T022-T032)

**T022-T028: Cross-Platform Setup Guides**

These are **documentation tasks** - can be parallelized across team members.

**Template for each OS guide**:

```markdown
# [OS Name] 环境配置指南

**适用于**: [OS Version]
**预计时间**: 30-60分钟
**前置要求**: [Prerequisites]

## 环境概览

- **操作系统**: [OS Details]
- **CPU架构**: [x86_64/arm64]
- **GPU支持**: [Yes/No, details]
- **Python版本**: 3.9+ (推荐3.11)

## 安装步骤

### 1. 安装Python

[OS-specific Python installation steps]

### 2. 安装uv包管理器

[OS-specific uv installation steps]

### 3. 克隆项目并创建虚拟环境

[Standard steps]

### 4. 安装依赖

[OS-specific dependency installation, including GPU drivers if applicable]

### 5. 验证安装

[Validation commands]

## 常见问题

### 问题1: [Common Issue]
- **症状**: [Description]
- **原因**: [Root cause]
- **解决**: [Solution]

[Repeat for 3-5 common issues]

## 下一步

- 继续学习: [link to stage3 intro]
- 运行首个项目: [link to quickstart]
- 遇到问题？查看[故障恢复清单](troubleshooting.md)
```

**Estimated Time**: 1-2 hours per guide (6-12 hours total for 6 guides + troubleshooting)

---

**T029-T032: Auxiliary Documentation**

These provide essential context for learners.

**Key files**:
- `docs/glossary.md`: ≥15 terms with Chinese/English equivalents
- `docs/prerequisites.md`: Math/Python requirements + external learning resources
- `docs/learning-path.md`: Milestone checklist, time estimates
- `docs/framework-comparison.md`: PyTorch vs TensorFlow comparison table

**Estimated Time**: 3-4 hours total

---

## 🚀 Quick Start Commands

### For Single Developer (Continue from T007)

```bash
cd /Users/hanlinqi/Desktop/Code/AICode/py_ai_tutorial

# T007: Create CI/CD config
mkdir -p .github/workflows
# [Copy CI/CD YAML content above to .github/workflows/ci.yml]

# T008: Create offline directories
mkdir -p offline/{stage3-data,stage4-data,stage5-data,stage4-models}
# [Create offline/README.md]

# T009: Git commit
git add .
git commit -m "feat: 完成项目基础设置

- 配置项目结构与依赖管理
- 配置MkDocs文档系统
- 配置CI/CD流水线
- 创建离线数据目录

Co-authored-by: Claude <claude@anthropic.com>"
git push origin 002-ai-tutorial-stages

# Start Phase 2: Foundation
# T010: Create stages.yaml
mkdir -p configs/content
# [Create configs/content/stages.yaml with content above]

# Continue with remaining Foundation tasks...
```

### For Team (3 Developers, Day 1 Morning)

**All devs**: Sync on branch and pull latest
```bash
git checkout 002-ai-tutorial-stages
git pull origin 002-ai-tutorial-stages
```

**Dev A (Foundation Lead)**:
```bash
# T007-T009: Finalize setup
# [Create CI/CD, offline dirs, git commit]

# T010-T013: Create YAML configs
mkdir -p configs/content
# [Create all 4 YAML files]
```

**Dev B (Content Creator 1)**:
```bash
# T033-T036: Start Module M01
mkdir -p docs/stage3/01-scientific-computing
mkdir -p notebooks/stage3
# [Create README.md + 3 notebooks]
```

**Dev C (Content Creator 2)**:
```bash
# T029-T032: Auxiliary docs
# [Create glossary, prerequisites, learning path, framework comparison]

# T016-T017: Project templates
mkdir -p templates/project-template
# [Create template structure]
```

---

## 📊 Progress Tracking

### How to Mark Tasks Complete

Update `specs/002-ai-tutorial-stages/tasks.md`:

```diff
-- [ ] T001 创建项目根目录结构
+- [X] T001 创建项目根目录结构
```

### How to Track Your Progress

Create a daily log:

```bash
# Create progress log
cat > PROGRESS.md << 'EOF'
# Implementation Progress Log

## 2025-11-05
- ✅ T001-T006: Completed initial setup
- ⏳ T007-T009: In progress
- 📝 Next: Foundation phase (T010-T032)

## [Date]
- [Tasks completed]
- [Blockers encountered]
- [Next steps]
EOF
```

---

## 🎓 Learning Resources (for Implementers)

### Python Best Practices
- [PEP 8 Style Guide](https://pep8.org/)
- [Type Hints (PEP 484)](https://peps.python.org/pep-0484/)
- [Python Docstring Conventions](https://peps.python.org/pep-0257/)

### MkDocs Material
- [MkDocs Material Documentation](https://squidfunk.github.io/mkdocs-material/)
- [MkDocs Jupyter Plugin](https://github.com/danielfrg/mkdocs-jupyter)

### AI/ML References (for content creation)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
- [LangChain Documentation](https://python.langchain.com/)

---

## ⚠️ Known Issues & Solutions

### Issue 1: MkDocs YAML Warnings

**Symptom**: YAML warnings about unresolved tags in `mkdocs.yml`

**Cause**: IDE doesn't recognize MkDocs-specific YAML tags

**Solution**: These are safe to ignore - MkDocs will process them correctly. Alternatively, suppress warnings in IDE settings.

### Issue 2: uv Installation Fails

**Symptom**: `curl` command fails or uv not found

**Solution**: Use alternative installation:
```bash
pip install uv
# or
pipx install uv
```

### Issue 3: Large Data Files in Git

**Symptom**: Git complains about file size when committing data

**Solution**: Ensure `.gitignore` excludes data files:
```gitignore
data/
*.parquet
*.h5
*.pth
```

---

## 📞 Getting Help

- **Spec Questions**: Review `specs/002-ai-tutorial-stages/spec.md`
- **Technical Decisions**: Review `specs/002-ai-tutorial-stages/research.md`
- **Data Model**: Review `specs/002-ai-tutorial-stages/data-model.md`
- **API Contracts**: Review `specs/002-ai-tutorial-stages/contracts/`
- **Task List**: Review `specs/002-ai-tutorial-stages/tasks.md`

---

## ✅ Definition of Done (MVP)

### Phase 1: Setup
- [X] Project structure created
- [X] pyproject.toml configured
- [X] MkDocs configured
- [X] README.md complete
- [ ] CI/CD configured
- [ ] Git initialized with first commit

### Phase 2: Foundation
- [ ] All 4 YAML entity configs created
- [ ] Core scripts implemented (env detection, data verification, validation)
- [ ] All 6 OS setup guides complete
- [ ] Auxiliary docs complete (glossary, prerequisites, learning path)

### Phase 3: User Story 1 (MVP)
- [ ] All 4 Stage 3 module tutorials complete (docs + notebooks)
- [ ] Stage 3 data download scripts working
- [ ] All 9 Stage 3 projects complete and tested
- [ ] Evaluation system working (rubrics, metrics, eval scripts)
- [ ] At least 3 projects verified on 2+ different OS platforms
- [ ] Documentation buildable and deployable

**MVP Success Criteria**:
- ✅ Learner can configure environment on any OS in <60 minutes
- ✅ Learner can complete Stage 3 projects with CPU only
- ✅ Project outputs match expected metric ranges (±5%)
- ✅ Documentation site builds without errors
- ✅ CI/CD pipeline passes

---

**Good luck with implementation! Feel free to adjust priorities based on your team's strengths and project needs.** 🚀
