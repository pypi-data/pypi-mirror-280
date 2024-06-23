import pandas as pd


def groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa los datos por estado y año y calcula los valores acumulados totales.

    Args:
        df (pd.DataFrame): El DataFrame con las columnas 'year', 'state', 'permit', 'handgun', 'long_gun'.

    Returns:
        pd.DataFrame: El DataFrame agrupado por 'state' y 'year'.
    """
    if 'state' in df.columns and 'year' in df.columns:
        grouped_df = df.groupby(['state', 'year']).sum().reset_index()
    else:
        raise KeyError("Las columnas 'state' y 'year' no existen en el DataFrame")
    return grouped_df

def print_biggest_handguns(df: pd.DataFrame):
    """
    Imprime el estado y el año con el mayor número de 'handgun'.

    Args:
        df (pd.DataFrame): El DataFrame agrupado por 'state' y 'year'.
    """
    max_handgun = df.loc[df['handgun'].idxmax()]
    print(
        f"El mayor número de handguns se registró en {max_handgun['state']} en el año {max_handgun['year']}, con un total de {max_handgun['handgun']}.")


def print_biggest_longguns(df: pd.DataFrame):
    """
    Imprime el estado y el año con el mayor número de 'long_gun'.

    Args:
        df (pd.DataFrame): El DataFrame agrupado por 'state' y 'year'.
    """
    max_longgun = df.loc[df['long_gun'].idxmax()]
    print(
        f"El mayor número de longguns se registró en {max_longgun['state']} en el año {max_longgun['year']}, con un total de {max_longgun['long_gun']}.")
