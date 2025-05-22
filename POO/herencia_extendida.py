class Animal:
    
    def __init__(self,edad,color):
        self.edad = edad
        self.color = color
        
    def hablar(self):
        print('este animal emite un sonido')
        
class Pajaro(Animal):
    
    def __init__(self,edad,color,altura_vuelo):
        # super(): para heredar atributos de instancia de la clase padre (Animal)
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo
        
    # modifico el metodo de la clase padre Animal
    def hablar(self):
        print('pio')
    def volar(self,metros):
        print(f'El pajaro vuela {metros} metros y es de color {self.color}')

pajaro = Pajaro(2,'verde',60)
print(pajaro.altura_vuelo)
pajaro.volar(100)



# ***********************************************************************************************
# ***************************************HERENCIA MULTIPLE********************************************************

class Padre:
    def hablar(self):
        print('hola')
        
class Madre:
    def reir(self):
        print('ja ja ja')
    def hablar(self):
        print('ey que tal')
class Hijo(Padre,Madre):
    pass
class Nieto(Hijo):
    pass

# nieto hereda todos los atributos y metodos de Padre y Madre
mi_nieto= Nieto()
mi_nieto.hablar() #ejecuta este metodo de Padre porque primero se llama la clase Padre y luego Madre si fuera al contrario ahi si hereda el metodo hablar() de la clase madre
mi_nieto.reir()