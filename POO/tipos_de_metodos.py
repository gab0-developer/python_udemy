class Pajaro: 
    alas = 'si vuela'
    @classmethod # Indicamos que los metodos pertenecen a la clase (no a una instancia). Por lo cual no es necesario instanciar la clase para ejeuctar los metodos 
    def color(cls,color):
        print(f' El color del pajaro es {color}')
        cls.alas = 'NO VUELA' #cambio el valor del atributo de clase "alas"
        print(f' El  pajaro es {cls.alas}') #accedemos a atributo de clase (no se accede a atributo ni metodo de instancia[self])
        
    """
        @staticmethod:  en Python define un método estático que:
        1.No recibe self ni cls (no accede a la instancia ni a la clase).
        2.Es como una función normal, pero vive dentro de la clase por organización.
        3.Se usa sin instanciar la clase (ej: Clase.metodo()).
    """
    @staticmethod
    def especie():
        print('EL PAJARO ES UN TUCAN -> ESTE ES UN METODO ESTATICO')
        
        
# ejecutar metodo de clase sin necesidad de intanciar la clase
Pajaro.color('amarillo')
Pajaro.especie()