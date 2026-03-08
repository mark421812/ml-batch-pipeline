import pytest

pytest.importorskip("pandas")

from src.io.readers import load_all_sources


def test_load_all_sources_has_7_tables() -> None:
    tables = load_all_sources()
    assert len(tables) == 7
