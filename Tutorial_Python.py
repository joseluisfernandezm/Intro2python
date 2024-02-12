'''Este archivo de python va a tratar de ser un tutorial en que probaremos diferentes codigos que
 nos permitan conocer lo basico de este lenguaje de programacion'''

 # ----------------TIPOS BÁSICOS Y DECLARACION DE VARIABLES----------------

'''nosotros vamos a declarar variables de una manera muy sencilla'''

x=3 #en este lenguaje no es necesario el ; aqui declaramos un entero
x=int(3)# declaremos un entero haciendo una especie de cast forzando a ese tipo de dato
x=3.0 #con esto decalaramos un float
x=float(3.0)#con esto hacemos lo mismo que con lo de el cast de antes

#NOTA IMPORTANTE EN PYTHON NO FUNCIONA EL X++ O X--

x=x-1 # esta es la forma de restar uno en python
print(x)

#----------------BOOLEANS----------------

t=True
f=False

print(type(t))#type es un metodo que nos dice la clase del objeto que introduciomos
print(t and f)#operacion logica and t and f =f
print(t or f)#el resultado es true
print(not t)
print(t!=f)

#----------------Strings----------------

#declaracion de las cadenas (son objetos)
hello='hello'
world='world'
print(hello)
print(world)
print(len(hello))
hw=hello+' '+world#se concatena con mases como en java
print(hw)
hw12='%s %s %d'%(hello, world, 12)
print(hw12)

s="hello"
print(s.capitalize())#metodo del objeto cadena s que pone la primera letra en mayuscula
print(s.upper())#metodo del objeto cadena s que pone la cadena en mayusculas
print(s.rjust(7))#pone en nuestro caso 7 espacios en blanco a la inzquierda
print(s.center(7))#muestra el texto centrado, rellena con espacios 
print(s.replace('l','(ell)'))#sustituye las l por ell

#----------------CONTENEDORES----------------

#LISTAS

xs=[3,1,2]
print(xs,xs[2])#PARA CONCATENAR ENTEROS EN UN PRINT USAMOS COMAS Y NO + ESTOS SON SOLO PARA STRINGS
print(xs[-1])#los indices negativos cuentan hacia atras en la lista sacando el 2
xs[2]='foo'#LAS LISTAS EN PYTHON PUEDEN CONTENER ELEMENTOS DE DISTINTOS TIPOS ES COMO EL ARRAYLIST DE JAVA
print(xs)

#la lista xs es un objeto de tipo list entonces tiene sus pripios metodos como pasana en Java

xs.append('bar')#con append añadimos un elemento mas a la lista
print(xs)
x=xs.pop()#con pop eliminamos el ultimo elemento de la lista y lo retornamos
print(x)
print(xs)
xs.insert(2,'n')#la diferencia con append es que con insert yo elijo en que posicion añado el elemento
print(xs)#vemos como el resto de elementos se desplazan a la derecha
xs.remove('n')#con remove busca de entre todos los elemetos los que coincidan con el argumento del metodo y lo elimina
print(xs)#los elementos se recolocan no quedan posiciones de memoria vacias
print('Numero de elementos de la lista '+str(len(xs)))#hacemos un casta str para que pueda concatenarse a la primera cadena con un +

#vamos a ver ahora el acceso a varios elementos de una lista de manera simultanea

nums=list(range(5))#con esta linea creamos nums que es un objeto de tipo list pasando al constructor un rango del 0 al 5
print(nums)
print(nums[2:4])#de esta manera me da los numeros de la posicion 2 a la 4 sin incluir la posicion de cierre esto se parece a matlab
print(nums[2:])#me imprime todos desde la posicion 2
print(nums[:2])#me imprime todos hasta la posicion 2
print(nums[:])#me imprime todos los elemntos
print(nums[:-1])#los indices pueden ser negarivos diciendo que me imprima todos hasta el ultimo por la derecha el cual no quiero que me incluya
nums[2:4]=[8,9]#sobreescribimos los elementos de la posicion 2 y 3
print(nums)

#Ahora vamos a ver los bucles sobte listas

#Primera opcion 

animals=['cat','dog','monkey']

for animal in animals:
    print(animal)

#esta opcion es como la de Java en la que creamos un objeto auxiliar y lo vamos cambiando en cada iteracion
#nos va a mostrar a cada animal de la lista en una linea nueva

#Segunda opcion 

for idx, animal in enumerate(animals):
    print('#%d: %s'%(idx+1,animal))

# en este caso hemos usado un idx que va a ir aumentando en cada iteracion y vamos a ir enumerando en cada iteracion el animal que toca

# ----------------DICCIONARIOS----------------

