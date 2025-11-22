import pandas as pd

# Esta es una función que lee un archivo y lo convierte en un dataframe
# file_path es el path del archivo que se va a leer
# file_path: str es el path del archivo que se va a leer
# return es el dataframe que se obtiene del archivo
def read_file(file_path: str):
    if file_path.lower().endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.lower().endswith(('.xls', '.xlsx')):
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Formato no soportado. Usa .csv o .xlsx")
    # Opcional: asegurar nombres de columnas esperadas
    return df
