import numpy as np

#creación de un array
valoraciones = np.array([  [8,7,8,5], [2,6,8,1], [8,8,9,5]  ])
valoraciones
#llamar a in dato de una fila y columna
valoraciones[0][1] # = valoraciones[0,1]

#creación de un array que contiene mas arrays (3,2,4)
valoraciones2 = np.array([ [[8,7,8,5], [2,5,5,2]], [[2,6,8,4], [8,9,7,4]],  [[8,8,9,3], [10,9,10,8]]])
valoraciones2
#llamar a in dato de una fila y columna
valoraciones2[0,1,2]

# arrays con todos los valores 0, con 2 arrays dentro de un array dentro de un array de 4 repetido 10 veces,
# de dimensiones 3x5 
np.zeros((3,2,4,10,5))

# unimos arrays de iguales dimensiones
valoraciones2 + np.ones((3,2,4))
#media de la array
np.mean(valoraciones2) 
np.mean(valoraciones2, axis=0)
np.mean(valoraciones2, axis=1)
np.mean(valoraciones2, axis=2)

#nueva array en este caso indicamos los valores y despues la medida del array 3 arrays de 2x2
np.reshape([1,2,3,4,5,6,7,8,9,10,11,12], (3,2,2))
np.median(df["Columna1"])