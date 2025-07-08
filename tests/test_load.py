# tests/test_load.py

import pandas as pd
from scripts.new.load_to_postgres_w_logging import load_to_postgresql

class DummyLogger:
    def info(self, msg): pass
    def error(self, msg): pass

def test_load_to_postgres(monkeypatch):
    # Create dummy DataFrames
    df = pd.DataFrame({
        "date": ["2024-01-01"],
        "hospital": ["Hospital A"],
        "patient_count": [10]
    })

    db_config = {
        "user": "postgres",
        "password": "admin",
        "host": "localhost",
        "port": "5432",
        "dbname": "hospital_data"
    }

    logger = DummyLogger()

    # Skip actual database load using monkeypatch (if testing locally)
    def fake_to_sql(*args, **kwargs): return None
    monkeypatch.setattr(pd.DataFrame, "to_sql", fake_to_sql)

    load_to_postgresql(df, df, df, df, db_config, logger)
