# *args= significa argumetno . Gracias al * podemos definir funciones donde el numero de argumentos sea variado. Es decir podemos definir funciones genericas que no acepten un numero determinado de argumetno , sino adaptarse s a la cantidad que se pase

# el nombre puede cambiar , siempre y cuando comience con un *(asterisco), pro por buenas practicas se deja :*args

def suma (*args):
    total = 0
    for arg in args:
        total += arg
    return total


def sumaRapida (*args):
    return sum(args)



# ? **KWARGS : ARGUMENTOS INDEFINIDOS y trabajan con diccionarios.

def sumaKwargs (**kwargs):
    total = 0
    
    for clave,valor in kwargs.items():
        print(f'clave: {clave} y su valor es : {valor}')
        total += valor

    return f'El total es : {total}'

# print(sumaKwargs(a=5,b=6,c=7)) 

def pruba(n1,n2,*args,**kwargs):
    
    print(f'El valor de N1 es : {n1}')
    print(f'El valor de N2 es : {n2}')
    
    for args in args:
        print(f'El valor de *args es : {args}')
    
    for clave,valor in kwargs.items():
        print(f'clave de kwargs es : {clave} y su valor es : {valor}')


# print(pruba(20,50,100,200,300,a=5,b=6,c=7)) 
# forma mas limpia de los valores:
args = [100,200,300]
kwargs= {'a':'5','b':'6','c':'7'}
pruba(20,50,*args,**kwargs)