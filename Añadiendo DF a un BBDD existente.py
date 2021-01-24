import pandas as pd
import numpy as numpy
import os

df = pd.read_csv("C:/Users/usuario/Desktop/Pruebas/basedatos2008.csv")
df2= df.head(500)
df3=df.head(10000)

path = "C:/Users/usuario/Desktop/Pruebas/example.csv"
df2.to_csv('example.csv', index = None, mode="a", header= not os.path.isfile(path))