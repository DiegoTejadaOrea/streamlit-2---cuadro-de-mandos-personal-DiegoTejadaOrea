import json
import pandas as pd

df_pokemon = pd.read_csv('pokedex.csv')

with open('datosImagenes.json') as f:
    data = json.load(f)

df_imagenes = pd.DataFrame.from_dict(data)
df_unido = pd.merge(df_pokemon, df_imagenes, on='nombre', how='inner')
df_unido.to_csv('datos_pokemon_unidos.csv', index=False)
