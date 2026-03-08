from pathlib import Path
import pandas as pd


def write_parquet(df: pd.DataFrame, path: str) -> None:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output, index=False)
