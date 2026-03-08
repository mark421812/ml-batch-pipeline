from pathlib import Path
import pandas as pd


def load_all_sources() -> dict[str, pd.DataFrame]:
    """TODO: replace sample loading with real data connectors."""
    names = [
        "fact_hourly_sales",
        "fact_store_traffic",
        "fact_weather_env",
        "fact_promotions",
        "dim_product",
        "dim_store",
        "dim_calendar",
    ]
    return {n: pd.DataFrame() for n in names}


def read_parquet(path: str) -> pd.DataFrame:
    return pd.read_parquet(path)


def read_layer_tables(layer_dir: str) -> dict[str, pd.DataFrame]:
    tables = {}
    for fp in Path(layer_dir).glob("*.parquet"):
        tables[fp.stem] = pd.read_parquet(fp)
    return tables
