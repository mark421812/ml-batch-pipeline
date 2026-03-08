import pytest

pd = pytest.importorskip("pandas")

from src.modeling.dataset_builder import build_modeling_base_tables


def test_modeling_base_returns_two_frames() -> None:
    df = pd.DataFrame({"a": [1]})
    train_df, infer_df = build_modeling_base_tables(df)
    assert len(train_df) == len(infer_df) == 1
