# tests/test_load.py

import os
import pandas as pd
from dotenv import load_dotenv
from scripts.new.load_to_postgres_w_logging import load_to_postgresql

# Dummy logger for silent test runs
class DummyLogger:
    def info(self, msg): pass
    def error(self, msg): pass

def test_load_to_postgres(monkeypatch):
    load_dotenv()  # Load DB credentials from .env

    # Create dummy DataFrame to simulate cleaned data
    df = pd.DataFrame({
        "date": ["2024-01-01"],
        "hospital": ["Hospital A"],
        "patient_count": [10]
    })

    # Pull database config from environment
    db_config = {
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
        "dbname": os.getenv("DB_NAME")
    }

    logger = DummyLogger()

    # Monkeypatch .to_sql so no DB connection is made
    monkeypatch.setattr(pd.DataFrame, "to_sql", lambda *args, **kwargs: None)

    # Run the load function
    load_to_postgresql(df, df, df, df, db_config, logger)


