import sys
from pathlib import Path

# 添加項目根目錄到 Python 路徑
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.io.readers import read_layer_tables
from src.io.writers import write_parquet
from src.transforms.build_training_features import build_training_features
from src.utils.config import load_yaml


def main() -> None:
    paths = load_yaml("configs/paths.yaml")["paths"]
    clean = read_layer_tables(paths["clean_dir"])
    features = build_training_features(clean)
    write_parquet(features, f"{paths['feature_dir']}/hourly_feature_table.parquet")


if __name__ == "__main__":
    main()
