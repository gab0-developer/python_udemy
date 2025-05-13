# EVITAR NOMBRAR EL NOMBRE DEL ARCHIVO IGUAL (EN ESTE CASO PUSE LA INICIAL EN MAYUSCULA)

from random import * ## "*": indica que importaremos todas las librerias de random
# from random import randint ## especificamos la libreria a importar

randint = randint(1,50) #se coloca un rango de numero y trae nro aleatorios
uniform = round(uniform(1,50),2) #se coloca un rango de numero y trae nro aleatorios con decimales
random = random() #trae numero aleatorio unicamente entre el 0 y 1

array = ['azul','narajanda',21]
# array_nro =list(range(1,10,2))
choice = choice(array) #Seleccion aleatoria dentro de los elementos de una lista
shuffle(array) #mezclarar o variar el contenido de un array y NO SE ALMACENA EN UNA VARIABLE SINO QUE SE LLAMA DESPUES LA VARIABLE DE LA LISTA
print(array)
 