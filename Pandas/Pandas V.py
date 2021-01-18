import pandas as pd
df = pd.read_csv("C:/Users/usuario/Desktop/archivos_base_python_data_science_big_data_esencial/basedatos2008.csv", nrows = 1e6)

# duplicar un df y guardarla en una nueva variable (datos duplicados)
dfduplicate = df.append(df) # agrego la base de datos df a la base existente 

# lo reordenamos 
dfduplicate = dfduplicate.sample(frac=1)

# creamos una base de datos nueva y limpiamos los duplicados
dfclean = dfduplicate.drop_duplicates()
#  hacemos un conteo y comprobamos si hay la misma cantidad de filas del nuevo DF con el DF original - 
len(dfclean) == len(df)
#dignifica que el DF oiriginal tenia filas repetidas, por eso el valor es false
len(dfclean) 


# eliminar datos especificos  - columnas especificas
dfclean.drop_duplicates(subset ="DayofMonth")  #buscara duplicados en la fila que indiquemos

# gestion de datos faltantes- indicamos que borre las filas que tengan un dato faltante =Not Avalible= na
df.dropna() # nos dara una tabla vacia

# no seamos radiales y usamos otra funcion: 
df.dropna(thresh = 25) #informacon minima por fila - almenos que cada fila tenga almenos 25 datos

# como maximo total de columnas - 2 (otra orma es poner 30-2)(pero asi es mejor si no sabemos el total de columnas)
df.dropna(thresh = len(df.columns)-2) 

# filtramos por una columna en concreto
df.dropna(subset= ["CancellationCode"]) # la tabla no tendra na en la columna CancellationCode
