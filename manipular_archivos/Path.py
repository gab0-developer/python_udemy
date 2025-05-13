from pathlib import Path
#? METODOS
# home(): para obtener una ruta absoluta a un directorio de nuestra pc
# with_name(): cambiar nombr de archivo dentro de un directorio ya creado o existente en el objeto Path
# parent(): devuelve el padre mas cercano al archivo
# relative_to(): indicar a partir de que directorio iniciar

base = Path.home()
guia = Path(base,'canada','europa','family.txt') #transformar string a directio de acceso
# cambiar nombre del archivo
guia2= guia.with_name('conocimientos.txt') 
print(f'guia : {guia}')
print(f'guia2 : {guia2}')
print(f'parent {guia.parent.parent}') #devuelve el penultimo padre (se puede poner una sola vez y devuelve el padre mas sercano al archivo)

ruta = Path('pais','estadoUnidos','NewYork','city.txt')
relative= ruta.relative_to(Path('pais')) #devuelve : estadoUnidos\NewYork\city.txt
print(f'relative_to : {relative}')


ruta_ = Path('C:/Users/Usuario/Desktop/Curso Python') / 'Cuestionario Día 6' / 'Pregunta 1'
carpeta_ = ruta_.parents[3]

print(f'ruta_ {ruta_}')
print(f'carpeta_ {carpeta_}')