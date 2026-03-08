import pandas as pd


def has_duplicate_keys(df: pd.DataFrame, keys: list[str]) -> bool:
    if df.empty:
        return False
    return bool(df.duplicated(keys).any())
