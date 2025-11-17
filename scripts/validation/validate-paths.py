#!/usr/bin/env python3
"""
路径引用验证脚本 (Path Reference Validation Script)

验证YAML配置文件中引用的所有文件路径是否存在。

Usage:
    python scripts/validation/validate-paths.py
    python scripts/validation/validate-paths.py --config-dir configs/content --root-dir .
    python scripts/validation/validate-paths.py --verbose
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Any
import yaml


class PathValidator:
    """路径验证器"""

    def __init__(self, config_dir: Path, root_dir: Path, verbose: bool = False):
        self.config_dir = config_dir
        self.root_dir = root_dir
        self.verbose = verbose
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.checked_paths: List[Path] = []

    def load_yaml(self, file_path: Path) -> Dict:
        """加载YAML文件"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return yaml.safe_load(f)
        except Exception as e:
            self.errors.append(f"❌ 无法加载{file_path.name}: {e}")
            return {}

    def check_path(self, path_str: str, entity_id: str, field_name: str, required: bool = True) -> bool:
        """检查路径是否存在"""
        if not path_str:
            if required:
                self.errors.append(f"❌ {entity_id}: {field_name} 为空")
            return False

        # 将相对路径转换为绝对路径
        full_path = self.root_dir / path_str
        self.checked_paths.append(full_path)

        if not full_path.exists():
            if required:
                self.errors.append(f"❌ {entity_id}: {field_name} 路径不存在: {path_str}")
            else:
                self.warnings.append(f"⚠️  {entity_id}: {field_name} 路径不存在: {path_str} (可选)")
            return False

        if self.verbose:
            print(f"   ✅ {entity_id}: {field_name} → {path_str}")
        return True

    def validate_modules(self) -> bool:
        """验证模块中的路径引用"""
        print("🔍 验证模块路径引用...")

        modules_file = self.config_dir / "modules.yaml"
        if not modules_file.exists():
            self.warnings.append(f"⚠️  modules.yaml 不存在")
            return True

        config = self.load_yaml(modules_file)
        modules = config.get("modules", [])

        if not modules:
            self.warnings.append(f"⚠️  modules.yaml 为空")
            return True

        path_count = 0
        for module in modules:
            module_id = module.get("id", "UNKNOWN")

            # 检查 content_path (必需)
            if "content_path" in module:
                self.check_path(module["content_path"], module_id, "content_path", required=True)
                path_count += 1

            # 检查 notebook_paths (可选)
            if "notebook_paths" in module:
                for nb_path in module["notebook_paths"]:
                    self.check_path(nb_path, module_id, "notebook_paths", required=False)
                    path_count += 1

        print(f"   ✅ 验证了 {len(modules)} 个模块，{path_count} 个路径")
        return len(self.errors) == 0

    def validate_projects(self) -> bool:
        """验证项目中的路径引用"""
        print("🔍 验证项目路径引用...")

        projects_file = self.config_dir / "projects.yaml"
        if not projects_file.exists():
            self.warnings.append(f"⚠️  projects.yaml 不存在")
            return True

        config = self.load_yaml(projects_file)
        projects = config.get("projects", [])

        if not projects:
            self.warnings.append(f"⚠️  projects.yaml 为空")
            return True

        path_count = 0
        for project in projects:
            project_id = project.get("id", "UNKNOWN")

            # 检查 notebook_path (可选)
            if "notebook_path" in project:
                self.check_path(project["notebook_path"], project_id, "notebook_path", required=False)
                path_count += 1

            # 检查 script_path (可选)
            if "script_path" in project:
                self.check_path(project["script_path"], project_id, "script_path", required=False)
                path_count += 1

            # 检查 readme_path (必需)
            if "readme_path" in project:
                self.check_path(project["readme_path"], project_id, "readme_path", required=True)
                path_count += 1

            # 检查 project_dir (必需)
            if "project_dir" in project:
                self.check_path(project["project_dir"], project_id, "project_dir", required=False)
                path_count += 1

        print(f"   ✅ 验证了 {len(projects)} 个项目，{path_count} 个路径")
        return len(self.errors) == 0

    def validate_datasets(self) -> bool:
        """验证数据集中的路径引用"""
        print("🔍 验证数据集路径引用...")

        datasets_file = self.config_dir / "datasets.yaml"
        if not datasets_file.exists():
            self.warnings.append(f"⚠️  datasets.yaml 不存在")
            return True

        config = self.load_yaml(datasets_file)
        datasets = config.get("datasets", [])

        if not datasets:
            self.warnings.append(f"⚠️  datasets.yaml 为空")
            return True

        path_count = 0
        for dataset in datasets:
            dataset_id = dataset.get("id", "UNKNOWN")

            # 检查 local_path (可选，因为数据可能还未下载)
            if "local_path" in dataset:
                self.check_path(dataset["local_path"], dataset_id, "local_path", required=False)
                path_count += 1

            # 检查 offline_package (可选)
            if "offline_package" in dataset:
                self.check_path(dataset["offline_package"], dataset_id, "offline_package", required=False)
                path_count += 1

        print(f"   ✅ 验证了 {len(datasets)} 个数据集，{path_count} 个路径")
        return len(self.errors) == 0

    def validate_all(self) -> bool:
        """验证所有路径引用"""
        print("=" * 60)
        print("📋 路径引用验证")
        print("=" * 60)

        results = [
            self.validate_modules(),
            self.validate_projects(),
            self.validate_datasets(),
        ]

        return all(results)

    def print_summary(self):
        """打印验证摘要"""
        print("\n" + "=" * 60)
        print("📊 验证摘要")
        print("=" * 60)

        print(f"✅ 检查的路径总数: {len(self.checked_paths)}")

        if self.warnings:
            print(f"\n⚠️  警告数量: {len(self.warnings)}")
            for warning in self.warnings:
                print(f"   {warning}")

        if self.errors:
            print(f"\n❌ 错误数量: {len(self.errors)}")
            for error in self.errors:
                print(f"   {error}")
            print("\n❌ 路径验证失败！")
            return False
        else:
            print("\n✅ 所有必需路径验证通过！")
            return True


def main():
    parser = argparse.ArgumentParser(description="验证YAML配置文件中的路径引用")
    parser.add_argument(
        "--config-dir",
        type=Path,
        default=Path("configs/content"),
        help="配置文件目录 (默认: configs/content)",
    )
    parser.add_argument(
        "--root-dir",
        type=Path,
        default=Path("."),
        help="项目根目录 (默认: .)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="显示详细信息",
    )

    args = parser.parse_args()

    # 转换为绝对路径
    config_dir = args.config_dir.resolve()
    root_dir = args.root_dir.resolve()

    # 检查配置目录是否存在
    if not config_dir.exists():
        print(f"❌ 配置目录不存在: {config_dir}")
        sys.exit(1)

    # 创建验证器并运行验证
    validator = PathValidator(config_dir, root_dir, args.verbose)
    success = validator.validate_all()
    validator.print_summary()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
