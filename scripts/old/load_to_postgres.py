import pandas as pd
from sqlalchemy import create_engine

# Load transformed datasets into PostgreSQL
# Called in run_pipeline() as the final step
# Overwrites each table with cleaned data

def load_to_postgresql(attendances_clean, wait_time_clean, bor_clean, merged_df):
    # Database connection parameters
    DB_USER = "postgres"
    DB_PASSWORD = "admin"
    DB_HOST = "localhost"
    DB_PORT = "5432"
    DB_NAME = "hospital_data"

    # Create a SQLAlchemy engine for connecting to PostgreSQL
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    # Load each cleaned dataset into its corresponding PostgreSQL table
    # Replace existing tables if they already exist
    attendances_clean.to_sql("attendances", engine, if_exists="replace", index=False)
    wait_time_clean.to_sql("wait_times", engine, if_exists="replace", index=False)
    bor_clean.to_sql("bed_occupancy", engine, if_exists="replace", index=False)
    merged_df.to_sql("er_summary", engine, if_exists="replace", index=False)

