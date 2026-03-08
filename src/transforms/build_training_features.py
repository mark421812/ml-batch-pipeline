import pandas as pd


def build_training_features(clean_tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """TODO: merge clean tables and generate modeling features."""
    return clean_tables.get("fact_hourly_sales", pd.DataFrame()).copy()
