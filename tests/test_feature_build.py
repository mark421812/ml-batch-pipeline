import pytest

pd = pytest.importorskip("pandas")

from src.transforms.build_training_features import build_training_features


def test_feature_build_fallback_returns_sales() -> None:
    sales = pd.DataFrame({"sales_qty": [1]})
    out = build_training_features({"fact_hourly_sales": sales})
    assert "sales_qty" in out.columns
