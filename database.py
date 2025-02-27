# Description: Conexión a la base de datos PostgreSQL
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", 5432)

def connect_db():
    try:
        print(f"🔑 Conectando con: {DB_USER}@{DB_HOST}:{DB_PORT}, DB: {DB_NAME}")
        print(f"🔑 Contraseña (solo longitud): {len(DB_PASS) if DB_PASS else 'No definida'}")
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT,
            client_encoding="UTF8"  # Fuerza UTF-8 para evitar errores de codificación
        )
        conn.set_client_encoding('UTF8')  # 🔥 Asegurar UTF-8 manualmente
        print("✅ Conectado a la base de datos")
        return conn
    except Exception as e:
        print(f"❌ Error al conectar a la base de datos: {e}")
        return None
