class Persona:
    
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    
class Cliente(Persona):

    # balance =  #saldo
    def __init__(self,nombre,apellido,numero_cuenta,balance =0):
        
        super().__init__(nombre,apellido) #herar atributos de instancias de la clase padre
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    
    # __str__(): ayuda a definir como quiero que se muestre un string de mi CLASE cada vez que un metodo lo solicit
    print('***********************SUS DATOS ACTUALE***********************')
    def __str__(self):
        return f'\nCLIENTE: {self.nombre.upper()} {self.apellido.upper()}\n BALANCE DE CUENTA: numero de cuenta: {self.numero_cuenta} y su monto actual: {self.balance}'
    
    def depositar(self,monto_deposito):
        self.balance += monto_deposito 
        print(f'monto: {monto_deposito} depositado')
        
    def retirar(self,monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro 
            print(f'monto a retirar: {monto_retiro} retirado')
        else:
            print('Fondos insuficientes. Por favor verifique')
        

def crear_cliente():
    nombre_cliente = input('INGRESAR SU NOMBRE: ')
    apellidoi_cliente = input('INGRESAR SU PELLIDO: ')
    numero_cuenta = input('INGRESAR SU NUMERO DE CUENTA: ')
    
    cliente = Cliente(nombre_cliente,apellidoi_cliente,numero_cuenta)
    return cliente

def inicio():
    cliente =crear_cliente()
    print(cliente)
        
    options = ['REALIZAR DEPOSTIO','REALIZAR RETIRO','SALIR DEL SISTEMA']

    while True:
        print('\n' +'*'* 10 + 'INDICE DE OPCIONES'+ '*'*10 + '\n')
        for option in range(len(options)):
            print(f'{option+1 } : {options[option]}')
            
        opcion = int(input('\n SELECCIONAR UNA DE LAS OPCIONES (1-3): '))
        match opcion:
            case 1:
                print('****************************REALIZAR DEPOSITO****************************')
                deposito = int(input('INGRESAR MONTO A DEPOSITAR: '))
                cliente.depositar(deposito) 
            case 2:
                print('****************************REALIZAR RETIRO****************************')
                retiro = int(input('INGRESAR MONTO A RETIRAR: '))
                cliente.retirar(retiro) 
            case 3:
                print('\n SALIO DEL SISTEMA...\n')
                break
            case _:
                print('LA OPCION NO COINCIDE CON NINGUNO DE LOS DATOS')
        print(cliente)
        
    print('GRACIAS POR REALIZAR SU OPERACION BANCARIA')
    print(cliente)
    

inicio()