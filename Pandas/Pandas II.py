import pandas as pd 
df = pd.read_csv("C:/Users/usuario/Desktop/archivos_base_python_data_science_big_data_esencial/basedatos2008.csv")

df["ArrDelay"].head()
df[100:110] #consulta las filas de ese rango

df[df["ArrDelay"] >= 60].head() # filtro concreto, ver retrasos de igual o mas de 60min 

df[df["Origin"] == "ATL"].head() # vuelos de origen ATL

#Vuelos que tienen origen en ATL y(&) retraso de mas de 60 min 
df[(df["Origin"] == "ATL") & (df["ArrDelay"] > 60)].head()

#diferentes origenes a la vez : 
df[df.Origin.isin(["HOU", "ATL"])].head()

#datos no disponible seria: "not avalible = .na" --- filtramos por columna co retraso --- vuelos sin retraso
df[pd.isna(df["ArrDelay"])].head()

#para contar esots vuelos sin retrasos: 
len(df[pd.isna(df["ArrDelay"])])