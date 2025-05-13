import os
from pathlib import Path
from shutil import rmtree #rmtree: orrar una carpeta que contiene archivos u otros directorios dentro de ella

# ruta = Path('C:/Users/Gabriel/OneDrive/Desktop/python_udemy/proyectos/dia6/Recetas')
ruta = Path(__file__).parent / 'Recetas'
print(ruta)

getcwd= os.getcwd() #obtener la ruta actual de las recetas
# *chdir: change directory -> cambiar de directorio
chdir= os.chdir('C:\\Users\\Gabriel\\OneDrive\\Desktop\\UNEXCA')

bienvenda = 'HOLA! BIENVENID@ A NUESTRO RECETARIO' 
recetas= os.listdir(ruta)
cantidad_recetas = len(recetas)

opciones = ['VER RECETAS','CREAR NUEVA RECETA','CREAR NUEVA CATEGORIA','ELIMINAR RECETA','ELIMINAR CATEGORIA', 'SALIR DEL SISTEMA']
cantidad_opciones = len(opciones)
print(recetas)

menu = 0
print('\n')
print(f'*******************{bienvenda}************************')
print(f'*******************CANTIDAD DE RECETAS DISPOBIBLES: {cantidad_recetas}  ************************ \n')

print(f'*******************SELECCIONAR UNA OPCION: ************************ \n')

# def lista_opciones():
#     for opcion in range(cantidad_opciones):
#         print(f'{opcion + 1} : {opciones[opcion]}')
#     opcion_menu = int(input('----SELECCIONAR UNA DE LAS OPCIONES SEGUN SU NUMERO: '))
#     return opcion_menu
# menu = lista_opciones()
    
def categorias():
    print('*******************SELECCIONAR CATEGORIA DE RECETAS************************')
    lista_categorias = []
    for i in range(cantidad_recetas):
        categorias = f'{i} : {recetas[i]}'
        lista_categorias.append(categorias)
        print(categorias)
    # return lista_categorias
# categorias()

def SeleccionarCategoria(numero_categoria):
    for i in range(cantidad_recetas):
        categoria_seleccionada = f'{recetas[numero_categoria]}'
    return categoria_seleccionada
# print(SeleccionarCategoria(numero_categoria))

def LeerArchvo(url):
    # 'C:/Users/Gabriel/OneDrive/Desktop/python_udemy/proyectos/dia6/Recetas/Carnes/Matambre a la Pizza.txt'
    with open(Path(url),'r') as archivo:
                contenido = archivo.read()
                return f'\n CONTENIDO DE LA RECETA: \n ----------------\n  {contenido} \n ----------------\n'

def CrearArchivo(url,nombre,contenido):
    # 'C:/Users/Gabriel/OneDrive/Desktop/python_udemy/proyectos/dia6/Recetas/Carnes/Matambre a la Pizza.txt'
    with open(Path(url),'w', encoding='utf-8') as archivo:
        contenido = archivo.write(contenido)
        return f'\n NUEVA RECETA: ----------------{nombre}----------------\n'
    
def EliminarArchivo (url,name_archive):
    os.remove(url)
    return f'\n SE ELIMINO EL ARCHIVO: {name_archive.upper()}\n'

def CrearCategoria(url,name_category):
    os.mkdir(url)
    return f'\n SE CREO LA CATEGORIA: {name_category.upper()}\n'

def EliminarCategoria (url,name_category):
    rmtree(url)
    return f'\n SE ELIMINO LA CATEGORIA: {name_category.upper()}\n'

