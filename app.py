import plotly.graph_objects as go
import time
import pandas as pd
import streamlit as st
import requests
import plotly.express as px
import matplotlib.pyplot as plt

# URL con la lista de pokemones
URL = 'https://raw.githubusercontent.com/DWES-LE/streamlit-2---cuadro-de-mandos-personal-DiegoTejadaOrea/main/datos_pokemon_unidos.csv'

# ============ GENERACIÓN Y CARGA DE DATOS ====================


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

# Definir las generaciones de Pokémon y las edades de corte
generaciones = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
edades_corte = [5, 10, 15, 20, 25, 35, 40, 45, 50]

# Crear un sidebar para seleccionar la edad de la persona
st.sidebar.title('Selecciona tu edad')
edad = st.sidebar.slider('Edad', min_value=5, max_value=50, value=30)

# Determinar la generación de Pokémon que se mostrará en función de la edad de la persona
for i, edad_corte in enumerate(edades_corte):
    if edad <= edad_corte:
        generacion_seleccionada = generaciones[i]
        break

# Filtrar los datos por generación de Pokémon seleccionada
df_filtrado = df[df['generation'] == generacion_seleccionada]

# Mostrar los datos filtrados en una tabla
st.write(f"Generación de Pokémon para {edad} años:")
st.write(df_filtrado)
