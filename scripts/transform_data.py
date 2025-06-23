import pandas as pd

# Clean and transform each dataset after extraction
# Called in run_pipeline() for all 3 datasets
# Performs standard reshaping, column cleanup, and missing data handling

def clean_moh_dataset(df, value_column_name):
    # Make a copy of input DataFrame to avoid modifying original
    df = df.copy()

    # Strip whitespace from all column names for consistency
    df.columns = df.columns.str.strip()
    
    # Remove 'Years' column as 'date' column is sufficient
    if "Years" in df.columns:
        df = df.drop(columns=["Years"])

    # Return empty DataFrame if 'Date' column is missing (critical for time series)
    if "Date" not in df.columns:
        return pd.DataFrame()

    # Keep only rows where 'Date' can be parsed into a valid datetime
    df = df[pd.to_datetime(df["Date"], errors="coerce").notna()]

    # Reshape data from wide to long format:
    # 'Date' remains as an identifier; other columns (hospitals) become row values
    df_long = df.melt(id_vars=["Date"], var_name="hospital", value_name=value_column_name)

    # Rename 'Date' column to lowercase 'date' for consistency
    df_long = df_long.rename(columns={"Date": "date"})

    # Convert 'date' column to datetime type
    df_long["date"] = pd.to_datetime(df_long["date"])

    # Strip whitespace from hospital names
    df_long["hospital"] = df_long["hospital"].str.strip()

    # Drop rows where the value (patient_count, wait_time, or occupancy_rate) is missing
    # Remove duplicate rows to ensure data quality
    df_long = df_long.dropna(subset=[value_column_name]).drop_duplicates()

    return df_long
