class Animal:
    
    def __init__(self,edad,color):
        self.edad = edad
        self.color = color
        
    def nacer(slef):
        print('Este animal acaba de nacer')



class Pajaro(Animal):
    pass


# comprobar herencia en la clase Pajaro
print(Pajaro.__base__) #resultado : <class '__main__.Animal'> indica que se hereda la clase Animal
# comprobar si hay sub clases
print(Animal.__subclasses__()) #resultao : [<class '__main__.Pajaro'>] indica que la subclase es Pajaro ya que esta hereda Animal

# instancias objeto(class)
pajaro = Pajaro(2,'verde')
print(pajaro.edad)
print(pajaro.color)
# obtener metodo heredado
pajaro.nacer()