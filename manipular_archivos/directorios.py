# os: Sistema Operativos
import os
# todo -----  metodos de OS--------
# *getcwd():obtener el directorio de trabajo actual
getcwd= os.getcwd()
# *chdir: change directory -> cambiar de directorio
chdir= os.chdir('C:\\Users\\Gabriel\\OneDrive\\Desktop\\UNEXCA')
# *ABRIR ARCHIVO DE OTRO DIRECTORIO
# with open('prueba_directory.txt','r') as archivo:
#     print(archivo.read())
# *makedirs: acceder a directorio y crear una carpeta nueva
# makedirs= os.makedirs('C:\\Users\\Gabriel\\OneDrive\\Desktop\\UNEXCA\\_python_makedirs') #ejecutar en python 

# *******************************************************************************************
# *******************************************************************************************

ruta = 'C:\\Users\\Gabriel\\OneDrive\\Desktop\\python_udemy\\manipular_archivos\\prueba.txt'
# basename: nombre base desde nuestra ruta (directorio)
# dirname: nombre de todo el directorio
# split: Nos trae una tupla con el directorio completo y nomobre base 
# elemento = os.path.split(ruta)

# * ELMINAR CARPETA
# *rmdir: remover o eliminar directorio
# rmdir= os.rmdir('C:\\Users\\Gabriel\\OneDrive\\Desktop\\UNEXCA\\_python_makedirs') #ejecutar en python 
# print(elemento)

# * ***************** CREAR RUTAS PARA QUE SE INTERPRETEN EN CUALQUIER SISTEMA OPERATIVO ****************
# se coloco Path con la inicial mayuscula debido a que es un objeto no es modulo ni metodo
from pathlib import Path #indica que se puede leer los arhivos en cualquier sistema operativo

carpeta = Path('C:/Users/Gabriel/OneDrive/Desktop/UNEXCA') #El archivo se puede abrir con cualquier sistema operativo gracias a Path
# importar archivo concatenando la carpeta y nombre del archivo existente
archivo = carpeta / 'prueba_directory.txt'  
# ABRIR ARCHIVO
with open(archivo) as archive:
    print(archive.read())