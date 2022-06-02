'''
Jose Manuel Peres Puig - Examen de Programación del segundo trimestre
'''
from clase_persona import Persona

class Cuenta():
    def __init__(self, numero='', interes=0, titulares=[Persona('n','a1','d')], saldo=0) -> None:
        if self.__validar_numero(numero):
            self.__numero = numero
        else:
            raise Exception('El numero de cuenta ha de ser de 20 digitos')
        self.__interes = interes
        if len(titulares) < 4:
            self.__titulares = titulares
        if self.__validar_saldo(saldo):
            self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    @property
    def numero(self):
        return self.__numero
    @property
    def interes(self):
        return self.__interes
    @property
    def titulares(self):
        salida = ''
        for p in self.__titulares:
            salida  += p.nombre
        return salida 

    @interes.setter
    def interes(self, new_interes):
        if 0 < new_interes > 1:
            self.__interes = new_interes
        else:
            raise Exception('el interés ha de ser una cantidad entre 0 y 1')
    
    
    def __validar_saldo(self, saldo):
        return saldo >= 0
    def __validar_titulares(self):
        return len(self.__titulares) < 4
    def __validar_numero(self, num):
        return len(num) == 20
    
    def ingresar(self, suma):
        if suma > 0.00 and type(suma) is float:
            self.__saldo += suma
        else:
            raise Exception('El ingreso debe ser una cantidad positiva')
    
    def retirar(self, resta):
        if resta < self.__saldo:
            self.__saldo -= resta
        else:
            raise Exception('La cantidad a retirar debe ser menor que el saldo disponible')

    def add_titular(self, new_titular):
        if self.__validar_titulares:
            self.__titulares.append(new_titular)
        else:
            raise Exception('No se pueden añadir más titulares. Máximo 4')
    
    def __str__(self) -> str:
        return f'número de cuenta: {self.__numero}\n Clientes: {self.titulares}\nSaldo de la cuenta: {self.__saldo}\nInteres de la cuenta: {self.__interes}'

# =======================================

p = Persona('Pepe','Alba','12345678V','Segundo')
c = Cuenta('12345678912345678900', [p])
print(c)
    