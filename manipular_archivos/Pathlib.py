from pathlib import Path,PureWindowsPath
# ? Path: la ruta la transforma a un objeto y tiene sus propios metodos. Ademas de transformar un string en un formato de ruta de acceso
    #? ventajas:
    # ?    crear o mever arhivos
    #  ?   enumerar archivos
    #   ?  crear rutas basadas en string

carpeta = Path('C:/Users/Gabriel/OneDrive/Desktop/python_udemy/manipular_archivos/prueba.txt')
# * ********************* metodos ********************************
# read_text(): leer el archivo
# name: nombre del archivo
# suffix: extension del archivo(si es .txt,.csv,.pdf, etc)
# stem: nombre del archivo sin su extension 
# exists(): validar si el archivo existe 

# VALIDAR SI EL ARCHIVO INDICADO EN RUTA EXISTE
if not carpeta.exists():
    print('EL ARCHIVO NO EXISTE')
else:
    print('SI EXISTE EL ARCHIVO')
print(carpeta.stem)
# * PureWindowsPath: Transformar cualquier ruta en una ruta de windows
ruta_window= PureWindowsPath(carpeta)
print(f'RUTA TRANSFORMADA : {ruta_window}')


# !NOTA : LA VENTAJA DE PATH ES QUE NOS PERMITE LEER LOS ARCHIVOS : 
# SIN IMPORTAR EL SISTEMA OPERATIVO
#     ABRIR Y CERRAR ARCHIVO