'''
Los diccionarios son contenedores, como listas pero que no van a guardar ningun orden en especifico y almacinan parejas o mejor conocidas
como tuplas en las que son (clave,valor) y cada tupla es una entrada en el diccionario
'''
d={'cat':'cute','dog':'furry'}#abrimos el diccionario con llaves e indicamos la tupla con los dos puntos
print(d['cat'])#al darle la clave del diccionario cat nos va a devolver cute ojo que aqui usamos corchete
print('cat'in d)# de esta manera verificamos que existe la clave en el diccionario devolviendome un true 
d['fish']='wet'# de esta manera estamos añadiendo una nueva entrada en el diccionario
print(d['fish'])
# print (d[ ’ monkey ’]) # KeyError : ’ monkey ’ no es una clave de d

# d es un objeto de tipo diccionario asi que va a tener sus propios metodos 
d.update({'cat':'furry'})#con este metodo añadimos una nueva entrada al diccionario en el cado de no existir la clave o la actuaiza en el caso de existir
print(d.get('monkey','N/A'))#con get obtenemos un elemento con valor por defecto nos muestra N/A
print(d.get('fish','N/A'))
del d['fish']#eliminamos el de clave fish
print(d.get('fish','N/A'))#como ahora ya no es una clave nos va a mostrar N/A que es lo que indicamos que salga por defecto en el caso de que no exista la clave

# ahora vamos a ver los bucles en los diccionarios, que son similares a los bucles en listas

# Opcion 1 - acceso al valor
d = {'person': 2 , 'cat ': 4 , 'spider ': 8}

for animal in d:
    legs=d[animal]
    print('A %s has %d legs' %(animal,legs))

# muestra "A person has 2 legs " , "A cat has 4 legs " , "A spider has 8 legs "

# Opcion 2 - acceso a la clave y valor

for animal, legs in d.items():
    print('A %s has %d legs'%(animal,legs))
    # Prints "A person has 2 legs " , "A cat has 4 legs " , "A spider has 8 legs "

# Opcion 3 - mi forma

for animal in d:
    legs=d[animal]
    print('A '+str(animal)+' has '+str(legs)+' legs')
    # Prints "A person has 2 legs " , "A cat has 4 legs " , "A spider has 8 legs "



# ----------------Conjuntos----------------

'''
Los conjuntos o sets aunque son menos frecuentes en python tambien dispone de conjuntos que definen una coleccion de elementos sin orden 
'''

animals={'cat','dog'}
print('cat'in animals)#verifica si un elemnto esta en el conjunto muestra un true porque esta en animals
print('fish' in animals)#muestra false porque no esta en el conjunto
animals.add('fish')#con el metodo add añadimos un nuevo elemento al conjunto
print ('fish' in animals ) # muestra " True "
print (len( animals )) # Numero de elementos en el conjunto ; muestra "3"
animals . add ('cat') # Anadir un elemento al conjunto que ya existe --> no se hace nada
print (len( animals )) # muestra "3"
animals . remove ('cat') # Eliminar un elemento del conjunto
print (len( animals )) # muestra "2" 

'''
Las operaciones mas habituales entre conjuntos son la unidon la interseccion y la diferencia de conjuntos:
A | B: Union entre el conjunto A y B (suma de elementos).
A & B: Intersecci´on entre el conjunto A y B.
A - B: Diferencia entre el conjunto A y B.

'''

#ahora vamos a ver que pasa con los bucles en conjuntos que como vamos a ver si hacen de manera similar a las listas
#no obstante no se puede hacer ninguna asuncion acerca del orden en el cual se extraen los elementos

animals={'cat','dog','fish'}

for idx, animal in enumerate(animals):
    print('#%d: %s'%(idx+1,animal))
    # muestra "#1: fish " , "#2: dog " , "#3: cat "


#----------------Condicionales----------------

'''
En python se usa el comando if como en el resto de lenguajes que conocemos pero con dos puntos al final, de manera adicional tenemos 
elif y else, elif es como un elseif de c o de java y else es cualquier otro caso sin condicion alguna
'''

nota_alumno=5.5

if(nota_alumno==10.0):
    print("El estudiante ha obtenido matricula de honor")
elif(nota_alumno>=5.0):
    print('El estudiante ha aprobado')#NOTA EN PRINCIPIO DA IGUAL PARA CADENA DE CARACTERES SI ES COMILLAS SIMPLES O DOBLES
else:
    print("El estudiante ha suspendido")

'''
Las condiciones mas frecuenes son:
a==b
a<b
a>b
not(a>b)
a<b and c>b OJO AQUI NO SE PONE && COMO EN C O JAVA SE USA AND O OR
a<b or c>b
'''

