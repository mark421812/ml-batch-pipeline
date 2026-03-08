import pandas as pd


def clean_weather(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    out = df.drop_duplicates().copy()
    # TODO: normalize weather_type and anomaly checks
    return out
