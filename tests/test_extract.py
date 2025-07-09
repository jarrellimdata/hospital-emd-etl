# tests/test_extract.py
# Tests extract_data() using real config paths and files

import os
import pandas as pd
import yaml
from scripts.new.extract_data_w_logging import extract_data

class DummyLogger:
    def info(self, msg): pass
    def warning(self, msg): pass
    def error(self, msg): pass

def check_files_exist(base_dir, files):
    """Verify that all expected Excel files exist in the raw data directory"""
    missing = [f for f in files if not os.path.isfile(os.path.join(base_dir, f))]
    if missing:
        raise FileNotFoundError("Missing test files:\n" + "\n".join(missing))

def test_extract_valid_file():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "raw"))

    # Load file names from config.yaml
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    expected_files = list(config['data_paths'].values())
    check_files_exist(base_dir, expected_files)

    # Build full paths to the Excel files
    paths = {
        key: os.path.join(base_dir, filename)
        for key, filename in config['data_paths'].items()
    }

    # Extract data
    logger = DummyLogger()
    dfs = extract_data(paths, logger)

    # Assert all extracted objects are DataFrames
    assert all(isinstance(df, pd.DataFrame) for df in dfs.values())

    # Confirm expected column exists in attendances
    assert "Date" in dfs["attendances"].columns