#----------------Bucles----------------


#En python los bucles se implementan con los comandos while y for

#While

valor=1
while (valor<5): #SE PUEDE PONER O NO PARENTESIS PERO LOS DOS PUNTOS SIEMPRE, COMO EN MATLAB
    print("Valor "+str(valor))
    valor=valor+1

#For

for valor in range(1,5): # EL FOR VA A CAMBIAR YA QUE AHORA ES NECESARIO EL IN RANGE PARA DEFINIR EL RANGO DE LA VARIABLE
    print("Valor "+str(valor))

'''
El comando for se puede utilizar sobre cualquier elemento iterable como son listas, diccionarios, conjuntos y tuplas
'''
# Ejemplo sobre una lista

coches=('Ferrari','Tesla','BMW','Audi')

for coche in coches:
    print(coche)
# muestra ’ Ferrari ’, ’Tesla ’, ’BMW ’ y ’Audi ’ cada uno en una linea

# Ejemplo de iteracion sobre una lista y asignar un numero de orden

for i, coche in enumerate(coches):
    print(str(i)+" - "+coche)
# muestra ’0 - Ferrari ’, ’1 - Tesla ’, ’2 - BMW ’ y ’3 - Audi ’ cada uno en una linea      

#----------------Funciones----------------

'''
Para crear funciones que no clases en python camos a usar el comando def 
'''

def sign(x):
    if(x>0):
        return 'positive'
    elif(x<0):
        return 'negative'
    else:
        return 'zero'
    
for x in [-1,0,1]:
    print(sign(x))

#NOTA IMPORTANTE LAS FUNCIONES HAY QUE DEFINIRLAS ANTES DEL CODIGO QUE LAS UTILIZA COMO EN C 
#ADICIONALMENTE TAMBIEN SE PUEDEN DEFINIR FUNCIONES CON ARGUMENTOS OPCIONALES

def hello(name, loud=False):
    if loud:
        print('HELLO,'+name+'!')
    else:
        print('Bye,'+name+'!')

hello ('Bob') # muestra " Bye , Bob " porque por defecto hemos definido loud como false
hello ('Fred', loud = True ) # muestra " HELLO , FRED !"
hello ('Fred', True ) # muestra " HELLO , FRED !"


#----------------Clases----------------

'''
Recuerdo que la diferencia entre clase y funcion es la terminologia de la creacion de objetos, en donde una clase tiene sus propios metodos y el constructor
vamos a hacer un ejemplo como en el tutorial de moodle y luego voy a intentar importar una clase desde otro fichero .py
'''
#Ejemplo de moodle

#definicion de la clase
class Greeter(object):
    #constructor
    def __init__(self,name): #EL SELF ES COMO EL THIS DE JAVA
        self.name=name  

    #metodo
    def greet(self,loud=False):
        if loud:
            print('HELLO '+self.name)
        else:
            print('Bye '+self.name)


g=Greeter('Fred')
g.greet()
g.greet(True)

from coche import coche #NOTA AL IMPORTAR NO PONER DESPUES DEL FROM EL .PY DEL ARCHIVO O NO VA 

Ferrari=coche("Ferrari","grande")
Ferrari.dimeMarca()
Ferrari.tipoRueda()



#----------------Numpy----------------

'''
Numpy es la principal biblioteca para el calculo cienifico en python, nos proporciona funcionalidad para procesamiento de matrices multidimensionales.
Existen varias maneras para importar la funcionalidad de numpy:
'''

# #Opcion 1
# import numpy
# numpy.X #con esta linea accedemos a la funcion/objeto X de numpy

# #Opcion 2 ACONSEJADA
# import numpy as np #con esta linea pode mos importar numpy con el nombre corto np para mayor practicidad
# np.X # con esta linea accedemos a la funcion/objeto X de numpy

# # Opcion 3 ( de sa co ns ej ad o )
# from numpy import * # importar todas las funciones / objetos
# X #ya no necesitamos usar numpy .X o np.X para acceder

#Arrays en numpy

'''
Al contrario que en las listas de python un array de numpy es un conjunto de elementos del mismo tipo.
O sea que podemos ver las listas como un Arraylist de Java
'''
import numpy as np

a=np.array([1,2,3])#creamos un array de 3x1
print(type(a))#con este metodo cemos que tipo de dato, a que clase pertenece el objeto a
print(a.shape)#nos muestra 3 que es la dimension, 1 fila(omite) y 3 columnas
print(a[0], a[1], a[2])#nos muestra los elementos actuales del array
a[0]=5 # cambiamos la posicion 0 del array, o sea la primera OJO ESTO NO ES COMO EN MATLAB QUE EMPEZAMOS EN LA POS 1, AQUI DESDE LA 0
print(a)#nos muestra todos los elemntos del array de forma directa

