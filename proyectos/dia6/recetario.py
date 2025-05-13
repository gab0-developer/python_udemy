import os
from pathlib import Path

ruta = Path('C:/Users/Gabriel/OneDrive/Desktop/python_udemy/proyectos/dia6/Recetas')

getcwd= os.getcwd() #obtener la ruta actual de las recetas
# *chdir: change directory -> cambiar de directorio
chdir= os.chdir('C:\\Users\\Gabriel\\OneDrive\\Desktop\\UNEXCA')

bienvenda = 'HOLA! BIENVENID@ A NUESTRO RECETARIO' 
recetas= os.listdir(ruta)
cantidad_recetas = len(recetas)

opciones = ['VER RECETAS','CREAR NUEVA RECETA','CREAR NUEVA CATEGORIA','ELIMINAR RECETA','ELIMINAR CATEGORIA', 'SALIR DEL SISTEMA']
cantidad_opciones = len(opciones)
print(ruta)
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
# while True :

#* ver recetas existentes
if menu == 1: # ver recetas disponibles
    categorias()
    numero_categoria= int(input('SELECCIONAR UNA CATEGORIA DE RECETA POR SU NUMERO: '))
    categoria_seleccionada = SeleccionarCategoria(numero_categoria)
    ruta_categoria = ruta / categoria_seleccionada
    lista_archivos= os.listdir(ruta_categoria) #reccorrer con for
    print(lista_archivos)
    # numero_categoria= int(input('CUAL DE LAS RECETAS QUIERE LEER?  '))
elif menu == 6:
    print('FINALIZO SISTEMA')

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
    

    