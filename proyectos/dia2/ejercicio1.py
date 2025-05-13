nombre = input("Ingresar su nombre: ")
ventas_mensuales = input("Ingresar la cantidad de venta mensual: ")
operacion = round(int(ventas_mensuales) * 13 / 100,2)
print(f'"{nombre}" al tener un total de "{ventas_mensuales}" ventas mensuales tu comisión en este mes es: {operacion}$')



# 20/20 