import plotly.graph_objects as go
import time
import pandas as pd
import streamlit as st
import requests
import plotly.express as px
import matplotlib.pyplot as plt

# URL con la lista de pokemones
URL = 'https://raw.githubusercontent.com/DWES-LE/streamlit-2---cuadro-de-mandos-personal-DiegoTejadaOrea/main/datos_pokemon_unidos.csv'

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

st.dataframe(generacion)

# ============================================================================

# ============= TIPO DE POKEMON EN BASE A TUS GUSTOS =======================
st.sidebar.title('Que te define mejor?')
preferencia = st.sidebar.selectbox("Selecciona tu preferencia de gusto", ["Entomología", "Noche", "Mitologia", "Mecanica", "Fantasia",
                                                                          "Deporte", "Caos", "Pjaros", "Fantasmas", "Naturaleza",
                                                                          "Tierra", "Nieve", "Normal", "Venom", "Musica",
                                                                          "Geologia", "Nadar", "Soldadura"])


def obtener_tipo(preferencia):
    if preferencia == "Entomología":
        return df[df["Type"] == "Bug"]
    elif preferencia == "Noche":
        return df[df["Type"] == "Dark"]
    elif preferencia == "Mitologia":
        return df[df["Type"] == "Dragon"]
    elif preferencia == "Mecanica":
        return df[df["Type"] == "Electric"]
    elif preferencia == "Fantasia":
        return df[df["Type"] == "Fairy"]
    elif preferencia == "Deporte":
        return df[df["Type"] == "Fighting"]
    elif preferencia == "Caos":
        return df[df["Type"] == "Fire"]
    elif preferencia == "Pjaros":
        return df[df["Type"] == "Flying"]
    elif preferencia == "Fantasmas":
        return df[df["Type"] == "Ghost"]
    elif preferencia == "Naturaleza":
        return df[df["Type"] == "Grass"]
    elif preferencia == "Tierra":
        return df[df["Type"] == "Ground"]
    elif preferencia == "Nieve":
        return df[df["Type"] == "Ice"]
    elif preferencia == "Normal":
        return df[df["Type"] == "Normal"]
    elif preferencia == "Venom":
        return df[df["Type"] == "Poison"]
    elif preferencia == "Musica":
        return df[df["Type"] == "Psychic"]
    elif preferencia == "Geologia":
        return df[df["Type"] == "Rock"]
    elif preferencia == "Nadar":
        return df[df["Type"] == "Water"]
    else:
        return df[df["Type"] == "Steel"]


preferencia = obtener_tipo(preferencia)
st.dataframe(preferencia)
