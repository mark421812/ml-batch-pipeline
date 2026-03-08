import pandas as pd


def add_default_quality_flags(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in ["stockout_flag", "available_for_sale_flag", "listed_flag"]:
        if col not in out.columns:
            out[col] = 1
    return out
