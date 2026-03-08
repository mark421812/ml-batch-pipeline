import pandas as pd


def build_modeling_base_tables(feature_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    # TODO: split training/inference with horizon-aware logic
    return feature_df.copy(), feature_df.copy()


def build_tft_dataset_config() -> dict:
    return {
        "target": "sales_qty",
        "group_ids": ["store_id", "product_id"],
        "time_idx": "time_idx",
    }
