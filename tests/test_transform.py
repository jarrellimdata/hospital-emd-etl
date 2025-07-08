# tests/test_transform.py

from scripts.new.transform_data import clean_moh_dataset
import pandas as pd

def test_clean_valid_attendance():
    df = pd.DataFrame({
        "Date": ["2024-01-01", "2024-01-02"],
        "Hospital A": [5, 10],
        "Hospital B": [3, 6]
    })
    cleaned = clean_moh_dataset(df, "patient_count")
    assert not cleaned.empty
    assert set(cleaned.columns) == {"date", "hospital", "patient_count"}
