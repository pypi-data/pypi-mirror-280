import pandas as pd


def read_csv(file_path: str) -> pd.DataFrame:
    """
    Lee un archivo CSV y devuelve un DataFrame de pandas.

    Args:
        file_path (str): La ruta del archivo CSV.

    Returns:
        pd.DataFrame: El DataFrame leído.
    """
    df = pd.read_csv(file_path)
    print("Primeras cinco filas del DataFrame:")
    print(df.head())
    print("\nEstructura del DataFrame:")
    print(df.info())
    return df


def clean_csv(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia el DataFrame eliminando columnas innecesarias.

    Args:
        df (pd.DataFrame): El DataFrame original.

    Returns:
        pd.DataFrame: El DataFrame limpiado.
    """
    columns_to_keep = ['month', 'state', 'permit', 'handgun', 'long_gun']
    cleaned_df = df[columns_to_keep]
    print("Columnas del DataFrame después de la limpieza:")
    print(cleaned_df.columns)
    return cleaned_df


def rename_col(df: pd.DataFrame) -> pd.DataFrame:
    """
    Renombra la columna 'longgun' a 'long_gun' en el DataFrame.

    Args:
        df (pd.DataFrame): El DataFrame con la columna a renombrar.

    Returns:
        pd.DataFrame: El DataFrame con la columna renombrada.
    """
    if 'longgun' in df.columns:
        df = df.rename(columns={'longgun': 'long_gun'})
    print("Columnas del DataFrame después del renombrado:")
    print(df.columns)
    return df