b=np.array([[1,2,3],[4,5,6]])#creamos un array 2x3
print(b.shape)#nos saca la dimension del array
print(b[0,0],b[0,1],b[1,0]) #muestra "1 2 4"

# A continuacion, se muestran varios ejemplos para iniciar matrices:

a=np.zeros((2,2))#crea un array de ceros 2x2
print(a)

b=np.ones((1,2))#crea un array de unos 1x2
print(b)

c=np.full((2,2),7)#crea un array 2x2 de todo 7
print(c)

d=np.eye(2)#crea una matriz identidad 2x2
print(d)

e=np.random.random((2,2))#crea un array con valores aleatorios y como es 2x2 usamos 2 random
print(e)

#Ahora veremos ejemplos de indexacion de matrices con numpy

# crear una matriz con rango 2 y dimensiones 3 ( filas ) x 4 ( columnas )
# [[ 1 2 3 4]
# [ 5 6 7 8]
# [ 9 10 11 12 ]]
a = np.array ([[1 ,2 ,3 ,4], [5 ,6 ,7 ,8], [9 , 10 ,11 , 12]])

# Utilizamos ’ slicing ’ para extraer un subarray consistente en las filas 0, 1 y las columnas 1,2;
# El resultado ’b ’ es una matrix 2x2
# [[2 3]
# [6 7]]

b=a[:2,1:3]#OJO RECORDAMOS QUE EN PYTHON EN LOS CORCHETES NO CUENTA EL ELEMNTO QUE CIERRA EL CORCHETE

#OJOOOO: Esta submatriz ’b ’ ( ’ slice of an array ’) es una vista de los mismos datos ,
# con lo cual una modificacion de ’b’ tambien cambia la matriz original ’a

print (a[0 , 1]) # muestra "2"
b[0 , 0] = 77 # b[0 , 0] apunta al mismo dato que a[0 , 1]
print (a[0 , 1]) # muestra "77 "

# extraccion de filas
row_r1 = a[1 , :] # segunda fila de ’a’ vista como matriz de rango 1 (unidimensional)
row_r2 = a[1:2 , :] # segunda fila de ’a’ vista como matriz de rango 2 (bidimensional)
print ( row_r1 , row_r1.shape ) # muestra "[5 6 7 8] (4 ,)"
print ( row_r2 , row_r2.shape ) # muestra "[[ 5 6 7 8]] (1, 4)"

# extraccion de columnas
col_r1 = a[:, 0] # primera columna de ’a ’ vista como matriz de rango 1 ( u n i d i m e n s i o n a l )
col_r2 = a[:, 0:1] # primera columna de ’a ’ vista como matriz de rango 2 ( bi dim en si on al )
print ( col_r1 , col_r1.shape ) # muestra "[ 1 5 9] (3 ,)"
print ( col_r2 , col_r2.shape ) # muestra "[[ 1]
                                # [ 5]
                                # [9]] (3, 1)"

# Adicionalmente, pueden realizarse operaciones de indexaci´on mediante condicionales booleanas (Verdadero o Falso):

a = np.array ([[1 ,2], [3 , 4], [5 , 6]])

bool_idx=(a>2)#de esta forma de encuentran los elementos que son mayores que 2
              #Decuelce un np array de booleanos con el mismo tamaño (shape)
              #sonde coada elemento de bool idx es un boolean que indica si en el indice de a el elemento el es >2 o no
print(bool_idx)

#ahora usando el arry de booleanos para construir un array de rango 1 con los elemntos que tengan el valor a true n bool_idx
print(a[bool_idx])# muestra "[3 4 5 6 ]"

#ESTO LO PODEMOS REALIZAR DE MANERA MAS COMPACTA SIN TENER QUE SACAR EL ARRAY AUXILIAR CON LOS BOOLEANS
print(a[a>2])# muestra "[3 4 5 6 ]"


#Ahora veremos los tipos de los numpy

'''
En la creacion de una arraym numpy puede determinar de manera automatica el tipo de datos que se contienen en la matriz o se puede indeicar de manera explicita
el tipo de dato que queremos utilizar dentro de la matriz.
A continuacion, se muestran ejemplos para la creacion de arrays con datatypes implicitos y explicitos:
'''

x = np.array ([1 , 2]) # numpy selecciona automaticamente el datatype
print (x.dtype ) # muestra " int64 "
x = np.array ([1.0 , 2.0]) # numpy selecciona automaticamte el datatype
print (x.dtype ) # muestra " float64 "
x = np.array ([1 , 2], dtype =np.int64 ) # forzar un tipo concreto de datatype indicandoselo al metodo arry del objeto np
print (x.dtype ) # muestra " int64 "


