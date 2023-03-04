import requests
from bs4 import BeautifulSoup
import pandas as pd

# Realizar una solicitud GET a la página web
url = 'https://pokemondb.net/pokedex/all'
response = requests.get(url)

# Analizar el HTML de la página web utilizando Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar la tabla de la lista de Pokémon
table = soup.find('table', {'id': 'pokedex'})

# Extraer los encabezados de la tabla
headers = []
for th in table.find_all('th'):
    headers.append(th.text)

# Extraer los datos de la tabla
data = []
for tr in table.find_all('tr'):
    row = []
    for td in tr.find_all('td'):
        row.append(td.text.strip())
    if row:
        data.append(row)

# Crear un marco de datos pandas con los encabezados y los datos extraídos
df = pd.DataFrame(data, columns=headers)

# Guardar el marco de datos en un archivo CSV
df.to_csv('pokedex.csv', index=False)
