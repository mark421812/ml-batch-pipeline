import pandas as pd


def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    out = df.drop_duplicates().copy()
    # TODO: enforce dtypes + stockout-aware rules
    return out
