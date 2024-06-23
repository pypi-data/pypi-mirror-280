import pandas as pd
import matplotlib.pyplot as plt


def time_evolution(df: pd.DataFrame):
    """
    Analiza la evolución temporal de permisos, pistolas y rifles de asalto.

    Args:
        df (pd.DataFrame): El DataFrame con los datos a analizar.
    """
    df_grouped = df.groupby('year').sum()

    plt.figure(figsize=(10, 6))
    plt.plot(df_grouped.index, df_grouped['permit'], label='Permits', color='blue')
    plt.plot(df_grouped.index, df_grouped['handgun'], label='Handguns', color='orange')
    plt.plot(df_grouped.index, df_grouped['long_gun'], label='Long Guns', color='green')
    plt.xlabel('Año')
    plt.ylabel('Cantidad')
    plt.title('Evolución Temporal de Permisos, Pistolas y Rifles de Asalto')
    plt.legend()
    plt.grid(True)

    # Guardar el gráfico como imagen
    plt.savefig('time_evolution.png')
    plt.close()


def comment_on_evolution():
    """
    Comenta la evolución temporal observada en el gráfico.
    """
    print(
        "El gráfico muestra un incremento significativo en las verificaciones de antecedentes para permisos, pistolas y rifles de asalto a lo largo del tiempo.")
    print(
        "Podemos observar picos notables en ciertos años, lo cual podría correlacionarse con eventos específicos o cambios en la legislación.")
