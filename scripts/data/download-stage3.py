#!/usr/bin/env python3
"""
Stage 3 Dataset Download Script
下载阶段3的9个项目数据集并自动校验

Usage:
    python scripts/data/download-stage3.py [--mirror] [--verify-only]

Options:
    --mirror       使用国内镜像加速下载
    --verify-only  仅校验已下载的数据，不重新下载
    --dataset ID   仅下载指定数据集 (如: DS-S3-P01-HOSPITAL)
"""

import argparse
import hashlib
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional
import urllib.request
import urllib.error
import yaml

# 项目根目录
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "stage3"
CONFIG_FILE = PROJECT_ROOT / "configs" / "content" / "datasets.yaml"


class Colors:
    """Terminal colors for better output"""
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"


def load_datasets() -> List[Dict]:
    """Load dataset configurations from YAML"""
    if not CONFIG_FILE.exists():
        print(f"{Colors.RED}✗ Error: Config file not found: {CONFIG_FILE}{Colors.ENDC}")
        sys.exit(1)
    
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    # Filter only Stage 3 datasets
    stage3_datasets = [
        ds for ds in config.get('datasets', [])
        if ds.get('stage_id') == 'stage3'
    ]
    
    return stage3_datasets


def calculate_sha256(file_path: Path, chunk_size: int = 8192) -> str:
    """Calculate SHA256 checksum of a file"""
    sha256 = hashlib.sha256()
    
    with open(file_path, 'rb') as f:
        while chunk := f.read(chunk_size):
            sha256.update(chunk)
    
    return sha256.hexdigest()


def verify_checksum(file_path: Path, expected_checksum: str) -> bool:
    """Verify file checksum"""
    if not file_path.exists():
        return False
    
    actual_checksum = calculate_sha256(file_path)
    return actual_checksum == expected_checksum


def download_file(url: str, dest_path: Path, desc: str = "") -> bool:
    """Download a file with progress indicator"""
    try:
        print(f"{Colors.BLUE}→ Downloading: {desc or url}{Colors.ENDC}")
        print(f"  URL: {url}")
        print(f"  Destination: {dest_path}")
        
        # Create parent directory
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Download file
        def reporthook(count, block_size, total_size):
            if total_size > 0:
                percent = count * block_size * 100 / total_size
                size_mb = total_size / (1024 * 1024)
                downloaded_mb = count * block_size / (1024 * 1024)
                sys.stdout.write(f"\r  Progress: {downloaded_mb:.1f}/{size_mb:.1f} MB ({percent:.1f}%)")
                sys.stdout.flush()
        
        urllib.request.urlretrieve(url, dest_path, reporthook)
        print()  # New line after progress
        return True
        
    except urllib.error.URLError as e:
        print(f"\n{Colors.RED}✗ Download failed: {e}{Colors.ENDC}")
        return False
    except Exception as e:
        print(f"\n{Colors.RED}✗ Unexpected error: {e}{Colors.ENDC}")
        return False


