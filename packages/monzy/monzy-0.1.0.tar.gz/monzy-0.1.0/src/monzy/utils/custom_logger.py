import json
import sys

from loguru import logger as loguru_base_logger


def logger_patch(record):
    """Patch to customise format of logging with Loguru module.

    Args:
        record (dict): Dict of logging data
    """
    record["extra"]["serialized"] = json.dumps(
        {
            "timestamp": str(record["time"]),
            "line_number": record["line"],
            "level": record["level"].name,
            "message": record["message"],
            "extra": record["extra"],
        }
    )


loguru_base_logger.remove(0)
logger = loguru_base_logger.patch(logger_patch)
logger.add(sys.stderr, format="{extra[serialized]}")
