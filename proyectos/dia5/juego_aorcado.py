from random import * 

def game_aorcado():
    
    palabras = ['oso','jardin','lobo','cuartilla']
    intentos= 1
    vida= 6

    palabra_secreta= choice(palabras)
    cantidad_letras = len(palabra_secreta)
    guiones = ['_'] * cantidad_letras

    print(f'*********COMPLETE LA PALBRA: {guiones}\n')

    while intentos <= 6:
        print(F'TIENES DE VIDA ❤️  {vida} \n')
        
        letra_usuario = input('Ingresar una letra: ')
        if (intentos == 6):
            print(f'VAYA! YA NO TIENES VIDA 💔 {vida} \n')
            break
    
        # validar string --- .
        # isalpha(): devuelve true si todos los caracteres son letras (a-z, A-Z) y no hay números, espacios o símbolos
        if len(letra_usuario) != 1 or not letra_usuario.isalpha():
            print('DEBE INGRESAR UNA SOLA LETRA (a-z)')
            continue
            
        
        if letra_usuario in  guiones:
            print(f"\n--------------------¡Ya ingresaste esta letra: {letra_usuario} anteriormente-----------------".upper())
            
        elif letra_usuario in  palabra_secreta:
            # Buscar todas las posiciones donde aparece la letra
            for l in range(len(palabra_secreta)):
                if palabra_secreta[l] == letra_usuario:
                    guiones[l] = letra_usuario  # Actualizar posición (agregar letra en la posicion que coincide)
            print(f"¡Correcto! La letra '{letra_usuario}' está en la palabra.")           
                
        else:
            intentos += 1
            vida -=1
            print('\n *****************INTENTA CON OTRA LETRA***************************')
        
        print(f'LETRAS AGREGADAS: {guiones}')
        # # Verificar si ya se adivinó toda la palabra
        if "_" not in guiones:
            print("\n¡Felicidades! Adivinaste la palabra:", palabra_secreta)
            return guiones
        
        
print(game_aorcado())