#A continuacion vamos a ver las diferentes operaciones

'''
Numpy proporciona metodos matemáticos para operar sobre arrays. se pueden utilizar las funciones np.add np.substract np.multiply np.divide ...
o los operadores habituales + - * /
'''
# crear dos arrays para operaciones de ejemplo
x = np.array ([[1 ,2],[3 , 4]], dtype =np.float64 )#vamos a forzar el datatype que queremos
y = np.array ([[5 ,6],[7 , 8]], dtype =np.float64 )
# Suma elemento a elemento ; ambas producen el mismo resultado
# [[ 6.0 8.0]
# [10.0 12 .0]]
print (x + y)
print ( np.add (x , y) )
# Resta elemento a elemento ; ambas producen el mismo resultado
# [[ -4.0 -4.0]
# [ -4.0 -4.0]]
print (x - y)
print ( np.subtract (x,y))
# Producto elemento a elemento ; ambas producen el mismo resultado
# [[ 5.0 12 .0]
# [21.0 32 .0]]
print (x * y)
print ( np.multiply (x , y ))
# Division elemento a elemento ; ambas producen el mismo resultado
# [[ 0.2 0. 33333333 ]
# [ 0. 42857143 0.5 ]]
print (x / y)
print ( np.divide (x , y))
# Raiz cuadrada elemento a elemento ; produce el resultado este por ejemplo tenemos que hacerlo con metodo de manera obligatoria
# [[ 1. 1. 41421356 ]
# [ 1. 73205081 2. ]]
print ( np.sqrt(x))
# Transpuesta de una matriz
print (x) # muestra "[[ 1 2]
# [3 4 ]]"
print (x.T) # muestra "[[ 1 3]
# [2 4 ]]"
# Observe que no produce ningun resultado
# tomar la transpuesta de una matriz u n i d i m e n s i o n a l ( vector )
v = np.array ([1 ,2 , 3])
print (v) # Prints "[ 1 2 3]"
print (v.T) # Prints "[ 1 2 3]"

'''
NOTA IMPORTANTE
Observe que al contrario que en matlab * en numpy este simbolo es la operacion de multiplicacion elemento a elemento (.* en matlab), 
en numpy para hacer la multiplicacion de matrices usamos el metodo dot
'''

x = np.array ([[1 ,2],[3 , 4]]) # array 1 2x2
y = np.array ([[5 ,6],[7 , 8]]) # array 2 2x2
v = np.array ([9 , 10]) # array 3 1x2
w = np.array ([11 , 12]) # array 4 1x2

# ejemplos de multiplicacion  escalar 2 formas de hacerlo
# matrices unidimensionales ; ambas resultan en el valor 219
print (v.dot(w))
print (np.dot(v , w))
# entre matriz y vector ; ambas resultan un array de rango 1 [29 67]
print (x.dot (v) )
print ( np.dot (x , v) )
# matrices bidimensional ; ambas resultan en un array de rango 2
# [[ 19 22 ]
# [43 50 ]]
print (x.dot (y) )
print ( np.dot (x , y) )

#numpy tambien proporciona varios metodos utiles como el de sumatorio .sum

x = np.array ([[1 ,2],[3 , 4]])
print ( np.sum (x)) # calcula la suma de todos los elementos ; muestra "10"
print ( np.sum (x , axis =0)) # calcula la suma de cada columna ; muestra "[4 6]"
print ( np.sum (x , axis =1)) # calcula la suma de cada fila ; muestra "[ 3 7]"


#----------------Matplotlib----------------

'''
Matplotlib es una libreria para mostrar datos, siendo muy similar a como plotea matlab
Primero vamos a ver las diversas opciones de importacion de la libreria
'''
# #Opcion 1
# import matplotlib.pyplot
# matplotlib.pyplot.X #con esto accedemos a los diferentes metodos de la libreria

# #Opcion 2 (aconsejado)
# import matplotlib.pyplot as plt #asi reducimos la nomenclatura
# plt.X

# #Opcion 3 (desaconsejado)
# import matplotlib.pyplot import *
# X

#Plot
import numpy as np
import matplotlib.pyplot as plt

#calculo de datos 2D la funcion seno
x=np.arange(0, 3*np.pi , 0.1) # estamos definiendo como en matlab los incrementos
y=np.sin(x)#calculo de la funcion sen()

#mostrar puntos usando matplotlib
plt.plot(x,y)#el plot funciona igual que en matlab
plt.show()#debe llamar plt.show para que se puestre en una ventana

