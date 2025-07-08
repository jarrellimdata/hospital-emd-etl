import os
import yaml 
from dotenv import load_dotenv

from scripts.utils.logger import setup_logger
from scripts.new.extract_data_w_logging import extract_data
from scripts.new.transform_data import clean_moh_dataset
from scripts.new.load_to_postgres_w_logging import load_to_postgresql

# load environment variables from .env file
load_dotenv() 

# retrieve corresponding database credentials from environment variables
# store in dictionary for easy access
db_config = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "dbname": os.getenv("DB_NAME")
}

def run_pipeline():
    logger = setup_logger()
    logger.info("ETL pipeline started")

    # Load config.yaml to fetch paths and DB credentials
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    raw_data_dir = config.get('raw_data_dir', 'data/raw')
    processed_data_dir = config.get('processed_data_dir', 'data/processed')

    # Use filenames from config under data_paths
    paths = {
        key: os.path.join(raw_data_dir, filename)
        for key, filename in config['data_paths'].items()
    }

    # EXTRACT
    try:
        dataframes = extract_data(paths, logger)
        logger.info("Data extraction completed successfully")
    except Exception:
        logger.error("Pipeline aborted during extraction")
        return

    # TRANSFORM
    cleaned_data = {}
    try:
        for key, df in dataframes.items():
            value_col = {
                "attendances": "patient_count",
                "wait_time": "wait_time",
                "bor": "occupancy_rate"
            }[key]
            logger.info(f"Cleaning {key} data")
            cleaned_data[key] = clean_moh_dataset(df, value_col)
            logger.info(f"{key} cleaned data shape: {cleaned_data[key].shape}")
        logger.info("Data transformation completed successfully")
    except Exception as e:
        logger.error(f"Pipeline aborted during cleaning: {e}")
        return

    if cleaned_data['attendances'].empty:
        logger.error("attendances_clean is empty. Aborting pipeline.")
        return

    # MERGE
    try:
        logger.info("Merging datasets")
        merged_df = cleaned_data['attendances'].merge(cleaned_data['wait_time'], on=["date", "hospital"], how="outer")
        merged_df = merged_df.merge(cleaned_data['bor'], on=["date", "hospital"], how="outer")
        logger.info(f"Merged data shape: {merged_df.shape}")
        logger.info("Merging completed successfully")
    except Exception as e:
        logger.error(f"Pipeline aborted during merging: {e}")
        return

    # SAVE TO CSV in processed folder
    try:
        os.makedirs(processed_data_dir, exist_ok=True)
        for key, df in cleaned_data.items():
            df.to_csv(os.path.join(processed_data_dir, f"{key}_clean.csv"), index=False)
        merged_df.to_csv(os.path.join(processed_data_dir, "er_summary.csv"), index=False)
        logger.info("Cleaned data saved to processed CSV")
    except Exception as e:
        logger.error(f"Failed saving CSVs: {e}")
        return

    # LOAD TO POSTGRES
    try:
        load_to_postgresql(
            cleaned_data['attendances'], cleaned_data['wait_time'],
            cleaned_data['bor'], merged_df, db_config, logger # db_config is an argument for loading to postgresql db
        )
        logger.info("Data loaded into PostgreSQL successfully")
    except Exception as e:
        logger.error(f"Pipeline aborted during loading: {e}")
        return

    logger.info("ETL pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()
