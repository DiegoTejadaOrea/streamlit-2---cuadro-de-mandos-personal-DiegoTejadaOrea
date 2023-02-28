import time
import pandas as pd
import streamlit as st
import requests
import plotly.express as px

# URL con la lista de pokemones
URL = 'https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv'

# ============ GENERACIÓN Y CARGA DE DATOS ====================


@st.cache_data
def load_data():
    """Carga los datos de la URL"""
    data = pd.read_csv(URL)
    return data


pokemon_data = load_data()

st.header('ESTADÍSTICAS Y DATOS DE POKEMON')

# ==============================================================


# ============ CARGA DE TABLA CON FILTROS ====================

# Crear el sidebar
st.sidebar.title('Seleccionar datos')
option = st.sidebar.selectbox('Seleccione una opción', ('Mostrar todas las columnas',
                              'Mostrar columnas específicas', 'Filtrar por generación', 'Filtrar por HP mínimo'))

# Mostrar los datos según la opción seleccionada
if option == 'Mostrar todas las columnas':
    st.write(pokemon_data)
elif option == 'Mostrar columnas específicas':
    selected_columns = st.sidebar.multiselect(
        'Seleccione las columnas que desea mostrar', pokemon_data.columns)
    st.write(pokemon_data[selected_columns])
elif option == 'Filtrar por generación':
    gen = st.sidebar.slider('Seleccione la generación', 1, 6)
    st.write(pokemon_data[pokemon_data['Generation'] == gen])
else:
    hp_min = st.sidebar.text_input('Ingrese el HP mínimo:', value='0')
    filtered_data = pokemon_data[pokemon_data['HP'] >= float(hp_min)]
    st.write(filtered_data)


# ==============================================================


# ================= GRÁFICO REDONDO =========================

# CANTIDAD DE POKEMONS POR GENERACIÓN EN PORCENTAJE
# Contar la cantidad de Pokemons en cada generación
st.header('POKEMONS POR GENERACIÓN')
gen_counts = pokemon_data['Generation'].value_counts()

# Convertir a porcentajes
gen_percents = gen_counts / gen_counts.sum() * 100

# Crear la gráfica de pastel
fig = px.pie(names=gen_percents.index, values=gen_percents.values)

# Mostrar la gráfica
st.plotly_chart(fig)

# ==============================================================


# ================= CONTADOR TIPOS DE POKEMON =========================

st.header('SUB-TIPOS DE POKEMON EN CANTIDAD')
# Contar la cantidad de Pokemons en cada SUB-tipo
type_counts = pokemon_data['Type 2'].value_counts()

# Crear la gráfica de barras
fig = px.bar(x=type_counts.index, y=type_counts.values)

# Establecer los títulos de la gráfica
fig.update_layout(title='No todos los pokemons tienen un 2 tipo, pero estos son los más frecuentes:',
                  xaxis_title='Tipo', yaxis_title='Cantidad')

# Mostrar la gráfica
st.plotly_chart(fig)

# ==============================================================


# ================= TABLA POKEMONS LEGENDARIOS =========================

st.header('TABLA POKEMONS LEGENDARIOS')
# Seleccionar los Pokemons legendarios
legendary_pokemons = pokemon_data.loc[pokemon_data['Legendary'] == True]

# Mostrar la tabla
st.write(legendary_pokemons)

# ==============================================================


# ================= SALUD MINIMA FILTRADO POKEMON =========================


# ==============================================================


# SELECCIONAR LA GENERACON DE POKEMON
# def select_generation():
#     st.sidebar.header("Selecciona la generación")
#     st.sidebar.slider(
#         "La generaciones van de la 1 a la 6", min_value=1, max_value=6)


# SELECCIONAR VALOR VIDA
# st.sidebar.header("Selecciona el rango de vida")
# columnas_hp = st.sidebar.columns(2)
# hp_min = columnas_hp[0].number_input(
#     "Salud minima", value=pokemon_data['HP'].min())
# HP_max = columnas_hp[1].number_input(
#     "Maximum HP", value=pokemon_data['HP'].max())
# if HP_max < hp_min:
#     st.error("La salud máxima no puede ser menor que la mínima!")
# else:
#     st.success("Parametros correctos!")
#     subset_HP = pokemon_data[(pokemon_data['HP'] <= HP_max) & (
#         hp_min <= pokemon_data['HP'])]

# BARRA DE CARGA
# progress_bar = st.progress(0)
# progress_text = st.empty()
# # definir el tiempo de espera
# for i in range(101):
#     time.sleep(0.1)
#     progress_bar.progress(i)
#     progress_text.text(f"Progress: {i}%")
