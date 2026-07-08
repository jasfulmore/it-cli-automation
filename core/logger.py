import logging
from pathlib import Path

# create logs directory if it doesnt exist
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

log_file = log_dir / "it-cli.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("it-cli")