while True :
    
    for opcion in range(cantidad_opciones):
        print(f'{opcion + 1} : {opciones[opcion]}')

    opcion = int(input('\n SELECCIONAR UNA DE LAS OPCIONES (1-6): '))
    match opcion:
        case 1:
            categorias()
            numero_categoria= int(input('SELECCIONAR UNA CATEGORIA DE RECETA POR SU NUMERO: '))
            categoria_seleccionada = SeleccionarCategoria(numero_categoria)
            print(f'SELECCIONASTE: {categoria_seleccionada.upper()} Y SUS RECETAS SON: ')
            ruta_categoria = ruta / categoria_seleccionada
            lista_archivos= os.listdir(ruta_categoria) 
            cantidad_lista_archivos = lista_archivos
            #reccorrer con lista_archivos
            for i in range(len(lista_archivos)):
                print(f'{i}: {lista_archivos[i]}')
            archivo_receta= int(input('SELECCIONA EL NUMERO DE UNA RECETA QUE DESEAS LEER: '))
            ruta__archivo_receta= ruta_categoria / cantidad_lista_archivos[archivo_receta]
            # funcion Leer_receta del archivo
            print(f'{LeerArchvo(ruta__archivo_receta)}')
        case 2:
            print('**********************CREAR NUEVA RECETA**********************')
            categorias()
            numero_categoria= int(input('SELECCIONAR UNA CATEGORIA DE RECETA POR SU NUMERO: '))
            categoria_seleccionada = SeleccionarCategoria(numero_categoria)
            ruta_categoria = ruta / categoria_seleccionada
            print(f'SELECCIONASTE: ***{categoria_seleccionada.upper()}***')
            nombre_nueva_receta= str(input('INGRESA NOMBRE DE LA RECETA: '))
            contenido_nueva_receta= str(input('INGRESA CONTENIDO DE LA RECETA: '))
            nueva_receta = f'{ruta_categoria / nombre_nueva_receta.lower()}.txt'
            print(f'{CrearArchivo(nueva_receta,nombre_nueva_receta,contenido_nueva_receta)}')
            
        case 3:
            print('**********************CREAR CARPETA DE CATEGORIAS**********************')
            # .strip(): Elimina espacios en blanco al inicio/final (evita carpetas con nombres como " carnes ").
            nombre_carpeta = input('INGRESAR NOMBRE DE SU NUEVA CATEGORIA DE RECETAS: ').strip().lower()
            print(f'nombre_carpeta : {nombre_carpeta}')
            create_carpeta = f'{ruta/nombre_carpeta}'
            print(CrearCategoria(create_carpeta,nombre_carpeta))
        case 4:
            print('**********************ELIMINAR RECETA**********************')
            categorias()
            numero_categoria= int(input('SELECCIONAR UNA CATEGORIA DE RECETA POR SU NUMERO: '))
            categoria_seleccionada = SeleccionarCategoria(numero_categoria)
            print(f'SELECCIONASTE: {categoria_seleccionada.upper()} Y SUS RECETAS SON: ')
            ruta_categoria = ruta / categoria_seleccionada
            lista_archivos= os.listdir(ruta_categoria) 
            cantidad_lista_archivos = lista_archivos
            #reccorrer con lista_archivos
            for i in range(len(lista_archivos)):
                print(f'{i}: {lista_archivos[i]}')
            archivo_receta= int(input('SELECCIONA EL NUMERO DE UNA RECETA QUE DESEAS ELIMINAR: '))
            ruta__archivo_receta= ruta_categoria / cantidad_lista_archivos[archivo_receta]
            archivo_eliminar = cantidad_lista_archivos[archivo_receta]
            print(ruta__archivo_receta)
            # funcion EliminarReceta del archivo
            print(f'{EliminarArchivo(ruta__archivo_receta,archivo_eliminar)}')
        case 5:
            print('**********************ELIMINAR CATEGORIA**********************')
            categorias()
            numero_categoria= int(input('SELECCIONAR QUE CATEGORIA DESEA ELIMINAR: '))
            categoria_seleccionada = SeleccionarCategoria(numero_categoria)
            ruta_categoria = ruta / categoria_seleccionada
            
            print(f'{EliminarCategoria(ruta_categoria,categoria_seleccionada)}')
            recetas= os.listdir(ruta)  # Actualizar lista de categorías
            cantidad_recetas = len(recetas) #actualizar la cantidad de categorias
        case 6:
            print('SALIO DEL SISTEMA...')
            break
        case _:
                print('NO COINCIDE CON NINGUNO DE LOS DATOS')
