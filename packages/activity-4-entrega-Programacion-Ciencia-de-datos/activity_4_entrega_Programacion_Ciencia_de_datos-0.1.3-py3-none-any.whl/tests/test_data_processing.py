import pytest
from my_module.data_cleaning import read_csv, clean_csv, rename_col
from my_module.data_processing import breakdown_date, erase_month

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

def test_breakdown_date():
    df = read_csv('data/nics-firearm-background-checks.csv')
    df_cleaned = clean_csv(df)
    df_renamed = rename_col(df_cleaned)
    df_with_date = breakdown_date(df_renamed)
    assert 'year' in df_with_date.columns
    assert 'month' in df_with_date.columns

def test_erase_month():
    df = read_csv('data/nics-firearm-background-checks.csv')
    df_cleaned = clean_csv(df)
    df_renamed = rename_col(df_cleaned)
    df_with_date = breakdown_date(df_renamed)
    df_final = erase_month(df_with_date)
    assert 'month' not in df_final.columns