import pandas as pd

def clean_moh_dataset(df, value_column_name):
    df = df.copy()
    df.columns = df.columns.str.strip()  # Clean whitespace from column names

    if "Years" in df.columns:
        df = df.drop(columns=["Years"])

    if "Date" not in df.columns:
        return pd.DataFrame()  # Empty if Date column missing

    df = df[pd.to_datetime(df["Date"], errors="coerce").notna()]  # Keep valid dates only

    # Convert wide to long format
    df_long = df.melt(id_vars=["Date"], var_name="hospital", value_name=value_column_name)
    df_long = df_long.rename(columns={"Date": "date"})
    df_long["date"] = pd.to_datetime(df_long["date"])
    df_long["hospital"] = df_long["hospital"].str.strip()
    df_long = df_long.dropna(subset=[value_column_name]).drop_duplicates()

    return df_long
