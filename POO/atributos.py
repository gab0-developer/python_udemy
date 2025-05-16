class Pajaro:
    # definir atributos de clase
    especie = 'tucan'
    
    # metodo constructor, se define como "__init__"
        # selft: palabra clave y obligatoria. Representa la instancia del objeto/clase que vaya a ser creado
    def __init__(self,color): # definimos atributo de instancia en este caso "color"
        # definimos un parametro  "micolor" que contiene el atributo de instancia
        self.micolor= color
        
# instancio u objeto de clase
mi_pajaro= Pajaro('azul')

print(mi_pajaro.micolor)
print(mi_pajaro.especie)