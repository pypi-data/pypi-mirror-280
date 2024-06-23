import pandas as pd


def groupby_state(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa los datos por estado y calcula los valores acumulados totales.

    Args:
        df (pd.DataFrame): El DataFrame agrupado por 'state' y 'year' con las columnas 'permit', 'handgun', 'long_gun'.

    Returns:
        pd.DataFrame: El DataFrame agrupado por 'state'.
    """
    grouped_df = df.groupby('state').sum().reset_index()
    print("Primeras cinco filas del DataFrame agrupado por estado:")
    print(grouped_df.head())
    return grouped_df


def clean_states(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina los estados Guam, Mariana Islands, Puerto Rico y Virgin Islands del DataFrame.

    Args:
        df (pd.DataFrame): El DataFrame agrupado por 'state'.

    Returns:
        pd.DataFrame: El DataFrame sin los estados especificados.
    """
    states_to_remove = ['Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands']
    df_cleaned = df[~df['state'].isin(states_to_remove)]
    print("Número de estados después de limpiar:")
    print(df_cleaned['state'].nunique())
    return df_cleaned


def merge_datasets(firearm_df: pd.DataFrame, population_df: pd.DataFrame) -> pd.DataFrame:
    """
    Fusiona el DataFrame de verificación de antecedentes de armas con el DataFrame de población por estado.

    Args:
        firearm_df (pd.DataFrame): El DataFrame de verificación de antecedentes de armas.
        population_df (pd.DataFrame): El DataFrame de población por estado.

    Returns:
        pd.DataFrame: El DataFrame resultante de fusionar los dos conjuntos de datos.
    """
    merged_df = pd.merge(firearm_df, population_df, on='state')
    print("Primeras cinco filas del DataFrame fusionado:")
    print(merged_df.head())
    return merged_df


def calculate_relative_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula los valores relativos de 'permit', 'handgun' y 'long_gun' en función de la población del estado.

    Args:
        df (pd.DataFrame): El DataFrame fusionado.

    Returns:
        pd.DataFrame: El DataFrame con las nuevas columnas de valores relativos.
    """
    df['permit_perc'] = (df['permit'] * 100) / df['pop_2014']
    df['handgun_perc'] = (df['handgun'] * 100) / df['pop_2014']
    df['longgun_perc'] = (df['long_gun'] * 100) / df['pop_2014']
    print("Primeras cinco filas con valores relativos calculados:")
    print(df.head())
    return df


def analyze_outliers(df: pd.DataFrame):
    """
    Analiza los valores atípicos en el DataFrame, enfocándose en el estado de Kentucky.

    Args:
        df (pd.DataFrame): El DataFrame con las columnas de valores relativos.
    """
    # Calcul0 la media de 'permit_perc'
    mean_permit_perc = df['permit_perc'].mean()
    print(f"Media de permisos (permit_perc): {mean_permit_perc:.2f}")

    # Información del estado de Kentucky
    kentucky_info = df[df['state'] == 'Kentucky']
    print("Información del estado de Kentucky:")
    print(kentucky_info)

    # Reemplazo el valor 'permit_perc' de Kentucky con la media
    df.loc[df['state'] == 'Kentucky', 'permit_perc'] = mean_permit_perc

    # Calculo la nueva media después del reemplazo
    new_mean_permit_perc = df['permit_perc'].mean()
    print(
        f"Nueva media de permisos (permit_perc) después de reemplazar el valor de Kentucky: {new_mean_permit_perc:.2f}")

    # Conclusiones sobre la eliminación de valores atípicos
    conclusion = """
     Inicialmente, la media de permisos (permit_perc) era 34.88 y después de identificar y reemplazar el valor atípico del estado de Kentucky,
     la nueva media de permisos (permit_perc) es 21.12. El valor del estado de Kentucky era considerablemente alto (736.481221), lo cual afectaba significativamente la media general.
     Asi' que al eliminar este valor atípico, la media se ha reducido considerablemente, reflejando una medida más precisa de la tendencia general.
     Esta eliminacion me ha ayudado a obtener una representación más fiel de los datos, evitando que anomalías influyan de manera desproporcionada en las conclusiones.
    """
    print(conclusion)
