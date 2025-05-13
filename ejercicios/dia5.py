
#! EJERCICIO 1✅

def devolver_distintos(*args):
    if len(args) != 3:
        return 'DEBEN SER MINIMO 3 NUMEROS'
    # Verificar que todos los argumentos sean enteros
    for num in args:
        if not isinstance(num, int):
            return "Todos los argumentos deben ser números enteros."
    
    suma = sum(args)
    if suma > 15:
        return f'EL NUMERO MAYOR ES {max(args)}'
    elif suma < 10:
        return f'EL NUMERO MENOR ES {min(args)}'
    elif 10 <= suma <= 15:
        # ordenar numero y devolver intermedio
        numero_intermedio= sorted(args)
        return f'EL NUMERO INTERMEDIO ES : {numero_intermedio[1]}'
# print(devolver_distintos(6,5,9))


# ! EJERCICIO 2✅

def palabra(palabra):
    return sorted(set(palabra))
# print(palabra('ositos'))

# ! EJERCICIO 3✅

def hallar_ceros(*args):
    if args.count(0) > 2 :
        return True
    else:
        return False
# print(hallar_ceros(1,2,0,0))

# ! EJERCICIO 4 ---- APOYADO DEL CURSO 

def contar_primos(numero):
    if numero < 2:
        return 0
    
    primos = [2] # Inicializamos la lista de primos con el primer número primo (2)
     # Iteramos a través de todos los números impares desde 3 hasta el número dado
    for iteracion in range(3, numero + 1, 2):
        es_primo = True # Asumimos inicialmente que el número es primo
        for n in primos:        # Verificamos si el candidato es divisible por algún primo ya encontrado
            # Optimización: si el primo al cuadrado es mayor que el candidato,
            # no necesitamos seguir verificando
            if n * n > iteracion:
                break
             # Si encontramos un divisor, marcamos como no primo y salimos del bucle
            if iteracion % n == 0:
                es_primo = False
                break
        # Si después de todas las verificaciones sigue siendo primo, lo agregamos a la lista
        if es_primo:
            primos.append(iteracion)
    
    print(primos)
    return len(primos)

print(contar_primos(20))