palabra = 'python'

# indica  mostrar elemento (letra ) por cada elemetno(letra ) que haya en la variable (palabra)
lista = [letra for letra in palabra]

numeros = [n for n in range(1,20) if n*2 > 10]

numeros = [n if n*2 > 10 else 'NO ES MAYOR' for n in range(1,20,2) ]

print(numeros)