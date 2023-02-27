import time
import pandas as pd
import streamlit as st

# URL con la lista de pokemones
URL = 'https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv'


@st.cache_data
def load_data():
    """Carga los datos de la URL"""
    data = pd.read_csv(URL)
    return data


pokemon_data = load_data()


# SELECCIONAR LA GENERACON DE POKEMON
def select_generation():
    st.sidebar.header("Selecciona la generación")
    st.sidebar.slider(
        "La generaciones van de la 1 a la 6", min_value=1, max_value=6)


# SELECCIONAR VALOR VIDA
st.sidebar.header("Selecciona el rango de vida")
columnas_hp = st.sidebar.columns(2)
hp_min = columnas_hp[0].number_input(
    "Salud minima", value=pokemon_data['HP'].min())
HP_max = columnas_hp[1].number_input(
    "Maximum HP", value=pokemon_data['HP'].max())
if HP_max < hp_min:
    st.error("La salud máxima no puede ser menor que la mínima!")
else:
    st.success("Parametros correctos!")
    subset_HP = pokemon_data[(pokemon_data['HP'] <= HP_max) & (
        hp_min <= pokemon_data['HP'])]

# BARRA DE CARGA
progress_bar = st.progress(0)
progress_text = st.empty()
# definir el tiempo de espera
for i in range(101):
    time.sleep(0.1)
    progress_bar.progress(i)
    progress_text.text(f"Progress: {i}%")


st.header('Pokemones')
st.write(select_generation())
