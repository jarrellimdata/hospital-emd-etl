# tests/test_transform.py

from scripts.new.transform_data import clean_moh_dataset
import pandas as pd

def test_clean_valid_attendance():
    # Sample wide-format input data (as in Excel)
    df = pd.DataFrame({
        "Date": ["2024-01-01", "2024-01-02"],
        "Hospital A": [5, 10],
        "Hospital B": [3, 6]
    })

    # Run cleaning
    cleaned = clean_moh_dataset(df, "patient_count")

    # Assert output is not empty and in long format
    assert not cleaned.empty
    assert set(cleaned.columns) == {"date", "hospital", "patient_count"}