#el siguiente ejemplo permite mostrar varios datos simultaneamente con titulo, leyenda
#y etiquetas en los ejes

#COMO PODEMOS VER LOS COMANDOS SON PARECIDOS A MATLAB
# calculo de datos 2D - funcion sen (x) y cos (x)
x = np.arange (0 , 3 * np .pi , 0.1)
y_sin = np.sin (x )
y_cos = np.cos (x )
# mostar datos usando matplotlib
plt.plot (x , y_sin )
plt.plot (x , y_cos )
# incluir etiqueta para ejes X e Y
plt.xlabel ('x axis label')
plt.ylabel ('y axis label')
# incluir titulo de figura
plt.title ('Sine and Cosine')
# incluir etiqueta / leyenda para los datos pintados
plt.legend (['Sine ', 'Cosine '])
# activar ventana
plt.show ()

#Subplot MUY SIMILAR A MATLAB
#Para mostrar carios datos en una misma ventana, utilizamos el comando subplot

# configurar un subplot con 2 filas y 1 columna ,
# y establecer como activo el primer subplot .
plt.subplot (2 , 1 , 1)
# primera subventana
plt.plot (x , y_sin ) # datos
plt.title ('Sine') # titulo
# segunda subventana
plt . subplot (2 , 1 , 2) # activamos la posicion a pintar
plt . plot (x , y_cos ) # datos
plt . title ('Cosine ') # titulo
# mostrar la figura
plt.show ()

#Imshow

from matplotlib . pyplot import imread

# cargar imagen RGB + alpha y mostrar imagen con mapas de colores RGB ( por defecto )
img = imread('Konoha.jpg')
print ( img.dtype , img.shape ) # muestra " float32 (130 , 542 ,4)"
plt.figure (1)#creacion de una figura
imgplot = plt.imshow ( img )
# plt.show ( block = False )
# # cargar imagen y mostrar imagen con mapas de colores en escala de grises
# img = imread('https://matplotlib.org/_static/stinkbug.png')
# print ( img.dtype , img.shape ) # muestra " float32 (375 , 500 )"
# plt . figure (2)
# imgplot = plt.imshow( img , cmap =" gray ")
# plt.show( block = False )
# # block execution so the program does not finish and we can see the images
# input(" Presione cualquier tecla para terminar el ejemplo ... ")

#----------------SciPy----------------

