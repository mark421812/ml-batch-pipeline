from src.modeling.trainer import train_tft


def main() -> None:
    train_tft("configs/paths.yaml", "configs/train.yaml")


if __name__ == "__main__":
    main()
