# tests/test_extract.py

import os
import pandas as pd
import yaml
from scripts.new.extract_data_w_logging import extract_data

class DummyLogger:
    def info(self, msg): pass
    def warning(self, msg): pass
    def error(self, msg): pass

def check_files_exist(base_dir, files):
    missing = [f for f in files if not os.path.isfile(os.path.join(base_dir, f))]
    if missing:
        raise FileNotFoundError("Missing test files:\n" + "\n".join(missing))

def test_extract_valid_file():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "raw"))

    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    expected_files = list(config['data_paths'].values())
    check_files_exist(base_dir, expected_files)

    paths = {
        key: os.path.join(base_dir, filename)
        for key, filename in config['data_paths'].items()
    }

    logger = DummyLogger()
    dfs = extract_data(paths, logger)

    assert all(isinstance(df, pd.DataFrame) for df in dfs.values())
    assert "Date" in dfs["attendances"].columns


