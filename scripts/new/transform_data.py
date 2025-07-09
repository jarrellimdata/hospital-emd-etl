#transform_data.py

import pandas as pd

def clean_moh_dataset(df, value_column_name):
    df = df.copy()
    df.columns = df.columns.str.strip()

    if "Years" in df.columns:
        df = df.drop(columns=["Years"])

    if "Date" not in df.columns:
        return pd.DataFrame()

    df = df[pd.to_datetime(df["Date"], errors="coerce").notna()]

    df_long = df.melt(id_vars=["Date"], var_name="hospital", value_name=value_column_name)
    df_long = df_long.rename(columns={"Date": "date"})
    df_long["date"] = pd.to_datetime(df_long["date"])
    df_long["hospital"] = df_long["hospital"].str.strip()
    
    # invalid_rows = df_long[df_long[value_column_name].astype(str).str.lower() == 'none']
    # if not invalid_rows.empty:
    #     print(f"[DEBUG] Found {len(invalid_rows)} rows with 'None' in {value_column_name}")
    #     print(invalid_rows.head())

    # Convert value column to numeric, coercing 'None' and other invalids to NaN
    df_long[value_column_name] = pd.to_numeric(df_long[value_column_name], errors="coerce")

    # Drop rows where value is NaN
    df_long = df_long.dropna(subset=[value_column_name]).drop_duplicates()

    return df_long

