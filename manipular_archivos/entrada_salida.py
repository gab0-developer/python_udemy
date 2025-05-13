# ABRIL ARCHIVO.TXT
archivo = open('manipular_archivos\\prueba.txt') 
#?  read(): metodo para leer archivos
# print(archivo.read())# leer archivo
#? readline(): leer una linea del archivo y podemos especificar la cantidad de caracteres a leer . Ejemplo: readline(50)
# print(archivo.readline(4)) 
#? readlines(): Para poder leer linea especifica del archivo y retorna un array con todas las
print(archivo.readlines()) 


# * ITERAR DENTRO DE CADA LINEAS DEL ARCHIVO
for l in archivo:
    print(F'ESTA LINEA DICE : {l}' )



archivo.close()#cerrar archivo para no consumir recursos. 