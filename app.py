import pandas as pd
import streamlit as st

# URL con la lista de pokemones
URL = 'https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv'


# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("#", "Name", "Type 1", "Generation")
)


@st.cache_data
def load_data():
    """Carga los datos de la URL"""
    data = pd.read_csv(URL)
    return data


pokemon_data = load_data()

st.header('Pokemones')
st.write(pokemon_data)
