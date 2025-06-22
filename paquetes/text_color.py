# pypi: repositorio de paquetes de python de codigo abierto
# pip install name_paquete: Descargar e instalar paquetes del repositorio pypi

from colored import fg, bg, attr
from openpyxl import * #para manipular con archivos excel

print(fg('red') + "hello world" + attr("reset"))