import pandas as pd
from sqlalchemy import create_engine

def load_to_postgresql(attendances_clean, wait_time_clean, bor_clean, merged_df, db_config, logger):
    try:
        # Create engine using DB credentials from config
        engine = create_engine(
            f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"
        )

        # Write each cleaned dataframe to a SQL table
        attendances_clean.to_sql("attendances", engine, if_exists="replace", index=False)
        wait_time_clean.to_sql("wait_times", engine, if_exists="replace", index=False)
        bor_clean.to_sql("bed_occupancy", engine, if_exists="replace", index=False)
        merged_df.to_sql("er_summary", engine, if_exists="replace", index=False)

    except Exception as e:
        logger.error(f"Failed to load data to PostgreSQL: {e}")
        raise
