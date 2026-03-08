from src.modeling.trainer import export_training_metadata


def main() -> None:
    export_training_metadata("configs/paths.yaml")


if __name__ == "__main__":
    main()
