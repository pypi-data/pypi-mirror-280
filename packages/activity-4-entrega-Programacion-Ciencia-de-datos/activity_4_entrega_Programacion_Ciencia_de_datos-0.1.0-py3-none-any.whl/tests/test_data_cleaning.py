import pytest
import pandas as pd
from my_module.data_cleaning import read_csv, clean_csv, rename_col

def test_read_csv():
    df = read_csv('data/nics-firearm-background-checks.csv')
    assert not df.empty

def test_clean_csv():
    df = read_csv('data/nics-firearm-background-checks.csv')
    df_cleaned = clean_csv(df)
    assert set(df_cleaned.columns) == {'month', 'state', 'permit', 'handgun', 'long_gun'}

def test_rename_col():
    df = read_csv('data/nics-firearm-background-checks.csv')
    df_cleaned = clean_csv(df)
    df_renamed = rename_col(df_cleaned)
    assert 'long_gun' in df_renamed.columns

if __name__ == "__main__":
    pytest.main()
