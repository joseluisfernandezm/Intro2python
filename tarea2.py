import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,3*np.pi,0.1)#con esta linea definimos el intervalo de o a 3*pi en saltos de 0.1 es el tipo que aparece en el depurador dtype('float64')
animals=['cat','dog','monkey']#lista de cadenas de caracteres, segun el depurador len es 3
y_sin=np.sin(x)