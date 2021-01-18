import pandas as pd
df = pd.read_csv("C:/Users/usuario/Desktop/archivos_base_python_data_science_big_data_esencial/basedatos2008.csv")

# Agrupa por categoria dayofweek y nos da los valores del ArrDelay
# describe muestra un resumen estadistico para cada dia de la semana
#1=lunes, 2=martes ....etc
df.groupby(by = "DayOfWeek")["ArrDelay"].describe()

# las columnas tiene qu ser del mismo tipo
# agrupa por categoria la columna que queramos, en este caso comparamos dos variables
df.groupby(by = "DayOfWeek")["ArrDelay","DepDelay"].mean()

# rangode valores (agrupacion) para cada dia de la semana, de los valores ArrDelay (max-min)
df.groupby(by = "DayOfWeek")["ArrDelay"].max() - df.groupby(by = "DayOfWeek")["ArrDelay"].min()

#nueva base de datos - con los vuelos de las ciudades ATL y HOU
dfATLHOU = df[df.Origin.isin(["ATL","HOU"])]

# los valores de ArrDelay los agrupamos por DayofWeek y Origin, obtenemos las medias
dfATLHOU.groupby(by = ["DayOfWeek", "Origin"])["ArrDelay"].mean() #asi comparamos en que ciudades los vuelos llegan mas retrazados y que dias de la semana

dfATLHOU.groupby(by = ["Origin", "DayOfWeek"])["ArrDelay"].mean() # lo mismo que el anterior solo que con otro orden de datos

#guardamos las bases de datos anteriores en una variable
mygroupby = dfATLHOU.groupby(by = ["Origin", "DayOfWeek"])["ArrDelay"].mean()

# ahora que esta guardado podemos hacer operaciones o consultas como los datos estadisticos:
mygroupby.describe()
