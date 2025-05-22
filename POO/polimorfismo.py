"""
# polimorfismo:
    # poli: muchos
    # morfismo: formas

En la programacion hace referencia que los objetos pueden tomar diferentes formas, Es decir que se se puede compartir el mismo nombre de metodos y luego llamar esos metodos con el mismo nombre desde el mismo lugar pero aplicados a diferentes objetos.
"""

# ? EJEMPLO DE POLIMORFISMO

class Vaca:
    def __init__(self,nombre):
        self.nombre = nombre
        
    def hablar(self):
        print(f'{self.nombre} dice muuu')

class Oveja:
    def __init__(self,nombre):
        self.nombre = nombre
        
    def hablar(self):
        print(f'{self.nombre} dice bee')
        
vaca1 = Vaca('rosa')
oveja1 = Oveja('nubesita')
# Ejeutar objetos de nombre distinto pueden ejecutar metodos con el mismo nombre 
# vaca1.hablar()
# oveja1.hablar()


# Este caso el polimorfismo nos permite hacer una iteracion de los distitnos objetos y ejecutar su metodos d mismo nombre pero con distita funcion de codigo.

animales = [vaca1,oveja1]
for animal in animales:
    animal.hablar()

# Con una funcion el llamado de distintos objeto
def animal_habla(animal) :
    animal.hablar()
    
animal_habla(vaca1)

