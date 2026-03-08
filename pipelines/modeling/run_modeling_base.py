import sys
from pathlib import Path

# 添加項目根目錄到 Python 路徑
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.io.readers import read_parquet
from src.io.writers import write_parquet
from src.modeling.dataset_builder import build_modeling_base_tables
from src.utils.config import load_yaml


def main() -> None:
    paths = load_yaml("configs/paths.yaml")["paths"]
    feature_df = read_parquet(f"{paths['feature_dir']}/hourly_feature_table.parquet")
    train_df, infer_df = build_modeling_base_tables(feature_df)
    write_parquet(train_df, f"{paths['modeling_dir']}/model_training_hourly_features.parquet")
    write_parquet(infer_df, f"{paths['modeling_dir']}/model_inference_hourly_features.parquet")


if __name__ == "__main__":
    main()
