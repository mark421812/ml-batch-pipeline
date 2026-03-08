import pandas as pd


def clean_traffic(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    out = df.drop_duplicates().copy()
    # TODO: member_txn_ratio + quality checks
    return out
