import numpy as np
import matplotlib.pyplot as plt
# from skimage import data Opcion del profe
import skimage as sk

#1. Cree una lista vacio con el nombre lista_img

lista_img=[]

#2. Lea la imagen astronaut y añadala a la lista

img_astro=sk.data.astronaut()
# plt.imshow(img_astro)
# plt.show()

#3. Lea la imagen camera y añadala a la lista

img_came=sk.data.camera()
# plt.imshow(img_came)
# plt.show()

lista_img.append(img_astro)
lista_img.append(img_came)

#4. Cree un array bidimensional de ceros con tamaño 10x10 y añadala a la lista, identifica si la imagen es de color o gris

array=np.zeros((10,10))
lista_img.append(array)

'''
Con este bucle veo cuantos elementos tiene el atributo shape de cada uno de los elementos que metemos en la lista, si tiene
3 elementos signica que tiene tres planos de color y por tanto es de color y si no pues no tiene tercer argumento y entonces
te sale blanco y negro
'''
for elemento in lista_img:
    if(len(elemento.shape)==3):
        print('La imagen es a color al tener 3 canales RGB')
    else:
        print('La imagen es en blanco y negro')

#5. Recorra la lista mediante un bucle utilizando la instruccion range, muestre por consola las dimensiones, imagenes, tipo y valor maximo junto a la visualizacion

#bucle que utiliza la instruccion range que muestra caracteristicas de la imagen

for valor in range(0,len(lista_img)):
    print('El tipo de la imagen es: '+str(lista_img[valor].dtype))
    print('El tamaño de la imagen es: '+str(lista_img[valor].shape))
    print('El valor maximo de la imagen es: '+str(np.max(lista_img[valor])))
    plt.imshow(lista_img[valor])
    plt.show()

#6. Cree una nueva lista con los dos primeros elementos de la lista y que muestra el numero de elementos de esta nueva lista

lista_nueva=[]
lista_nueva.append(lista_img[0].copy())
lista_nueva.append(lista_img[1].copy())
print('El tamaño de la lista es: '+str(len(lista_nueva)))