'''
SciPy es una libreria que utiliza Numpy pra proporcionar una colleccion de algoritmos matemáticos y utilidades
que permiten un rapido desarrollo
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd

# matriz / señal / imagen a filtrar

im = np.zeros((128,128))
im[32:-32 , 32:-32] = 1
im[45:-45 , 45:-45] = 2
print (im , im.shape)

# kernel para deteccion de bordes ESTO ES COMO EN TEORIA DE TECVID
k = np.array ([[0 ,-1 ,0],[-1 ,4 ,-1], [0 ,-1 , 0]])
print (k , k.shape )

# aplicamos el kernel con el metodo de convolucion 
res = nd.convolve (im,k,mode ='constant', cval =0.0 )
print ( res , res.shape)

# visualiza resultados graficamente
plt.figure (1)
plt.imshow (im , cmap ='gray')
plt.show ( block = False )
plt.figure (2)
plt.imshow ( res , cmap ='gray')

#Esto es para un pause de matlab         
plt.show ( block = False )
input (" Presione cualquier tecla para terminar el ejemplo ... ")

'''
Adicionalmete con Scipy proporciona opciones para varias opciones para el filtrado 
de imagenes dentro de su modulo spicy.ndimage. en el siguiente ejemplo se exploran 
los filtrados gaussiano y de sobel
'''

import numpy as np
import scipy . ndimage as nd
import matplotlib . pyplot as plt

im = np . zeros (( 256 , 256 ))
im[64:-64 , 64:-64] = 1
im[90:-90 , 90:-90] = 2

# suavizado con un nucleo Gausiano
sigma = 8
img = nd.gaussian_filter (im , sigma = sigma )

# deteccion de bordes con sobel
sx = nd.sobel(im , axis = 0 , mode = 'constant') # bordes horizontal
sy = nd.sobel (im , axis = 1 , mode='constant') # bordes vertical
sob = np.hypot (sx , sy ) # modulo de ambos bordes
plt.subplot (3 ,2 ,1)
plt.imshow(im , cmap ='gray') # mostar imagen original
plt.title('Imagen Original')
plt.subplot (3 ,2 ,2)
plt.imshow( img , cmap ='gray') # mostar imagen suavizada
plt.title('Suavizado Gaussiano')
plt.subplot (3 ,2 ,3)
plt.imshow(sx , cmap ='gray') # mostar bordes horizontal
plt.title('SobelX - Bordes horizontal')
plt.subplot(3 ,2 ,4)
plt.imshow(sy , cmap ='gray') # mostar bordes vertical
plt.title('SobelY - Bordes vertical')
plt.subplot(3 ,2 ,5)
plt.imshow(sob , cmap ='gray') # mostar bordes horizontal y vertical
plt.title('Bordes horizontal y vertical')
plt.show( block = False )
input (" Presione cualquier tecla para terminar el ejemplo ... ")

# Calculo de distincias entre puntos

#SciPy contiene multiples funciones para calcular distancias entre puntos en el modulo scipy.spatial.distance 

'''
A continuacion, se muestran un ejemplo para calcular distancias entre puntos previamente 
definidos mediante el metodo pdist :
'''
# Ejemplo 1
# Calculo de distancias entre todos los puntos con pdist
import numpy as np
from scipy.spatial.distance import pdist , squareform
# crea un array donde cada fila son las coordenadas de un punto en un espacio b id im en si on al 2D
# [[0 1]
# [1 0]
# [2 0]]
x = np.array ([[0 , 1], [1 , 0], [2 , 0]])
print (x)
# calculo de la distancia Euclidea entre todas las filas de ’x ’
# d[i , j] es la distancia euclidea entre el punto i x[i, :] y el punto j x[j, :] ,
# y ’d’ es el siguiente array :
# [[ 0. 1. 41421356 2. 23606798 ]
# [ 1. 41421356 0. 1. ]
# [ 2. 23606798 1. 0. ]]
d = squareform( pdist (x , 'euclidean') )
print (d)

'''
A continuacion, se muestran un ejemplo para calcular distancias entre conjuntos de puntos previamente definidos
mediante el metodo cdist
'''
# Ejemplo 2
# Calculo de distancias entre todos los pares de puntos de dos conjuntos con cdist
import numpy as np
from scipy.spatial.distance import cdist , squareform
# crea un array donde cada fila son las coordenadas de un punto en un espacio b id im en si on al 2D
# [[0 1]
# [1 0]
# [2 0]]
x = np.array ([[0 , 1], [1 , 0], [2 , 0]])
print (x)
# crea un array donde cada fila son las coordenadas de un punto en un espacio b id im en si on al 2D
# [[0 1]
# [1 1]
# [2 3]]
y = np.array ([[0 , 1], [1 , 1], [2 , 3]])
print (x)
# calculo de la distancia Coseno entre todas las filas de ’x ’
# d[i , j] es la distancia Coseno entre el punto i x[i, :] y el punto j y[j, :] ,
# y ’d’ es el siguiente array :
# [[ 0. 0. 29289322 0. 16794971 ]
# [1. 0. 29289322 0. 4452998 ]
# [1. 0. 29289322 0. 4452998 ]]
d = cdist(x , y , 'cosine')
print (d)

#Los metodos pdist y cdist soportan varios tipos distintos de distancias ademas de ’euclidean’ y ’cosine’

#----------------Scikit-image----------------

'''
Scitkit-image es una libreria especificamente diseñada para el manejo y tratamiento de imagenes en Python
Notese que la livreria Scipy tiene un caracter mas amplio, en otras palabras, esta mas orientada al campo 
de las matematicas ciencia e ingenieria y por ello  la scitkit tiene una menor funcionalidad respecto al
tratamiento de imagenes 
'''

#Lectura de iamgenes
#Para la lectura se usa la combianacion de los modulos skimage.io y matplotlib.pyplot 

import matplotlib.pyplot as plt
import numpy as np
from skimage import io

#lectura de imagen desde URL

img= io.imread('https://matplotlib.org/_static/stinkbug.png')
print(img.dtype, img.shape)

#mostrar imagen
plt.imshow(img, cmap='gray')
plt.show()

'''
Si se depuea este codigo se puede observar que la imagen tiene tipo uint8 cuyos valores van del rango de 
0 a 255 si por el contrario se quiere operar en el rango de 0 a 1 debe convertir la imagen leida con 
img_as_float32 como vemos en el siguiente codigo
'''

import matplotlib.pyplot as plt
import numpy as np
from skimage import io, img_as_float32

#lectura de imagen desde utl
img= io.imread('https://matplotlib.org/_static/stinkbug.png')
print(img.dtype, img.shape)

floatImage=img_as_float32(img)
print(floatImage.dtype, floatImage.shape)#muestra float32 (375,500)

#mostrar imagen
plt.imshow(floatImage,cmap='gray')#el cmap es como la tabla indexada
plt.show()

'''
Escala de grisess VS Color

