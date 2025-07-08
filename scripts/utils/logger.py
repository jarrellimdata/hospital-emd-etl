import logging
import os

def setup_logger(name="etl_logger", log_file="logs/pipeline.log", level=logging.INFO):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)  # Make sure logs/ exists

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        fh = logging.FileHandler(log_file)
        fh.setLevel(level)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger
