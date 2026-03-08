import sys
from pathlib import Path

# 添加項目根目錄到 Python 路徑
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.modeling.trainer import export_training_metadata


def main() -> None:
    export_training_metadata("configs/paths.yaml")


if __name__ == "__main__":
    main()
