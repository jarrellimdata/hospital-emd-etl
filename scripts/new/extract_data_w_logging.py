import pandas as pd

def extract_data(data_paths, logger):
    """
    Extracts raw Excel data for attendances, wait time, and BOR from configured paths.
    Performs schema validation (logs missing/extra columns but does not abort).
    
    Args:
        data_paths (dict): File paths for each dataset.
        logger (Logger): Logger instance for logging pipeline steps.

    Returns:
        dict: Dictionary of raw pandas DataFrames.
    """
    dataframes = {}

    # Define expected columns for each dataset
    expected_schema = {
        "attendances": {"Date", "AH", "CGH", "KTPH", "NTFGH", "NUH(A)", "SGH", "SKH", "TTSH", "WH"},
        "wait_time":   {"Date", "AH", "CGH", "KTPH", "NTFGH", "NUH(A)", "SGH", "SKH", "TTSH", "WH"},
        "bor":         {"Years", "Date", "AH", "CGH", "KTPH", "NTFGH", "NUH(A)", "SGH", "SKH", "TTSH", "WH"},
    }

    for key, path in data_paths.items():
        try:
            logger.info(f"Extracting {key} data from {path}")

            # Select correct sheet name based on dataset
            sheet = "BOR(%)_historical" if key == "bor" else "Historical"

            # Read Excel with appropriate sheet and skip header notes
            df = pd.read_excel(path, sheet_name=sheet, skiprows=2)

            # Schema validation
            # Check if expected columns match actual columns
            expected_cols = expected_schema[key] # access key in expected_schema above
            actual_cols = set(df.columns) # convert to set for comparison
            logger.info(f"Validating {key} data columns: {actual_cols}")
            

            missing_cols = expected_cols - actual_cols
            extra_cols = actual_cols - expected_cols
            if missing_cols:
                logger.warning(f"{key} is missing expected columns: {missing_cols}")
            if extra_cols:
                logger.info(f"{key} has unexpected extra columns: {extra_cols}")
            else:
                logger.info(f"{key} schema validation passed")

            # Add dataframe to results after validation
            dataframes[key] = df
            logger.info(f"{key} data shape: {df.shape}")

        except Exception as e:
            logger.error(f"Failed to extract {key} data: {e}")
            raise

    # logger.info("Data extraction completed successfully")
    return dataframes
