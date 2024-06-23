import pandas as pd
import folium
from selenium import webdriver
from PIL import Image
import io
import os
import requests


def download_geojson(url: str, save_path: str):
    """
    Descarga un archivo GeoJSON desde una URL y lo guarda en la ruta especificada.

    Args:
        url (str): La URL desde donde se descargará el archivo.
        save_path (str): La ruta donde se guardará el archivo descargado.
    """
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)


def create_choropleth_map(df: pd.DataFrame, column: str, geojson_path: str, map_title: str, output_image: str):
    """
    Crea un mapa coroplético para la columna especificada del DataFrame y guarda como imagen PNG.

    Args:
        df (pd.DataFrame): El DataFrame con los datos a visualizar.
        column (str): La columna del DataFrame a visualizar en el mapa.
        geojson_path (str): La ruta del archivo GeoJSON con las fronteras de los estados.
        map_title (str): El título del mapa.
        output_image (str): La ruta del archivo PNG donde se guardará el mapa.
    """
    # Creo el mapa
    m = folium.Map(location=[37.8, -96], zoom_start=4)

    folium.Choropleth(
        geo_data=geojson_path,
        name='choropleth',
        data=df,
        columns=['state', column],
        key_on='feature.properties.name',
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=map_title
    ).add_to(m)

    folium.LayerControl().add_to(m)

    # Convierto el mapa a imagen usando Selenium
    convert_map_to_image(m, output_image)


def convert_map_to_image(m, image_path: str):
    """
    Convierte un mapa de Folium a una imagen PNG usando Selenium.

    Args:
        m (folium.Map): El objeto de mapa de Folium.
        image_path (str): La ruta donde se guardará la imagen PNG.
    """
    # Guardo el mapa como archivo HTML temporal
    temp_html = 'temp_map.html'
    m.save(temp_html)

    # Configuración del navegador
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')

    # Inicio el navegador
    driver = webdriver.Firefox(options=options)
    driver.get(f"file://{os.path.abspath(temp_html)}")

    # Capturo la pantalla y la guardo como imagen
    img_data = driver.get_screenshot_as_png()
    img = Image.open(io.BytesIO(img_data))
    img.save(image_path)
    driver.quit()

    # Elimino el archivo HTML temporal
    os.remove(temp_html)


def create_all_maps(df: pd.DataFrame):
    """
    Crea mapas coropléticos para 'permit_perc', 'handgun_perc' y 'longgun_perc'.

    Args:
        df (pd.DataFrame): El DataFrame con los datos a visualizar.
    """
    # URL del archivo GeoJSON
    url = "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/us-states.json"
    geojson_path = 'data/us-states.json'  # Ruta al archivo GeoJSON

    # Descargo el archivo GeoJSON
    download_geojson(url, geojson_path)

    # Creo los 3 mapas que se piden
    create_choropleth_map(df, 'permit_perc', geojson_path, 'Permits per 100 People', 'maps/permit_perc_map.png')
    create_choropleth_map(df, 'handgun_perc', geojson_path, 'Handguns per 100 People', 'maps/handgun_perc_map.png')
    create_choropleth_map(df, 'longgun_perc', geojson_path, 'Long Guns per 100 People', 'maps/longgun_perc_map.png')
