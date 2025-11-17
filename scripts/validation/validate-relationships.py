#!/usr/bin/env python3
"""
实体关系验证脚本 (Entity Relationship Validation Script)

验证YAML配置文件中实体之间的引用关系完整性。

Usage:
    python scripts/validation/validate-relationships.py
    python scripts/validation/validate-relationships.py --config-dir configs/content
    python scripts/validation/validate-relationships.py --verbose
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Set, Any
import yaml


class RelationshipValidator:
    """关系验证器"""

    def __init__(self, config_dir: Path, verbose: bool = False):
        self.config_dir = config_dir
        self.verbose = verbose
        self.errors: List[str] = []
        self.warnings: List[str] = []

        # 存储实体ID集合
        self.stage_ids: Set[str] = set()
        self.module_ids: Set[str] = set()
        self.project_ids: Set[str] = set()
        self.dataset_ids: Set[str] = set()

        # 存储实体数据
        self.stages: List[Dict] = []
        self.modules: List[Dict] = []
        self.projects: List[Dict] = []
        self.datasets: List[Dict] = []

    def load_yaml(self, file_path: Path) -> Dict:
        """加载YAML文件"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return yaml.safe_load(f)
        except Exception as e:
            self.errors.append(f"❌ 无法加载{file_path.name}: {e}")
            return {}

    def load_all_entities(self):
        """加载所有实体配置"""
        print("🔍 加载实体配置...")

        # 加载stages
        stages_file = self.config_dir / "stages.yaml"
        if stages_file.exists():
            config = self.load_yaml(stages_file)
            self.stages = config.get("stages", [])
            self.stage_ids = {stage["id"] for stage in self.stages if "id" in stage}
            print(f"   ✅ 加载了 {len(self.stages)} 个阶段")

        # 加载modules
        modules_file = self.config_dir / "modules.yaml"
        if modules_file.exists():
            config = self.load_yaml(modules_file)
            self.modules = config.get("modules", [])
            self.module_ids = {module["id"] for module in self.modules if "id" in module}
            print(f"   ✅ 加载了 {len(self.modules)} 个模块")

        # 加载projects
        projects_file = self.config_dir / "projects.yaml"
        if projects_file.exists():
            config = self.load_yaml(projects_file)
            self.projects = config.get("projects", [])
            self.project_ids = {project["id"] for project in self.projects if "id" in project}
            print(f"   ✅ 加载了 {len(self.projects)} 个项目")

        # 加载datasets
        datasets_file = self.config_dir / "datasets.yaml"
        if datasets_file.exists():
            config = self.load_yaml(datasets_file)
            self.datasets = config.get("datasets", [])
            self.dataset_ids = {dataset["id"] for dataset in self.datasets if "id" in dataset}
            print(f"   ✅ 加载了 {len(self.datasets)} 个数据集")

    def validate_stage_references(self) -> bool:
        """验证阶段引用"""
        print("\n🔍 验证阶段引用...")

        has_errors = False

        for stage in self.stages:
            stage_id = stage.get("id", "UNKNOWN")

            # 检查modules引用
            if "modules" in stage:
                for module_id in stage["modules"]:
                    if module_id not in self.module_ids:
                        self.errors.append(f"❌ Stage {stage_id}: 引用的模块不存在: {module_id}")
                        has_errors = True

            # 检查projects引用
            if "projects" in stage:
                for project_id in stage["projects"]:
                    if project_id not in self.project_ids:
                        self.errors.append(f"❌ Stage {stage_id}: 引用的项目不存在: {project_id}")
                        has_errors = True

            # 检查prerequisites引用 (前置阶段)
            if "prerequisites" in stage and stage["prerequisites"]:
                for prereq_id in stage["prerequisites"]:
                    if prereq_id not in self.stage_ids:
                        self.errors.append(f"❌ Stage {stage_id}: 引用的前置阶段不存在: {prereq_id}")
                        has_errors = True

        if not has_errors:
            print("   ✅ 所有阶段引用有效")

        return not has_errors

    def validate_module_references(self) -> bool:
        """验证模块引用"""
        print("\n🔍 验证模块引用...")

        has_errors = False

        for module in self.modules:
            module_id = module.get("id", "UNKNOWN")

            # 检查stage_id引用
            if "stage_id" in module:
                stage_id = module["stage_id"]
                if stage_id not in self.stage_ids:
                    self.errors.append(f"❌ Module {module_id}: 引用的阶段不存在: {stage_id}")
                    has_errors = True

            # 检查prerequisites引用 (前置模块)
            if "prerequisites" in module and module["prerequisites"]:
                for prereq_id in module["prerequisites"]:
                    if prereq_id not in self.module_ids:
                        self.errors.append(f"❌ Module {module_id}: 引用的前置模块不存在: {prereq_id}")
                        has_errors = True

        if not has_errors:
            print("   ✅ 所有模块引用有效")

        return not has_errors

    def validate_project_references(self) -> bool:
        """验证项目引用"""
        print("\n🔍 验证项目引用...")

        has_errors = False

        for project in self.projects:
            project_id = project.get("id", "UNKNOWN")

            # 检查stage_id引用
            if "stage_id" in project:
                stage_id = project["stage_id"]
                if stage_id not in self.stage_ids:
                    self.errors.append(f"❌ Project {project_id}: 引用的阶段不存在: {stage_id}")
                    has_errors = True

            # 检查required_modules引用 (必需模块)
            if "required_modules" in project and project["required_modules"]:
                for module_id in project["required_modules"]:
                    if module_id not in self.module_ids:
                        self.errors.append(f"❌ Project {project_id}: 引用的必需模块不存在: {module_id}")
                        has_errors = True

            # 检查datasets引用
            if "datasets" in project and project["datasets"]:
                for dataset_id in project["datasets"]:
                    if dataset_id not in self.dataset_ids:
                        self.errors.append(f"❌ Project {project_id}: 引用的数据集不存在: {dataset_id}")
                        has_errors = True

        if not has_errors:
            print("   ✅ 所有项目引用有效")

        return not has_errors

    def validate_dataset_references(self) -> bool:
        """验证数据集引用"""
        print("\n🔍 验证数据集引用...")

        has_errors = False

        for dataset in self.datasets:
            dataset_id = dataset.get("id", "UNKNOWN")

            # 检查project_id引用
            if "project_id" in dataset:
                project_id = dataset["project_id"]
                if project_id not in self.project_ids:
                    self.warnings.append(f"⚠️  Dataset {dataset_id}: 引用的项目不存在: {project_id}")
                    # 数据集的project_id是反向引用，可以是警告而不是错误

            # 检查stage_id引用
            if "stage_id" in dataset:
                stage_id = dataset["stage_id"]
                if stage_id not in self.stage_ids:
                    self.errors.append(f"❌ Dataset {dataset_id}: 引用的阶段不存在: {stage_id}")
                    has_errors = True

        if not has_errors:
            print("   ✅ 所有数据集引用有效")

        return not has_errors

    def validate_bidirectional_references(self) -> bool:
        """验证双向引用一致性"""
        print("\n🔍 验证双向引用一致性...")

        has_errors = False

        # 检查stage->modules双向一致性
        for stage in self.stages:
            stage_id = stage.get("id", "UNKNOWN")
            stage_module_ids = set(stage.get("modules", []))

            # 查找声称属于该stage的模块
            actual_module_ids = {m["id"] for m in self.modules if m.get("stage_id") == stage_id}

            # 检查是否有模块未在stage中声明
            unlisted = actual_module_ids - stage_module_ids
            if unlisted:
                self.warnings.append(
                    f"⚠️  Stage {stage_id}: 有模块声称属于该阶段但未被列出: {unlisted}"
                )

            # 检查是否有stage列出的模块实际不属于该stage
            invalid = stage_module_ids - actual_module_ids
            if invalid:
                self.errors.append(
                    f"❌ Stage {stage_id}: 列出的模块不属于该阶段: {invalid}"
                )
                has_errors = True

        # 检查stage->projects双向一致性
        for stage in self.stages:
            stage_id = stage.get("id", "UNKNOWN")
            stage_project_ids = set(stage.get("projects", []))

            # 查找声称属于该stage的项目
            actual_project_ids = {p["id"] for p in self.projects if p.get("stage_id") == stage_id}

            # 检查是否有项目未在stage中声明
            unlisted = actual_project_ids - stage_project_ids
            if unlisted:
                self.warnings.append(
                    f"⚠️  Stage {stage_id}: 有项目声称属于该阶段但未被列出: {unlisted}"
                )

            # 检查是否有stage列出的项目实际不属于该stage
            invalid = stage_project_ids - actual_project_ids
            if invalid:
                self.errors.append(
                    f"❌ Stage {stage_id}: 列出的项目不属于该阶段: {invalid}"
                )
                has_errors = True

        if not has_errors:
            print("   ✅ 双向引用一致性验证通过")

        return not has_errors

    def validate_all(self) -> bool:
        """验证所有关系"""
        print("=" * 60)
        print("📋 实体关系验证")
        print("=" * 60)

        self.load_all_entities()

        results = [
            self.validate_stage_references(),
            self.validate_module_references(),
            self.validate_project_references(),
            self.validate_dataset_references(),
            self.validate_bidirectional_references(),
        ]

        return all(results)

    def print_summary(self):
        """打印验证摘要"""
        print("\n" + "=" * 60)
        print("📊 验证摘要")
        print("=" * 60)

        print(f"📚 实体统计:")
        print(f"   - 阶段: {len(self.stage_ids)}")
        print(f"   - 模块: {len(self.module_ids)}")
        print(f"   - 项目: {len(self.project_ids)}")
        print(f"   - 数据集: {len(self.dataset_ids)}")

        if self.warnings:
            print(f"\n⚠️  警告数量: {len(self.warnings)}")
            for warning in self.warnings:
                print(f"   {warning}")

        if self.errors:
            print(f"\n❌ 错误数量: {len(self.errors)}")
            for error in self.errors:
                print(f"   {error}")
            print("\n❌ 关系验证失败！")
            return False
        else:
            print("\n✅ 所有关系验证通过！")
            return True


def main():
    parser = argparse.ArgumentParser(description="验证YAML配置文件中的实体关系")
    parser.add_argument(
        "--config-dir",
        type=Path,
        default=Path("configs/content"),
        help="配置文件目录 (默认: configs/content)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="显示详细信息",
    )

    args = parser.parse_args()

    # 转换为绝对路径
    config_dir = args.config_dir.resolve()

    # 检查配置目录是否存在
    if not config_dir.exists():
        print(f"❌ 配置目录不存在: {config_dir}")
        sys.exit(1)

    # 创建验证器并运行验证
    validator = RelationshipValidator(config_dir, args.verbose)
    success = validator.validate_all()
    validator.print_summary()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
