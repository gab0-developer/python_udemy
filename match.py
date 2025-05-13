# coincidencias de patrones estructurales 
# funciona como if o switch case

serie = 'N3'
match serie:
    case 'N1':
        print('LA SAYONA')
    case 'N2':
        print('LA MOMIA')
    case 'N3':
        print('LA PATRONA')
    case _:
        print('NO EXISTE')
        
# ***********************************************************************
# **************************CODIGO MAS AVANZADO*********************************************
# ***********************************************************************
        
cliente ={
    'nombre': 'luis',
    'edad': 24,
    'ocupacion': 'ingeniero',
}
pelicula ={
    'titulo': 'matrix',
    'ficha_tecnica': {
        'protagonista':'juanito alimana',    
        'director':'richar fonica',       
    },
}

elementos = [cliente,pelicula,'libro']

for elemento in elementos :
    match elemento:
        # en caso de que la estructura esta compusta por :
        case {
            'nombre': nombre,
            'edad': edad,
            'ocupacion': ocupacion,
        }: print(f'es un cliente: {nombre} {edad} {ocupacion}')
        # +o en caso que la estructura esta compuesta por:
        case {
            'titulo': titulo,
            'ficha_tecnica': {'protagonista': protagonista,'director':director },
        }: print(f'es una pelicula: {titulo} {protagonista} {director}')
        case _:
            print('NO COINCIDE CON NINGUNO DE LOS DATOS')
        
        