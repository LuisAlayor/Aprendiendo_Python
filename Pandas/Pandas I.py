import pandas as pd
df = pd.read_csv("C:/Users/usuario/Desktop/archivos_base_python_data_science_big_data_esencial/basedatos2008.csv", nrows = 10000)
df.head() #5 primera filas de la base de datos
df.tail() #5 ultimas filas de la base de datos

#desordenar el data frame(df) la base de datos
df.sample(frac = 1) 

# para guardar es:
df1 = df.sample(frac =1 )
df1.columns #obtenemos informacion de una columna que existe
df1.DepTime # nos muestra la info de la columna que queremos
df.types #tipo de datos
df.values #valores de las columnas en forma de array

#guardar base de datos en otro data frame
df2 = df.head(10) 
df(5)
