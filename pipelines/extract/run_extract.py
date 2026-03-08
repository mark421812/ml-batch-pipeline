from src.io.readers import load_all_sources
from src.io.writers import write_parquet
from src.utils.config import load_yaml
from src.utils.logging import get_logger

logger = get_logger(__name__)


def main() -> None:
    paths = load_yaml("configs/paths.yaml")["paths"]
    tables = load_all_sources()
    for name, df in tables.items():
        write_parquet(df, f"{paths['raw_dir']}/{name}.parquet")
        logger.info("extract done: %s", name)


if __name__ == "__main__":
    main()
