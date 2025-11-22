import psycopg2 # Importamos la librería para conectarnos a la base de datos
from db.config import DB_CONFIG

def create_table():
    conn = psycopg2.connect(**DB_CONFIG) # Conexión a la base de datos
    cur = conn.cursor() # Creamos un cursor para ejecutar las consultas
    # un cursor es un objeto que nos permite ejecutar consultas y obtener resultados
    cur.execute("""
        CREATE TABLE IF NOT EXISTS producto (
            id_producto SERIAL PRIMARY KEY,
            nombre VARCHAR(100),
            categoria VARCHAR(100),
            unidad VARCHAR(50),
            precio NUMERIC(10,2),
            fecha_registro DATE
        );
    """)
    conn.commit() # Commit para guardar los cambios en la base de datos
    cur.close() # Cerramos el cursor
    conn.close() # Cerramos la conexión a la base de datos

def insert_data(df): # Pasamos como parámetro el dataframe que contiene los datos
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    # Creamos un bucle para insertar los datos en la base de datos
    # Los iteradores del bucles son las filas del dataframe
    # _ es el índice de la fila
    # row es la fila del dataframe
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO producto (nombre, categoria, unidad, precio, fecha_registro)
            VALUES (%s, %s, %s, %s, %s);
        """, (row.get('nombre'), row.get('categoria'), row.get('unidad'),
              row.get('precio'), row.get('fecha_registro')))
    conn.commit()
    cur.close()
    conn.close()

def get_all_data():
    """Obtiene todos los registros de la tabla producto"""
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT * FROM producto ORDER BY id_producto;")
    # desc[0] es el nombre de la columna
    # se trata de un bucle que recorre las columnas de la consulta
    # columns es una lista de los nombres de las columnas
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall() # Esto es para obtener todos los registros de la tabla
    cur.close() # Cerramos el cursor
    conn.close() # Cerramos la conexión a la base de datos
    return columns, rows # Devolvemos las columnas y los registros