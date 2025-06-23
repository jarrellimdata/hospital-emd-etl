from scripts.extract_data import extract_data
from scripts.transform_data import clean_moh_dataset
from scripts.load_to_postgres import load_to_postgresql
import os

# Full pipeline to orchestrate extraction → transformation → loading
# Includes basic logging and error handling at each step

def run_pipeline():
    # Step 1: Call extract_data() to load raw Excel files into DataFrames
    try:
        print("\n📥 Data extraction in progress...")
        attendances_df, wait_time_df, bor_df = extract_data()
        print("\n✅ Data extracted successfully:")
        print(f"Attendances shape: {attendances_df.shape}, Columns: {attendances_df.columns.tolist()}")
        print(f"Wait time shape: {wait_time_df.shape}, Columns: {wait_time_df.columns.tolist()}")
        print(f"BOR shape: {bor_df.shape}, Columns: {bor_df.columns.tolist()}")
    except Exception as e:
        print(f"❌ Failed during data extraction: {e}")
        return

    # Step 2: Use clean_moh_dataset() to reshape and clean each DataFrame
    try:
        print("\n🔄 Reshaping and cleaning data...")
        attendances_clean = clean_moh_dataset(attendances_df, "patient_count")
        wait_time_clean = clean_moh_dataset(wait_time_df, "wait_time")
        bor_clean = clean_moh_dataset(bor_df, "occupancy_rate")
        print("\n✅ Data transformed successfully:")
        print(f"Attendances clean shape: {attendances_clean.shape}, Columns: {attendances_clean.columns.tolist()}")
        print(f"Wait time clean shape: {wait_time_clean.shape}, Columns: {wait_time_clean.columns.tolist()}")
        print(f"BOR clean shape: {bor_clean.shape}, Columns: {bor_clean.columns.tolist()}")
    except Exception as e:
        print(f"❌ Failed during data cleaning: {e}")
        return

    # Abort pipeline if attendances_clean is empty (critical table for merging)
    if attendances_clean.empty:
        print("❌ attendances_clean is empty. Aborting.")
        return

    # Step 3: Merge the cleaned outputs from clean_moh_dataset() using date and hospital keys
    try:
        print("\n🔗 Merging datasets...")
        merged_df = attendances_clean.merge(wait_time_clean, on=["date", "hospital"], how="outer")
        merged_df = merged_df.merge(bor_clean, on=["date", "hospital"], how="outer")
        print(f"Merged DataFrame shape: {merged_df.shape}, Columns: {merged_df.columns.tolist()}")
    except Exception as e:
        print(f"❌ Failed during merging: {e}")
        return

    # Step 4: Save cleaned and merged datasets to local CSVs in /data/processed
    try:
        print("\n💾 Saving cleaned datasets to CSV...")
        os.makedirs("data/processed", exist_ok=True)
        attendances_clean.to_csv("data/processed/attendances_clean.csv", index=False)
        wait_time_clean.to_csv("data/processed/wait_time_clean.csv", index=False)
        bor_clean.to_csv("data/processed/bor_clean.csv", index=False)
        merged_df.to_csv("data/processed/er_summary.csv", index=False)
        print("\n✅ Cleaned datasets saved to CSV files.")
    except Exception as e:
        print(f"❌ Failed during saving CSV files: {e}")
        return

    # Step 5: Call load_to_postgresql() to write data into PostgreSQL tables
    try:
        print("\n🚀 Loading to PostgreSQL in progress...")
        load_to_postgresql(attendances_clean, wait_time_clean, bor_clean, merged_df)
        print("\n✅ Data loaded into PostgreSQL successfully.")
    except Exception as e:
        print(f"❌ Failed during loading to PostgreSQL: {e}")
        return

    # Final message if all steps complete without error
    print("\n🎉 ETL pipeline complete. All steps succeeded.")

# Run the ETL pipeline only when executed directly (not imported)
if __name__ == "__main__":
    run_pipeline()
