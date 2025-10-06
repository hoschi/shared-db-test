import sys
from loguru import logger

def setup_logging():
    """
    Set up structured logging for the application.
    """
    logger.remove()
    logger.add(
        sys.stderr,
        format=(
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
            "<level>{message}</level>"
        ),
        level="INFO",
        colorize=True,
    )
    # Example of how to add schema context to logs
    # logger.configure(patcher=lambda record: record["extra"].update(schema=schema_context.get()))
    return logger

# Initialize logger
log = setup_logging()