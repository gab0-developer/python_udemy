class Pajaro:

    alas = True

    def __init__(self,color): 
        self.micolor= color
    def piar(self):
        # paso atributo de instancia y obligatoriamente se debe poner sleft para hacer referencias al atributo instancia
        print(f'pio de color {self.micolor}')
    def volar(self,metro):
        print(f'El pajaro vuela {metro} metros')
        
mi_pajaro= Pajaro('azul')
mi_pajaro.piar() #ejecutamos nuestro metodo
mi_pajaro.volar(45) #ejecutamos nuestro metodo

print(mi_pajaro.micolor)
print(mi_pajaro.alas)
