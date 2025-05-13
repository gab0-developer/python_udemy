text = input('Por favor ingrese un texto: ').lower()
letras = input('Por favor ingrese un texto: ').lower()
array_letras = list(letras)

print('\n')
# ? ¿cuántas veces aparece cada una de las letras que eligió? 
resultado = {}
for letra in array_letras:
    print(f'La letra: {letra} aparece {text.count(letra)} veces')
    
print('\n')

#?  cuántas palabras hay a lo largo de todo el texto. 
palabras=text.split()
cantidad_palabras = len(palabras)
print(f'cantidad de palabras: {cantidad_palabras}')
print('\n')

#? primera letra y ultima letra del texto
first_letra = text[0]
last_letra = text[-1]
print(f'La primera letra del texto es: {first_letra}')
print(f'La ultima letra del texto es: {last_letra}')
print('\n')

#? invertir texto 
palabras_text = text.split()
palabras_invertidas=palabras_text[::-1]
texto_invertido = ' '.join(palabras_invertidas)  # Une las palabras con espacios
print(f'El texto invertido es : {texto_invertido}')
print('\n')
    
#? devolver boleano si existe la palabra "python"
boleano = 'python' in text
if boleano == True:
    print('La palabra PYTHON existe en su texto')
else:
    print('La palabra PYTHON no existe en su texto')
print('\n')
    