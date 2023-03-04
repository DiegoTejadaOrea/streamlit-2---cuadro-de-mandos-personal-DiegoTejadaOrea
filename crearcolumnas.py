import pandas as pd

# Cargar los datos de los Pokémon en un DataFrame
df = pd.read_csv(
    "https://raw.githubusercontent.com/DWES-LE/streamlit-2---cuadro-de-mandos-personal-DiegoTejadaOrea/main/datos_pokemon_unidos.csv")

# Dividir los valores de la columna "Type" por el espacio en blanco
tipos_separados = df["Type"].str.split(" ", expand=True)

# Asignar el primer tipo a la columna "Type 1"
df["Type 1"] = tipos_separados[0]

# Asignar el segundo tipo (si existe) a la columna "Type 2"
df["Type 2"] = tipos_separados[1]

# Eliminar la columna original "Type"
df = df.drop(columns=["Type"])

# Guardar los datos en un nuevo archivo CSV
df.to_csv("datos_pokemon_actualizados.csv", index=False)

# Mostrar un mensaje indicando que el archivo se ha guardado correctamente
print("¡El archivo se ha guardado correctamente!")
