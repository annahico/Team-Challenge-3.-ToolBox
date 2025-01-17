import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Configuración de estilo
sns.set(style='whitegrid')

# Cargar los datos de las películas de Harry Potter
df_chapters = pd.read_csv(
    './Harry_Potter_Movies/Chapters.csv', encoding='latin1')
df_characters = pd.read_csv(
    './Harry_Potter_Movies/Characters.csv', encoding='latin1')
df_data_dict = pd.read_csv(
    './Harry_Potter_Movies/Data_Dictionary.csv', encoding='latin1')
df_dialogue = pd.read_csv(
    './Harry_Potter_Movies/Dialogue.csv', encoding='latin1')
df_movies = pd.read_csv('./Harry_Potter_Movies/Movies.csv', encoding='latin1')
df_places = pd.read_csv('./Harry_Potter_Movies/Places.csv', encoding='latin1')
df_spells = pd.read_csv('./Harry_Potter_Movies/Spells.csv', encoding='latin1')

# Mostrar los primeros registros de las películas
print("Primeros registros de las películas de Harry Potter:")
print(df_movies.head())

# Análisis de la duración de las películas


def analizar_duracion(df):
    plt.figure(figsize=(10, 6))
    # Cambié 'Title' por 'Movie Title'
    sns.barplot(x='Movie Title', y='Runtime', data=df, palette='viridis')
    plt.title('Duración de las Películas de Harry Potter')
    plt.xlabel('Título de la Película')
    plt.ylabel('Duración (minutos)')
    plt.xticks(rotation=45)
    plt.show()

# Análisis de puntuaciones de Rotten Tomatoes


def analizar_puntuaciones(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Movie Title', y='Release Year', data=df,
                palette='coolwarm')  # Cambié 'Title' por 'Movie Title'
    plt.title('Año de estreno de las Películas de Harry Potter')
    plt.xlabel('Título de la Película')
    # plt.ylabel('Puntuación (%)')
    plt.xticks(rotation=45)
    plt.show()

# Función para clasificar personajes


def clasificar_personaje(datos_personaje):
    if datos_personaje['lealtad'] > 70:
        return 'Gryffindor'
    elif datos_personaje['astucia'] > 70:
        return 'Slytherin'
    elif datos_personaje['inteligencia'] > 70:
        return 'Ravenclaw'
    else:
        return 'Hufflepuff'

# Clasificación de los personajes


def clasificar_personajes(df_personajes):
    df_personajes['Casa'] = df_personajes.apply(clasificar_personaje, axis=1)
    return df_personajes

# Función principal


def main():
    # Analizar duración
    analizar_duracion(df_movies)

    # Analizar puntuaciones
    analizar_puntuaciones(df_movies)

    # Clasificar personajes (suponiendo que tenemos un DataFrame de personajes)
    try:
        df_personajes = pd.read_csv(
            'datos_personajes_harry_potter.csv', encoding='utf-8')
        df_clasificados = clasificar_personajes(df_personajes)
        print("Personajes clasificados:")
        print(df_clasificados)
    except FileNotFoundError:
        print("Archivo de personajes no encontrado. Omite la clasificación de personajes.")


if __name__ == "__main__":
    main()
