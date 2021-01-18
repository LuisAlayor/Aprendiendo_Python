import pandas as pd
df = pd.read_csv("C:/Users/usuario/Desktop/archivos_base_python_data_science_big_data_esencial/basedatos2008.csv")

#declaramos una columna nueva que sera el redondeo del retraso
df["HoursDelay"] = round(df["ArrDelay"]/60)
df["HoursDelay"].head() #ves la columna

#eliminamos columna
del(df["HoursDelay"])

#Eliminar varias columnas a la vez:  .drop - tenemos que especificar el eje "axis=1"
df.drop(["Diverted", "Cancelled", "Year"], axis = 1)
df = df.drop(["Diverted", "Cancelled", "Year"], axis = 1) #guardamos los cambos en la variable df

#lo mismo que la funcion anterior (para borrar) sin declararlo dentro de una variable añadimos inplaces=true
df.drop(["Diverted", "Cancelled", "Year"], axis = 1, inplaces=True) 
df.drop(0) #eliminamos la primera fila de la base de datos sin guardar
df.drop(range(0,1000)) #eliminamos en rango sin guardar

#creamos base de datos
dfATL = df[df.Origin == "ATL"] #con origen en ATL
dfHOU = df[df.Origin == "HOU"] #con origen en HOU

#sumamos estos dos DF:
newdf= dfATL.append(dfHOU) 
newdf.Origin #revisamos la columna origins del newdf

