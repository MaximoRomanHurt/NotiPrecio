# Utilizamos un diccionario para configurar la conexión a la base de datos

DB_CONFIG = {
    'dbname': 'Products', # En PostgreSQL, la base de datos se llama Products
    'user': 'postgres',
    'password': "tu_contraseña_aquí", # Reemplaza con tu contraseña real
    'host': 'localhost',
    'port': '5432'
}

# En PostgreSQL, la base de datos se llama Products
# La tabla tiene 5 campos:
# - id_producto: SERIAL PRIMARY KEY
# - nombre: VARCHAR(100)
# - categoria: VARCHAR(100)
# - unidad: VARCHAR(50)
# - precio: NUMERIC(10,2)
# - fecha_registro: DATE
