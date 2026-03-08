import sys
from pathlib import Path

# 添加項目根目錄到 Python 路徑
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.modeling.evaluator import run_evaluation


def main() -> None:
    run_evaluation("configs/paths.yaml")


if __name__ == "__main__":
    main()
