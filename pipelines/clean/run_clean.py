import sys
from pathlib import Path

# 添加項目根目錄到 Python 路徑
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.io.readers import read_layer_tables
from src.io.writers import write_parquet
from src.transforms.clean_sales import clean_sales
from src.transforms.clean_traffic import clean_traffic
from src.transforms.clean_weather import clean_weather
from src.utils.config import load_yaml


def main() -> None:
    paths = load_yaml("configs/paths.yaml")["paths"]
    raw = read_layer_tables(paths["raw_dir"])
    cleaners = {
        "fact_hourly_sales": clean_sales,
        "fact_store_traffic": clean_traffic,
        "fact_weather_env": clean_weather,
    }
    for table, df in raw.items():
        fn = cleaners.get(table, lambda x: x)
        write_parquet(fn(df), f"{paths['clean_dir']}/{table}.parquet")


if __name__ == "__main__":
    main()
