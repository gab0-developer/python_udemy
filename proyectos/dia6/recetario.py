import os
from pathlib import Path

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

def lista_opciones():
    for opcion in range(cantidad_opciones):
        print(f'{opcion + 1} : {opciones[opcion]}')
    opcion_menu = int(input('----SELECCIONAR UNA DE LAS OPCIONES SEGUN SU NUMERO: '))
    return opcion_menu
menu = lista_opciones()
    
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
def CrearCategoria(url,name_category):
    # 'C:/Users/Gabriel/OneDrive/Desktop/python_udemy/proyectos/dia6/Recetas/Carnes/Matambre a la Pizza.txt'
    with open(Path(url),'w', encoding='utf-8') as archivo:
        contenido = archivo.write(contenido)
        return f'\n NUEVA RECETA: ----------------{nombre}----------------\n'
# while True :

# #* ver recetas 
match menu:
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
        print('CREAR NUEVA RECETA')
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
        nombre_carpeta= str(input('INGRESAR NOMBRE DE SU NUEVA CATEGORIA DE RECETAS: '))
        create_carpeta = os.mkdir(f'{ruta/nombre_carpeta}')
        print(create_carpeta)
    case 4:
        print('**********************CREAR CARPETA DE CATEGORIAS**********************')
        nombre_carpeta= str(input('INGRESAR NOMBRE DE SU NUEVA CATEGORIA DE RECETAS: '))
        create_carpeta = os.mkdir(f'{ruta/nombre_carpeta}')
        print(create_carpeta)
    case 6:
        print('SALIO DEL SISTEMA')
    case _:
            print('NO COINCIDE CON NINGUNO DE LOS DATOS')


#         print('SELECCIONE UNA CATEGORIA POR EL NUMERO')
    #     #1 funcion mostrar y seleccionar categoria  
    #     #2 mostrar y seleccionar receta a leer y mostrar su contenido
    #     # 3. funcion volver al inicio
    # elif menus == 2 : #crear receta segun la categoria e incluir en la ruta correcta
    #     #1 funcion categoría de seleccion categoria  
    #     # 2. Crear receta segun la categoria seleccionada
    #         #nombre y contenido
    #     # 3. funcion volver al inicio
    #     print('CREAR NUEVA RECETA SEGUN SU CATEGORIA')
    # elif menus == 3: #CREAR CATEGORIA
    #     print('CREAR NUEVA CATEGORIA ')
    #     # funcion crear categoria (CREAR CARPETA)
    #     # 3. funcion volver al inicio
    # elif menus == 4: #ELIMINAR RECETAS SELECCIONADAS
    #     #1 funcion mostrar y seleccionar categoria  
    #     #2 funcion mostrar y seleccionar receta  
    #     #3 funcion eliminar receta seleccionada  
    #     # 4. funcion volver al inicio
    # elif menus == 5: #ELIMINAR CATEGORIA SELECCIONADAS
    #     #1 funcion mostrar y seleccionar categoria  
    #     #2 funcion eliminar categoria seleccionada  
    #     # 3. funcion volver al inicio
    # elif menus == 6: #FINALIZAR SISTEMA DEL BUCLE
    #     #1 funcion finalizar recetario (sistema)
    

    