import pandas as pd

# Extract raw Excel files into DataFrames
# Called in run_pipeline() as the first step
# Returns 3 separate DataFrames for transformation

# def extract_data():
#     # Define file paths for the 3 raw Excel datasets
#     attendances_path = "data/raw/Attendances at EMD_week24Y2025.xlsx"
#     wait_time_path = "data/raw/WT for Admission to Ward_week24Y2025.xlsx"
#     bor_path = "data/raw/Bed Occupancy Rate_week24Y2025.xlsx"

#     # Load each dataset into a pandas DataFrame
#     # Skip first 2 rows to remove header notes or metadata, start reading at actual header row
#     attendances_df = pd.read_excel(attendances_path, sheet_name="Historical", skiprows=2)
#     wait_time_df = pd.read_excel(wait_time_path, sheet_name="Historical", skiprows=2)
#     bor_df = pd.read_excel(bor_path, sheet_name="BOR(%)_historical", skiprows=2)

#     # Return raw extracted dataframes
#     return attendances_df, wait_time_df, bor_df

def extract_data():
    # Define the file paths, sheet names, and number of rows to skip for each dataset
    paths = {
        "attendances": ("data/raw/Attendances at EMD_week24Y2025.xlsx", "Historical", 2),
        "wait_time": ("data/raw/WT for Admission to Ward_week24Y2025.xlsx", "Historical", 2),
        "bor": ("data/raw/Bed Occupancy Rate_week24Y2025.xlsx", "BOR(%)_historical", 2)
    }

    # Dictionary to hold the loaded DataFrames
    dataframes = {}

    # Loop through each dataset configuration, load the Excel sheet, and store in the dictionary
    for key, (path, sheet, skiprows) in paths.items():
        dataframes[key] = pd.read_excel(path, sheet_name=sheet, skiprows=skiprows)

    # Return the dictionary containing all loaded DataFrames
    return dataframes

