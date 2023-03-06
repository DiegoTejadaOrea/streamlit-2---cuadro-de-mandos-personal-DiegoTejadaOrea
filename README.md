# 📈 Cuadro de mandos personal 📊
 
> Usa este repositorio para crear un cuadro de mandos personal con Streamlit. Documenta los siguientes apartados del README.
> Incluye en tu README la url de donde has publicado tu aplicación. Pon la `url` también en el `About` de tu repositorio.

## Objetivo
Diseño de un cuadro de mandos personal para visualización de datos filtrados, que tras la ejecucion muestar en base a unos datos personales el pokemon al que se ajustan los datos introducidos.

## Los datos
Los datos son las caracteristicas de los pokemons:
- Nombre
- Total
- HP
- Attack
- Defense
- Sp. Atk
- Sp. Def
- Speed
- Url_img
- Generation
- Type 1
- Type 2

## Búsqueda de los datos y documentación de los datos
He escogido los datos de la web https://pokemondb.net/pokedex/all, que es una base de datos de todos los pokemons que existen en la franquicia de videojuegos Pokemon. Para la extraccion de datos he realizado programas de escraping en python, que me han permitido extraer los datos de la web y guardarlos en un archivo csv.

En la carpeta datos estan todos los ficheros de datos que he utilizado en el proceso, el archivo final utilizado para la aplicacion es el archivo `datos_pokemon_actualizados.csv`.

## Prepara tu aplicación.
La aplicacion se llama `app.py` y en `requirements.txt` tienes las dependencias que necesitas para ejecutarla. Puedes usar `pipreqs` para generar el fichero de dependencias. 

## Carga y análisis de conjunto de dato con pandas
Los datos se van actualizando cada vez que se ejecuta el programa, por lo que no es necesario cargarlos en un dataframe, sino que se cargan directamente en el dataframe. Conforme seleccionas los datos, se van actualizando los datos del dataframe y se muestra el pokemon que se ajusta a los datos introducidos.

## Visualización de los datos
El dato final es una imagen del pokemon que se ajusta a los datos introducidos. Pero tambien se muestran los datos del pokemon escritos en la pantalla.

## Diseña la interacción que van a tener tus datos
Los filtros estan en el sidebar.
Son mediante un slider para los datos numericos y mediante un selectbox para los datos categoricos.


## Publica la aplicación.
Publica la aplicación en Streamlit Cloud, en Heroku o en el servicio que prefieras https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app
