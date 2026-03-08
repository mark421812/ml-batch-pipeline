from pathlib import Path
import json


def train_tft(paths_config: str, train_config: str) -> None:
    # TODO: implement Lightning trainer + early stopping + checkpoints
    Path("artifacts/checkpoints").mkdir(parents=True, exist_ok=True)


def export_training_metadata(paths_config: str) -> None:
    Path("artifacts/metadata").mkdir(parents=True, exist_ok=True)
    payload = {"status": "placeholder", "notes": "fill after training implementation"}
    with open("artifacts/metadata/training_metadata.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
