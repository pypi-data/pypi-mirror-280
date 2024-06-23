# Análisis de Uso de Armas de Fuego en EE.UU.

Este proyecto tiene como objetivo analizar el comportamiento de la población de Estados Unidos respecto al uso de armas de fuego utilizando datos de verificación de antecedentes.

## Estructura del Proyecto

- **main.py**: Archivo principal que ejecuta todas las funciones del proyecto.
- **data/**: Carpeta que contiene los archivos CSV con los datos y el archivo GeoJSON.
  - `nics-firearm-background-checks.csv`: Datos de verificación de antecedentes de armas.
  - `us-state-populations.csv`: Datos de población por estado.
  - `us-states.json`: Archivo GeoJSON con las fronteras de los estados.
- **maps/**: Carpeta donde se guardarán los mapas generados.
- **my_module/**: Módulo de Python que contiene las funciones de procesamiento, agrupamiento, análisis y visualización de datos.
  - `data_cleaning.py`: Funciones de limpieza de datos.
  - `data_processing.py`: Funciones de procesamiento de datos.
  - `data_grouping.py`: Funciones de agrupamiento de datos.
  - `temporal_analysis.py`: Funciones de análisis temporal.
  - `state_analysis.py`: Funciones de análisis de los estados.
  - `choropleth_maps.py`: Funciones de creación de mapas coropléticos.
- **tests/**: Carpeta que contiene los archivos de pruebas unitarias.
  - `test_data_cleaning.py`: Pruebas para las funciones de limpieza de datos.
  - `test_data_processing.py`: Pruebas para las funciones de procesamiento de datos.
  - `test_data_grouping.py`: Pruebas para las funciones de agrupamiento de datos.
  - `test_temporal_analysis.py`: Pruebas para las funciones de análisis temporal.
  - `test_state_analysis.py`: Pruebas para las funciones de análisis de los estados.
  - `test_choropleth_maps.py`: Pruebas para las funciones de creación de mapas coropléticos.
- **README.md**: Archivo con información sobre el proyecto.
- **requirements.txt**: Archivo con las dependencias necesarias para ejecutar el proyecto.
- **LICENSE**: Archivo de licencia.
- **setup.py**: Archivo de configuración para empaquetar el proyecto.

## Requisitos

Asegúrate de tener instaladas las siguientes librerías de Python:

- pandas
- folium
- matplotlib
- pytest

Puedes instalarlas usando el archivo `requirements.txt`:

```sh
pip install -r requirements.txt