def process_dataset(dataset: Dict, use_mirror: bool = False, verify_only: bool = False) -> bool:
    """Process a single dataset (download and verify)"""
    ds_id = dataset['id']
    ds_name = dataset['name']
    
    print(f"\n{Colors.BOLD}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}Dataset: {ds_name} ({ds_id}){Colors.ENDC}")
    print(f"{Colors.BOLD}{'='*60}{Colors.ENDC}")
    
    # Get file info
    files = dataset.get('files', [])
    if not files:
        print(f"{Colors.YELLOW}⚠ Warning: No files defined for this dataset{Colors.ENDC}")
        return True
    
    source = dataset.get('source', {})
    source_type = source.get('type')
    
    # Handle different source types
    if source_type == 'synthetic':
        print(f"{Colors.BLUE}ℹ Source: Synthetic data (needs to be generated){Colors.ENDC}")
        print(f"{Colors.YELLOW}⚠ This dataset is not yet available for automatic download{Colors.ENDC}")
        return True
    
    elif source_type == 'public':
        base_url = source.get('mirror_url') if use_mirror else source.get('url')
        if not base_url:
            print(f"{Colors.YELLOW}⚠ No download URL available{Colors.ENDC}")
            return True
    
    else:
        print(f"{Colors.YELLOW}⚠ Source type '{source_type}' not supported for automatic download{Colors.ENDC}")
        return True
    
    success = True
    for file_info in files:
        filename = file_info['filename']
        expected_checksum = file_info.get('checksum_sha256', '').replace('PLACEHOLDER_CHECKSUM_TO_BE_GENERATED', '')
        size_mb = file_info.get('size_mb', 0)
        
        dest_path = DATA_DIR / filename
        
        # Check if file exists and verify
        if dest_path.exists():
            print(f"\n{Colors.BLUE}✓ File exists: {filename}{Colors.ENDC}")
            
            if expected_checksum:
                print(f"  Verifying checksum...")
                if verify_checksum(dest_path, expected_checksum):
                    print(f"  {Colors.GREEN}✓ Checksum verified{Colors.ENDC}")
                else:
                    print(f"  {Colors.RED}✗ Checksum mismatch!{Colors.ENDC}")
                    if not verify_only:
                        print(f"  Re-downloading...")
                        dest_path.unlink()
                    else:
                        success = False
                        continue
            else:
                print(f"  {Colors.YELLOW}⚠ No checksum available (placeholder){Colors.ENDC}")
        
        # Download if not exists or checksum failed
        if not dest_path.exists() and not verify_only:
            # Construct download URL
            if source_type == 'public':
                # For public datasets, URL might be a base or direct link
                download_url = base_url if base_url.endswith(filename) else f"{base_url}/{filename}"
            else:
                print(f"{Colors.YELLOW}⚠ Cannot construct download URL{Colors.ENDC}")
                continue
            
            # Download
            desc = f"{ds_name} - {filename} ({size_mb}MB)"
            if not download_file(download_url, dest_path, desc):
                success = False
                continue
            
            # Verify after download
            if expected_checksum:
                print(f"  Verifying downloaded file...")
                if verify_checksum(dest_path, expected_checksum):
                    print(f"  {Colors.GREEN}✓ Download verified{Colors.ENDC}")
                else:
                    print(f"  {Colors.RED}✗ Downloaded file checksum mismatch!{Colors.ENDC}")
                    success = False
        
        elif verify_only and not dest_path.exists():
            print(f"{Colors.RED}✗ File not found: {filename}{Colors.ENDC}")
            success = False
    
    return success


def main():
    parser = argparse.ArgumentParser(description='Download Stage 3 datasets')
    parser.add_argument('--mirror', action='store_true', help='Use mirror URLs (faster in China)')
    parser.add_argument('--verify-only', action='store_true', help='Verify existing files without downloading')
    parser.add_argument('--dataset', type=str, help='Download specific dataset by ID')
    
    args = parser.parse_args()
    
    print(f"{Colors.BOLD}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}Stage 3 Dataset Download & Verification Tool{Colors.ENDC}")
    print(f"{Colors.BOLD}{'='*60}{Colors.ENDC}")
    print(f"Data directory: {DATA_DIR}")
    print(f"Mirror mode: {'Enabled' if args.mirror else 'Disabled'}")
    print(f"Verify only: {'Yes' if args.verify_only else 'No'}")
    
    # Load datasets
    datasets = load_datasets()
    print(f"\nFound {len(datasets)} Stage 3 datasets in configuration")
    
    # Filter by specific dataset if requested
    if args.dataset:
        datasets = [ds for ds in datasets if ds['id'] == args.dataset]
        if not datasets:
            print(f"{Colors.RED}✗ Dataset not found: {args.dataset}{Colors.ENDC}")
            sys.exit(1)
        print(f"Processing only: {args.dataset}")
    
    # Ensure data directory exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    # Process each dataset
    success_count = 0
    failed_datasets = []
    
    for dataset in datasets:
        try:
            if process_dataset(dataset, args.mirror, args.verify_only):
                success_count += 1
            else:
                failed_datasets.append(dataset['id'])
        except Exception as e:
            print(f"{Colors.RED}✗ Error processing {dataset['id']}: {e}{Colors.ENDC}")
            failed_datasets.append(dataset['id'])
    
    # Summary
    print(f"\n{Colors.BOLD}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}Summary{Colors.ENDC}")
    print(f"{Colors.BOLD}{'='*60}{Colors.ENDC}")
    print(f"Total datasets: {len(datasets)}")
    print(f"{Colors.GREEN}Successful: {success_count}{Colors.ENDC}")
    
    if failed_datasets:
        print(f"{Colors.RED}Failed: {len(failed_datasets)}{Colors.ENDC}")
        print(f"Failed datasets: {', '.join(failed_datasets)}")
        sys.exit(1)
    else:
        print(f"\n{Colors.GREEN}✓ All datasets processed successfully!{Colors.ENDC}")
        sys.exit(0)


if __name__ == '__main__':
    main()
