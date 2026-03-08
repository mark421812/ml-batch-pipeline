#!/usr/bin/env python3
"""
臨時包裝器：運行管道而無需完整安裝 src 包
"""
import sys
from pathlib import Path

# 添加項目根目錄到 Python 路徑
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# 現在可以導入 src 模塊
from src.io.readers import load_all_sources
from src.io.writers import write_parquet
from src.utils.config import load_yaml
from src.utils.logging import get_logger

logger = get_logger(__name__)


def run_extract() -> None:
    """運行 extract 管道"""
    print("🚀 開始運行 extract 管道...")
    try:
        paths = load_yaml("configs/paths.yaml")["paths"]
        tables = load_all_sources()
        for name, df in tables.items():
            write_parquet(df, f"{paths['raw_dir']}/{name}.parquet")
            logger.info("extract done: %s", name)
        print("✅ Extract 完成")
    except Exception as e:
        print(f"❌ 錯誤: {e}")
        sys.exit(1)


if __name__ == "__main__":
    run_extract()
