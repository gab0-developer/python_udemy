from random import randint

intentos = 1
numero_secreto = randint(1,100)
nombre = input('Cual es su nombre?: ')

while intentos <= 8:
    
    print('******SOLO TIENE 8 INTENTOS PARA ADIVINAR EL NUMERO****** \n')
    numero = int(input('Ingresar un numero del 1 al 100: '))
    
    if (intentos == 8):
        print(f'OH! LASTIMA, YA CULMINARON LOS INTENTOS- EL NUMERO SECRETO ES : {numero_secreto}. VUELVE A EJECUTAR EL PROGRAMA PARA JUGAR')
        break
    
    if numero == numero_secreto:
        print(f'FELICIDADES! {nombre} HA GANADO EN EL INTENTO: {intentos}') 
        break
    elif numero < 1 or numero > 100:
        print(f'ha elegido un número que no está permitido. Intento: {intentos}') 
    elif numero < numero_secreto:
        print(f'ha elegido un número menor al número secreto. Intento: {intentos}') 
    elif numero > numero_secreto:
        print(f'ha elegido un número mayor al número secreto. Intento: {intentos}') 
        
    intentos  += 1
    
# todo - 20/20
