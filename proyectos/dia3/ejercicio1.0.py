text = input('Por favor ingrese un texto: ').lower()
letra1 = input('ingrese una lertra: ').lower()
letra2 = input('ingrese una segunda letra: ').lower()
letra3 = input('ingrese una tercera letra: ').lower()
array_letras = []

array_letras.append(letra1)
array_letras.append(letra2)
array_letras.append(letra3)

# ? ¿cuántas veces aparece cada una de las letras que eligió? 
count_letra1 = text.count(array_letras[0])
count_letra2 = text.count(array_letras[1])
count_letra3 = text.count(array_letras[2])

print(f'en la letra {letra1} aparecen {count_letra1}')
print(f'en la letra {letra2} aparecen {count_letra2}')
print(f'en la letra {letra3} aparecen {count_letra3}')
print('\n')

#?  cuántas palabras hay a lo largo de todo el texto. 
palabras = text.split()
cantidad_palabras = len(palabras)
print(f'En el texto hay {cantidad_palabras} palabras')
print('\n')

#? primera letra y ultima letra del texto
primera_letra = text[0]
ultima_letra = text[-1]
print(f'La primera letra es {primera_letra} y la ultima letra es : {ultima_letra}')
print('\n')

#? invertir texto 
split = text.split()
palabras_invertidas = split[::-1]
text_invertido = ' '.join(palabras_invertidas)
print(f'El texto inveritdo es : {text_invertido}')
print('\n')

#? devolver boleano si existe la palabra "python"
boleano = 'python' in text
if boleano == True:
    print('La palabra PYTHON existe en su texto')
else:
    print('La palabra PYTHON no existe en su texto')