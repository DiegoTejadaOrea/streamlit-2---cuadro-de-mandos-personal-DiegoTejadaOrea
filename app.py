import plotly.graph_objects as go
import time
import pandas as pd
import streamlit as st
import requests
import plotly.express as px
import matplotlib.pyplot as plt
import base64
from PIL import Image
import numpy as np


# URL con la lista de pokemones
URL = 'https://raw.githubusercontent.com/DWES-LE/streamlit-2---cuadro-de-mandos-personal-DiegoTejadaOrea/main/datos/datos_pokemon_actualizados.csv'


# ============ generation Y CARGA DE DATOS ====================


@st.cache_data
def load_data():
    """Carga los datos de la URL"""
    data = pd.read_csv(URL)
    return data


pokemon_data = load_data()

# st.header('QUE POKEMON ERES TU?')
# Crear un elemento vacío para la tabla
tabla = st.empty()

# ==============================================================

# Cargar los datos del archivo CSV
df = pd.read_csv(URL)


# ============= GENERACION DE POKEMON EN ABSE A TU EDAD =======================

# Crear un sidebar para seleccionar la edad de la persona
st.sidebar.title('Selecciona tu edad')
edad = st.sidebar.slider('Edad', min_value=5, max_value=45, value=30)


def obtener_generacion(edad):
    if edad < 5:
        return df[df["generation"] == 9]
    elif edad < 10:
        return df[df["generation"] == 8]
    elif edad < 15:
        return df[df["generation"] == 7]
    elif edad < 20:
        return df[df["generation"] == 6]
    elif edad < 25:
        return df[df["generation"] == 5]
    elif edad < 30:
        return df[df["generation"] == 4]
    elif edad < 35:
        return df[df["generation"] == 3]
    elif edad < 40:
        return df[df["generation"] == 2]
    else:
        return df[df["generation"] == 1]


st.sidebar.write('Tu generación es la: ' +
                 str(obtener_generacion(edad).generation.unique()[0]))

generacion = obtener_generacion(edad)
tabla.write(generacion)


# ============================================================================

# ============= TIPO DE POKEMON EN BASE A TUS GUSTOS =======================
st.sidebar.title('Que te define mejor?')
# quiero poder seleccionar el tipo de pokemon que me define mejor, hasta 3 opciones
preferencia = st.sidebar.multiselect("Selecciona que te define mejor (3 max)", ["Bug", "Dark", "Dragon", "Electric",
                                                                                "Fairy", "Fighting", "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"])


def obtener_tipo(preferencia):
    # Filtrar los datos según las 3 opciones seleccionadas por el usuario y que se apliquen únicamente al campo 'Type 1'
    filtro = preferencia[:3] if len(preferencia) > 3 else preferencia
    df_filtered = df[df['Type 1'].isin(filtro)]
    return df_filtered


preferencia = obtener_tipo(preferencia)
# juntar filtro de generacion y preferencia
preferencia = generacion.merge(preferencia, how='inner')

tabla.write(preferencia)


# ============================================================================


# ============= TIPO DE POKEMON EN BASE A TU ESTADO FISICO =======================
st.sidebar.title('Selecciona tu estado fisico')
estado_fisico = st.sidebar.selectbox("Selecciona tu estado fisico", [
    "Muy bueno (Super atleta)", "Bueno (Deportista)", "Regular (Promedio)", "Malo (Nefasto)"])


def obtener_estado_fisico(estado_fisico):
    if estado_fisico == "Muy bueno":
        return df[(df["HP"] >= 180) & (df["HP"] <= 200)]
    elif estado_fisico == "Bueno":
        return df[(df["HP"] >= 130) & (df["HP"] <= 180)]
    elif estado_fisico == "Regular":
        return df[(df["HP"] >= 50) & (df["HP"] <= 130)]
    else:
        return df[(df["HP"] >= 0) & (df["HP"] <= 50)]


estado_fisico = obtener_estado_fisico(estado_fisico)
# juntar filtro de estado_fisico y preferencia
estado_fisico = preferencia.merge(estado_fisico, how='inner')

tabla.write(estado_fisico)

# ============================================================================


# ======================FILTRO ATACAR DEFENDER==============================

# Crear un menú desplegable para seleccionar entre "atacar" o "defenderse"
st.sidebar.title("¿Qué se te da mejor, atacar o defenderte?")
defensa_personal = st.sidebar.selectbox("¿Qué se te da mejor?", [
    "Atacar", "Defenderse", "Ninguna de las dos"])

# Filtrar los datos según la preferencia seleccionada por el usuario


def obtener_pelea(defensa_personal):
    if defensa_personal == "Atacar":
        return df[df["Attack"] >= df["Defense"]]
    elif defensa_personal == "Defenderse":
        return df[df["Defense"] >= df["Attack"]]
    else:
        return df


defensa_personal = obtener_pelea(defensa_personal)

# juntar filtro de defensa_personal y preferencia
defensa_personal = preferencia.merge(defensa_personal, how='inner')
tabla.write(defensa_personal)


# ============================================================================

# ======================FILTRO VELOCIDAD=============================

# Crear un slider en el sidebar para seleccionar un rango de velocidad
velocidad_min, velocidad_max = st.sidebar.slider(
    "¿Como de veloz crees que eres en % (pon de 0-max)?", 0, 200, (0, 100))
# Filtrar los datos según el rango de velocidad seleccionado por el usuario
velocidad = df[(df["Speed"] >= velocidad_min) &
               (df["Speed"] <= velocidad_max)]

# juntar filtro de defensa_personal y velocidad
velocidad = defensa_personal.merge(velocidad, how='inner')
tabla.write(velocidad)

# ============================================================================


# ======================== FUSION DE FILTROS MOSTRADO DE IMAGEN =========================

# si no hay ningun pokemon que cumpla con los filtros mostrara un mensaje de error
if len(velocidad) == 0:
    st.error(
        "No hay ningun pokemon que cumpla con los filtros seleccionados, pruebe a reajustar los filtros o seleccionar mas tipos diferentes.")
else:

    # enseñar campo en especifico de la tabla url_img
    imagen_url = velocidad.url_img.iloc[0]

    # Redimensionar la imagen
    imagen_redimensionada = Image.open(requests.get(
        imagen_url, stream=True).raw).resize((700, 700))

    # Mostrar en un parrafo texto con los datos fitrados
    st.header('El pokemon de la :blue[generacion] ' + str(generacion.generation.unique()[0]) +
              ' que mejor se adapta a ti es: ' + str(velocidad.nombre.iloc[0]))
    # Desactivar la opción de matplotlib para reducir el espacio entre el texto y la imagen
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Mostrar la imagen redimensionada
    st.image(imagen_redimensionada,
             caption='Imagen redimensionada', use_column_width=True)


# ============================================================================
