# Importamos las librerías necesarias
import pandas as pd # para manipular datos tabulares
import pandas_gbq # para interactuar con Google BigQuery
from google.cloud import bigquery # para acceder al servicio de BigQuery
from google.oauth2 import service_account # para autenticarnos con Google Cloud Platform

# Definimos las variables que contienen la información de la hoja de cálculo de Google Sheets
SHEET_ID = '17TUqLPowoHFiu6PGmHHs6oX5jTpz3C5N6vJ014eUOwA' # el identificador único de la hoja de cálculo
SHEET_NAME = 'dataset' # el nombre de la hoja que contiene los datos
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}' # la url que nos permite obtener los datos en formato csv

# Leemos los datos desde la url y los guardamos en un dataframe de pandas
df = pd.read_csv(url)

# Definimos la ruta del archivo json que contiene las credenciales de GCP
key_path = 'GCP credentials path to json key archive'

# Creamos un objeto de credenciales a partir del archivo json
credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

# Definimos las variables que contienen la información del proyecto, el conjunto de datos y la tabla de BigQuery
project_id = "PRUEBA_R5" # el identificador del proyecto de GCP
dataset = "prueba" # el nombre del conjunto de datos de BigQuery
table = "ventas" # el nombre de la tabla de BigQuery

# Cargamos el dataframe de pandas en la tabla de BigQuery, usando las credenciales y el identificador del proyecto
pandas_gbq.to_gbq(df, destination_id = f'{dataset}.{table}', project_id=f'{project_id}', credentials= credentials)