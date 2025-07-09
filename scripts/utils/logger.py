# scripts/utils/logger.py
import logging
import os

def setup_logger(name="etl_logger", log_file="logs/pipeline.log", level=logging.INFO):
    os.makedirs(os.path.dirname(log_file), exist_ok=True) # Ensure the logs directory exists

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicated handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger


