from etl import save_movies_to_db

# Ejecutar el proceso ETL
if __name__ == "__main__":
    print("🚀 Iniciando proceso ETL...")
    save_movies_to_db()
    print("✅ Proceso completado")
