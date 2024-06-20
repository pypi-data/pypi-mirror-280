import logging
from pathlib import Path


def setup_logging(log_file: Path, *, debug: bool) -> None:
    """Configure logging and create output folder."""
    log_file.parent.mkdir(exist_ok=True, parents=True)
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG if debug else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        force=True,
    )
