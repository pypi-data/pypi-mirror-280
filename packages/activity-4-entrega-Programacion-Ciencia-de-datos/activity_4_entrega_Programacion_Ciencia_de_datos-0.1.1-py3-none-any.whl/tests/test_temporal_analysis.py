from my_module.data_cleaning import read_csv, clean_csv, rename_col
from my_module.data_processing import breakdown_date, erase_month
from my_module.data_grouping import groupby_state_and_year
from my_module.temporal_analysis import time_evolution


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


def test_groupby_state_and_year():
    df = read_csv('data/nics-firearm-background-checks.csv')
    df_cleaned = clean_csv(df)
    df_renamed = rename_col(df_cleaned)
    df_with_date = breakdown_date(df_renamed)
    df_final = erase_month(df_with_date)
    grouped_df = groupby_state_and_year(df_final)
    assert not grouped_df.empty
    assert 'state' in grouped_df.columns
    assert 'year' in grouped_df.columns


def test_time_evolution():
    df = read_csv('data/nics-firearm-background-checks.csv')
    df_cleaned = clean_csv(df)
    df_renamed = rename_col(df_cleaned)
    df_with_date = breakdown_date(df_renamed)
    df_final = erase_month(df_with_date)
    grouped_df = groupby_state_and_year(df_final)
    time_evolution(grouped_df)
