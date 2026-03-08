import pandas as pd


def build_calendar_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    # TODO: month_no/day_of_month/week_of_year/season/pre-post holiday
    return out
