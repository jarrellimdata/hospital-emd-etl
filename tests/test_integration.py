# tests/test_integration.py
# Checks the entire ETL pipeline end-to-end
# Ensures all components work together correctly

from pipelines.pipeline_w_logging import run_pipeline
from scripts.utils.logger import setup_logger
import pytest

def test_full_pipeline():
    logger = setup_logger(
        name="test_integration_logger", 
        log_file="logs/test_integration.log"
    )
    
    logger.info("Running full pipeline integration test...")

    try:
        run_pipeline(logger=logger)
    except Exception:
        logger.error("Pipeline failed during test.")
        pytest.fail("Pipeline failed during integration test")

