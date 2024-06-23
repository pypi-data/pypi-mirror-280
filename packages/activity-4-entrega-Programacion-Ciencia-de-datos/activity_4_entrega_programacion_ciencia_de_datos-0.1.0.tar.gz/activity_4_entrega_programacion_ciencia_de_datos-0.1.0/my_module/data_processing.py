
def breakdown_date(df):
    # Asegúrate de que la columna 'month' existe
    if 'month' in df.columns:
        df[['year', 'month']] = df['month'].str.split('-', expand=True).astype(int)
    else:
        raise KeyError("La columna 'month' no existe en el DataFrame")
    return df


def erase_month(df):
    # Asegúrate de que la columna 'year' y 'month' existen antes de eliminar 'month'
    if 'year' in df.columns and 'month' in df.columns:
        df.drop(columns=['month'], inplace=True)
    else:
        raise KeyError("Las columnas 'year' y 'month' no existen en el DataFrame")
    return df
