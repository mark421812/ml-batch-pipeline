import pytest

pytest.importorskip("numpy")

from src.modeling.metrics import mae, rmse, smape


def test_metrics_basic() -> None:
    assert mae([1, 2], [1, 2]) == 0
    assert rmse([1, 2], [1, 2]) == 0
    assert smape([1, 2], [1, 2]) == 0
