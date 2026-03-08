import pandas as pd


def to_timestamp(series: pd.Series) -> pd.Series:
    return pd.to_datetime(series, errors="coerce")
