import numpy as np

#Genere un script tarea1.py que importe el paquete numpy con el nombre np y muestre la version de este paquete
print("La version de numpy es la: "+str(np.__version__))

#1. Cree un vector de tamaño 10x1 con valores aleatorios y muestrelo por pantalla Utilice numpy.random.random
array_random=np.random.random((10,1))
print("Vector aleatorio de tamaño 10x1:")
print(array_random)

#2. Posteriormente cree un array bidimensional de ceros con tamaño 10x10 Utilice numpy.zeros
array_zeros=np.zeros((10,10))
print("\nArray bidimensional de ceros de tamaño 10x10:")
print(array_zeros)

#3. Haga que las posiciones de los extremos del array bidimensional tengan el valor 1 Utilice indexacion de matrices
array_bordes=array_zeros.copy()#OJO PARA COPIAR QUE SI NO LO HACEMOS ASI SE MANTIENEN ENLAZADOS

array_bordes[0, :] = 1
array_bordes[-1, :] = 1
array_bordes[:, 0] = 1
array_bordes[:, -1] = 1

print("\nArray con los extremos con valor 1:")
print(array_bordes)

#4. Genere un nuevo array bidimensional con los elementos en posiciones con indices impares filas y columnas del array obtenido en el apartado 3
#Utilice numpy.array con el argumento copy=True e indexacion de matrices
'''
los pasos de la indexacion de matreices en numpy permiten seleccionar elemntos en intercalos regulares dentro de las dimansiones
La notacion [inicio:fin:paso]se utiliza para controlar como se seleccionan los elemntos a lo largo de un eje particular
En tu caso especifico estas usando esta notacion para seleccionar elemntos en posiciones de indices impares en un array bidimensional

'''
array_impar = np.array(array_bordes[1::2, 1::2], copy=True) #alternativa
# array_impar=array_bordes[1::2,1::2].copy()
print("\nArray de los indices impares:")
print(array_impar)

#5. Genere un nuevo array bidimensional con los elementos en posiciones con indices pares filas y columnas del array obtenido en el apartado 3
#Utilice numpy.array con el argumento copy=True e indexacion de matrices

array_par = np.array(array_bordes[0::2, 0::2], copy=True) #alternativa
# array_par=array_bordes[0::2,0::2].copy()
print("\nArray de los indices pares:")
print(array_par)


#6.Partiendo del array obtenido en el ejercicio 3, cambie el valor 3 la posicion definida por la columna tercera y dila segunda. Muestra por pantalla la segunda fila
array_intercambio=array_bordes.copy()
array_intercambio[2,0:10]=3
array_intercambio[0:10,3]=3
print("\nArray de intercambio:")
print(array_intercambio)
print("Sacamos por pantalla solo la segunda fila:")
print(array_intercambio[2,:])#revisar si es [1,:]