las imagenes en color se definen principalmente como un conjunto de matrices bidimendionales
cada matriz con calores representativos de la intensidad de la imagen. Por ejemplo, las imagenes a color
RGB estan compuestas de tres matrices independientes tambien llamadas canales para representar los colores
rojo verde y azul. Por otro lado las imagenes en escala de grisas estan formadas por una sola matriz que 
representa el nivel de gris o intensidad gray

En python podemos convertir las imagenes de color a escala de grises con el metodo rgb2gray. Tambien podemos
utilizar la indexacion. Para mostrar imagenes seguieremos usando Matplotlib y su funcion matplotlib.pyplot.imshow
el siguiente codigo muestra un ejemplo de toda la funcionalidad descrita:
'''

# import numpy as np
# from skimage import io , color
# import matplotlib . pyplot as plt
# # lectura de imagen RGB desde URL
# rgbImage = io.imread('http://www.jeffreysward.com/image/tp02aw600.gif')
# print(rgbImage.dtype , rgbImage.shape )
# # conversion a escala de grises
# grayImage = color.rgb2gray ( rgbImage )
# print ( grayImage.dtype , grayImage.shape )
# # mostrar imagen original y convertida
# plt.figure(1)
# plt.imshow( rgbImage )
# plt.figure(2)
# plt.imshow( grayImage , cmap ='gray')
# plt.show( block = False )
# # extraer canales de color
# redChannel = rgbImage [:,:,0] # canal rojo
# greenChannel = rgbImage [:,:,1] # canal verde
# blueChannel = rgbImage [:,:,2] # canal azul
# # mostrar los canales de color
# plt.figure(3)
# plt.imshow( redChannel , cmap ='gray'); plt.title ('Rojo')
# plt.figure(4)
# plt.imshow( greenChannel , cmap ='gray'); plt.title ('Verde')
# plt.figure(5)
# plt.imshow( blueChannel , cmap ='gray'); plt.title ('Azul')
# plt.show()

'''
En el siguiente ejemplo vamos a mostrar como se puede generar una imagen RGB
a partir de tres matrices la funcion np.stack de la libreria numpy
'''

# import numpy as np
# from skimage import io , color
# import matplotlib.pyplot as plt
# # lectura de imagen RGB desde URL
# rgbImage = io.imread ('http://www.jeffreysward.com/image/tp02aw600.gif')
# print ( rgbImage.dtype , rgbImage.shape )
# (m,n,o) = rgbImage.shape
# # extraer canales de color
# redChannel = rgbImage [:,:,0] # canal rojo
# greenChannel = rgbImage [:,:,1] # canal verde
# blueChannel = rgbImage [:,:,2] # canal azul
# # crear una imagen vacia (de niveles de gris )
# allBlack = np.zeros ((m , n) , dtype =np.uint8 )
# # crear version de color para cada canal extraido
# justRed = np.stack (( redChannel , allBlack , allBlack ) , axis =2)
# justGreen = np.stack (( allBlack , greenChannel , allBlack ) , axis =2)
# justBlue = np.stack (( allBlack , allBlack , blueChannel ) , axis =2 )
# # Recombinar los canales extraidos para recrear la imagen original RGB
# recombinedRGBImage = np.stack (( redChannel , greenChannel , blueChannel ) , axis =2)
# plt.imshow ( recombinedRGBImage )
# plt.show ()

#Convolucion y filtrado

'''
Para calcular la convolucion y filtrado si el kernel es isotropico ytilizaremos la misma
funcionalidad de Scipy. El siguiente ejemplo muestra como aplicar un filtro de media a
una imagen
'''
import numpy as np
import matplotlib.pyplot as plt
from skimage import color , data
from scipy.signal import convolve2d as conv2
from scipy.ndimage import convolve
# lectura de imagen desde el modulo ’data ’
astro = color.rgb2gray ( data.astronaut () )
# kernel 5x5 para el filtro de media
k = np.ones ((5 , 5 )) / 25
# aplicamos el kernel ( ambas opciones son equivalentes )
astro_ = conv2 ( astro , k , 'same') # opcion 1
astro_ = convolve ( astro , k , mode ='constant') # opcion 2
fig , ax = plt.subplots ( nrows =1 , ncols =2 , figsize =(8 , 5) ,
sharex =True , sharey = True )
plt.gray ()
ax[0].imshow( astro , cmap ='gray')
ax[0].axis('off')
ax[0].set_title('Imagen Astronaut del modulo skimage.Data')
ax[1].imshow( astro_ )
ax[1].axis('off')
ax[1].set_title('Suavizado con un filtro de media 5x5')
fig.tight_layout ()
plt.show ()