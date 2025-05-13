# shuffle: mezclar los elementos de una lista 
from random import shuffle

# lista
palitos = ['-','--','---','----']
# mexclar palitos
def mezclar (lista):
    shuffle(lista)
    return lista
# peodirle intento
def probar_suerte ():
    intento = ''
    # mientras que intento no se encuentre con la siguiente lsita conformada ....
    while intento not in ['1','2','3','4','5']:
        intento = input('Elige un numero del 1 al 4: ')
    return int(intento)

# comporbar intento
def comprobar_intento(lista,intento):
    # -1: indicamos a nuestra lista que no iniciara el primer elemento con 0 sino con 1
    if lista[intento -1] == '-':
        print('HA DORMIR')
    else:
        print('QUE SUERTE TE SALBASTE')
        
    print(f'TE HA TOCADO {lista[intento -1]} ')
    
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
comprobar_intento(palitos_mezclados,seleccion)
