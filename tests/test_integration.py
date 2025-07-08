# tests/test_integration.py
from pipelines.pipeline_w_logging import run_pipeline
import pytest

def test_full_pipeline():
    # run_pipeline() references the config.yaml file directly
    try:
        run_pipeline()
    except Exception:
        pytest.fail("Pipeline failed during integration test")
