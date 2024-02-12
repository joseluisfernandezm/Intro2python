import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
from skimage import data

#1. Lea y visualice la imagen en escala de grises brick disponible en el paquete skimage.data

img=data.brick()
plt.imshow(img)
plt.show()

#2. Muestre por consola las dimensiones de la imagen y el tipo

print('El tipo de la imagen es: '+str(img.dtype))
print('El tamaño de la imagen es: '+str(img.shape))

#3. Aplique las siguientes operaciones a la imagen leida y visualizacion de los resultados

# deteccion de bordes con sobel
sx = nd.sobel(img , axis = 0 , mode = 'constant') # bordes horizontal COMPROBAR QUE NO SE QUIERE EL VERTICAL
plt.imshow(sx)
plt.show()

# suavizado con un nucleo Gausiano
sigma = 10
img_gauss = nd.gaussian_filter (img , sigma = sigma )
plt.imshow(img_gauss)
plt.show()
