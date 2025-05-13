# w: indicamos que se va a sobreescribir en el archivo
archivo = open('manipular_archivos\\prueba.txt','w')  #sino existe el archivo lo crea 
# print(archivo.write('ESTE TEXTO ES DEL METODO -> WRITE y elimino el texto existente'))
print(archivo.writelines(['hola','mundo','que tal ?'])) #Solo escribir linea y se utiliza con array de string


archivo_a = open('manipular_archivos\\prueba.txt','a')#con metodo a: indicamos que podemos escrbir en el archivo debajo del contenido ya existente sin necesidad de eliminarlo
# print(archivo.write('ESTE TEXTO ES DEL METODO -> WRITE y elimino el texto existente'))
print(archivo_a.write('HELLO CULASO')) #Solo escribir linea y se utiliza con array de string

archivo.close()



