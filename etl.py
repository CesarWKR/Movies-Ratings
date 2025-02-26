import pandas as pd
from tmdb_api import get_popular_movies
from sqlalchemy import create_engine
import psycopg2
from database import connect_db
from database import DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT

def save_movies_to_db():
    conn = connect_db()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        print("✅ Conexión establecida. Creando tabla...")

        # Crear tabla si no existe con release_date como DATE
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS movies (
                id SERIAL PRIMARY KEY,
                tmdb_id INT UNIQUE NOT NULL,
                title TEXT NOT NULL,
                release_date DATE,
                popularity FLOAT
            )
        """)
        conn.commit() # Confirmar cambios en la base de datos
        print("✅ Tabla verificada.")

        # Obtener datos de la API
        movies = get_popular_movies(num_pages=100)
        if not movies:
            print("⚠ No se encontraron películas para insertar.")
            return
        
        print(f"📊 Se encontraron {len(movies)} películas.")

        # Revisar los datos que estamos insertando
        for movie in movies[:5]:  # Solo las primeras 5 para evitar spam en la consola
            print(f"🎬 {movie['title']} (ID: {movie['id']}, Fecha: {movie['release_date']}, Popularidad: {movie['popularity']})")

        # Insertar datos evitando duplicados
        for movie in movies:
            clean_title = movie["title"].encode("utf-8", "ignore").decode("utf-8")  # Limpiar caracteres problemáticos
            cursor.execute("""
                INSERT INTO movies (tmdb_id, title, release_date, popularity) 
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (tmdb_id) DO NOTHING
            """, (movie["id"], 
                  clean_title,
                  movie["release_date"], 
                  movie["popularity"]))

        conn.commit()
        print("✅ Datos guardados en la base de datos")

    except Exception as e:
        print(f"❌ Error al guardar datos: {e}")

    # Cerrar la conexión a la base de datos
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            print("🔌 Conexión cerrada correctamente")

if __name__ == "__main__":
    save_movies_to_db()
    
