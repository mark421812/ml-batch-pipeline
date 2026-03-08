from pathlib import Path
from src.modeling.metrics import mae, rmse, smape


def run_evaluation(paths_config: str) -> None:
    # TODO: load predictions/labels and produce layered reports
    _ = (mae([0], [0]), rmse([0], [0]), smape([0], [0]))
    Path("artifacts/reports").mkdir(parents=True, exist_ok=True)
    Path("artifacts/reports/evaluation_summary.txt").write_text("evaluation placeholder\n")
