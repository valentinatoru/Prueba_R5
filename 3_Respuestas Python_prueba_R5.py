# Importamos las librerías necesarias
import pandas as pd 

SHEET_ID = '17TUqLPowoHFiu6PGmHHs6oX5jTpz3C5N6vJ014eUOwA'
SHEET_NAME = 'dataset' 
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}' 
df = pd.read_csv(url)


#¿Cuáles son las tiendas con compras de al menos 100 clientes diferentes?
resultado_1 = df.groupby('codigo_tienda')['num_documento_cliente'].nunique().reset_index()
resultado_1=resultado_1[resultado_1['num_documento_cliente']>=100]
print(resultado_1)

#¿Cuáles son los 5 barrios donde la mayor cantidad de clientes únicos realizan compras en tiendas tipo 'Tienda Regional'?
resultado_2= df[df['tipo_tienda']=='Tienda Regional']
resultado_2 = resultado_2.groupby('nombre_barrio')['num_documento_cliente'].nunique().reset_index()
resultado_2= resultado_2.sort_values('num_documento_cliente', ascending=False)
resultado_2=resultado_2.head(5)
print(resultado_2)