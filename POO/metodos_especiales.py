class CD:
    def __init__(self,autor , titulo,canciones):
        self.autor= autor
        self.titulo= titulo
        self.canciones= canciones
        
    # metodo especial :
    # __str__(): ayuda a definir como quiero que se muestre un string de mi CLASE cada vez que un metodo lo solicite
    def __str__(self):
        return f'album : {self.titulo} de {self.autor} con {self.canciones} canciones'
    # __len__(): obtener longitud de caracateres, listas , etc
    def __len__(self):
        return self.autor
    # __del__(): Eliminar objeto (la clase ya instanciada)
    def __del__(self):
        return 'se ha eliminado la clase CD'
    
# instanciar mi clase
mi_cd = CD('gabriel','triunfador',24)
print(mi_cd) #result: album : triunfador de gabriel con 24 canciones