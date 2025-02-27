# Obtiene películas populares de la API de TMDb
import requests
from config import API_KEY, BASE_URL

def get_popular_movies(num_pages=1):
    """ Obtiene películas populares de varias páginas """
    all_movies = []  # Lista para almacenar todas las películas
    
    for page in range(1, num_pages + 1):  # Itera sobre varias páginas
        url = f"{BASE_URL}/movie/popular"
        params = {"api_key": API_KEY, "language": "es-ES", "page": page}
        response = requests.get(url, params=params)

        if response.status_code == 200:  # Indica que la petición fue exitosa
            movies = response.json()["results"]
            all_movies.extend(movies)  # Agrega las películas a la lista
        else:
            print(f"Error: {response.status_code}, {response.text}")
            break  # Detiene la ejecución si hay un error

    return all_movies

# Prueba la extracción
if __name__ == "__main__":
    movies = get_popular_movies(num_pages=3)  # Obtener películas de 3 páginas
    print(f"Se obtuvieron {len(movies)} películas.")
    print(movies[:5])  # Muestra las primeras 5 películas