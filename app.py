import plotly.graph_objects as go
import time
import pandas as pd
import streamlit as st
import requests
import plotly.express as px
import matplotlib.pyplot as plt
import base64
from PIL import Image

# URL con la lista de pokemones
URL = 'https://raw.githubusercontent.com/DWES-LE/streamlit-2---cuadro-de-mandos-personal-DiegoTejadaOrea/main/datos_pokemon_actualizados.csv'

# ============ generation Y CARGA DE DATOS ====================


@st.cache_data
def load_data():
    """Carga los datos de la URL"""
    data = pd.read_csv(URL)
    return data


pokemon_data = load_data()

st.header('QUE POKEMON ERES TU?')

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
st.write(generacion)

# ============================================================================

# ============= TIPO DE POKEMON EN BASE A TUS GUSTOS =======================
st.sidebar.title('Que te define mejor?')
preferencia = st.sidebar.selectbox("Selecciona tu preferencia de gusto", ["Entomología", "Noche", "Mitologia", "Mecanica", "Fantasia",
                                                                          "Deporte", "Caos", "Pjaros", "Fantasmas", "Naturaleza",
                                                                          "Tierra", "Nieve", "Normal", "Venom", "Musica",
                                                                          "Geologia", "Nadar", "Soldadura"])


def obtener_tipo(preferencia):
    if preferencia == "Entomología":
        return df[df["Type 1"] == "Bug"]
    elif preferencia == "Noche":
        return df[df["Type 1"] == "Dark"]
    elif preferencia == "Mitologia":
        return df[df["Type 1"] == "Dragon"]
    elif preferencia == "Mecanica":
        return df[df["Type 1"] == "Electric"]
    elif preferencia == "Fantasia":
        return df[df["Type 1"] == "Fairy"]
    elif preferencia == "Deporte":
        return df[df["Type 1"] == "Fighting"]
    elif preferencia == "Caos":
        return df[df["Type 1"] == "Fire"]
    elif preferencia == "Pjaros":
        return df[df["Type 1"] == "Flying"]
    elif preferencia == "Fantasmas":
        return df[df["Type 1"] == "Ghost"]
    elif preferencia == "Naturaleza":
        return df[df["Type 1"] == "Grass"]
    elif preferencia == "Tierra":
        return df[df["Type 1"] == "Ground"]
    elif preferencia == "Nieve":
        return df[df["Type 1"] == "Ice"]
    elif preferencia == "Normal":
        return df[df["Type 1"] == "Normal"]
    elif preferencia == "Venom":
        return df[df["Type 1"] == "Poison"]
    elif preferencia == "Musica":
        return df[df["Type 1"] == "Psychic"]
    elif preferencia == "Geologia":
        return df[df["Type 1"] == "Rock"]
    elif preferencia == "Nadar":
        return df[df["Type 1"] == "Water"]
    else:
        return df[df["Type 1"] == "Steel"]


preferencia = obtener_tipo(preferencia)

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


# ============================================================================

# ======================FILTRO VELOCIDAD=============================

# Crear un slider en el sidebar para seleccionar un rango de velocidad
velocidad_min, velocidad_max = st.sidebar.slider(
    "¿Como de veloz crees que eres en %?", 0, 200, (80, 120))
# Filtrar los datos según el rango de velocidad seleccionado por el usuario
velocidad = df[(df["Speed"] >= velocidad_min) &
               (df["Speed"] <= velocidad_max)]


# ============================================================================


# ========================FUSION DE FILTROS=========================

# Filtrar los datos según los filtros seleccionados por el usuario
def filtrado_total():
    return preferencia.merge(velocidad, how="inner").merge(estado_fisico, how="inner").merge(generacion, how="inner").merge(defensa_personal, how="inner")


# enseñar campo en especifico de la tabla url_img
imagen_url = filtrado_total().url_img.iloc[0]
# st.image(imagen_url, width=400)

# Redimensionar la imagen
imagen_redimensionada = Image.open(requests.get(
    imagen_url, stream=True).raw).resize((700, 700))
# Mostrar la imagen redimensionada
st.header('Tu pokemon es: ' + str(filtrado_total().nombre.iloc[0]))
st.image(imagen_redimensionada, caption='Imagen redimensionada')
