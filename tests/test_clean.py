import pytest

pd = pytest.importorskip("pandas")

from src.transforms.clean_sales import clean_sales


def test_clean_sales_deduplicate() -> None:
    df = pd.DataFrame({"x": [1, 1]})
    out = clean_sales(df)
    assert len(out) == 1
