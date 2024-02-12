import matplotlib.pyplot as plt
import numpy as np
from skimage import io, img_as_float32, color

#1. Lea y visualice la imagen RGB 

img=io.imread('A_small_cup_of_coffee.jfif')

#2. Muestre por consola las dimensiones, el tipo y el valor maximo de la imagen
print('El tipo de la imagen es: '+str(img.dtype))
print('El tamaño de la imagen es: '+str(img.shape))
print('El valor maximo de la imagen es: '+str(np.max(img)))

#mostrar imagen
plt.imshow(img)
plt.show() 

#3. Posteriormente cambie el tipo a float y normalice la imagen para que este en el rango de 0 a 1, mostrar las dimensiones y tipo

floatImage=img_as_float32(img)

print('\nEl tipo de la imagen es: '+str(floatImage.dtype))
print('El tamaño de la imagen es: '+str(floatImage.shape))
print('El valor maximo de la imagen es: '+str(np.max(floatImage)))

#4. Posteriormente transforme la imagen al espacio de color HSV

image_hsv = color.rgb2hsv(img)

redChannel = image_hsv [:,:,0] # canal rojo
greenChannel = image_hsv [:,:,1] # canal verde
blueChannel = image_hsv [:,:,2] # canal azul


#5. Visualice cada canal en una sola ventana como una imagen en escala de grises

plt.figure(1)
plt.imshow( redChannel , cmap ='gray'); plt.title ('Rojo')
plt.show() 
plt.figure(2)
plt.imshow( greenChannel , cmap ='gray'); plt.title ('Verde')
plt.show() 
plt.figure(3)
plt.imshow( blueChannel , cmap ='gray'); plt.title ('Azul')
plt.show() 


#Con subplot
# plt.figure(1)
# plt.subplot (1 , 3 , 1)
# plt.imshow( redChannel , cmap ='gray'); plt.title ('Rojo')
# plt.subplot (1 , 3 , 2)
# plt.imshow( greenChannel , cmap ='gray'); plt.title ('Verde')
# plt.subplot (1 , 3 , 3)
# plt.imshow( blueChannel , cmap ='gray'); plt.title ('Azul')
# plt.show() 

