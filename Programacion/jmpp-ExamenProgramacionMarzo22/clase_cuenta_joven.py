'''
Jose Manuel Peres Puig - Examen de Programación del segundo trimestre
'''

from clase_cuenta import Cuenta
from clase_persona import Persona

class PersonaJoven(Persona):
    def __init__(self, nombre, apellido1, dni, edad, apellido2=None) -> None:
        
        if PersonaJoven.valida_edad(edad):
            super().__init__(nombre, apellido1, dni, apellido2)
            self.__edad = edad
            
        else:
            raise Exception('Para ser una persona joven debe tener menos de 18 años')

    @property
    def edad(self):
        return self.__edad

    @staticmethod
    def valida_edad(edad):
        return edad < 18
            

class CuentaJoven(Cuenta):
    def __init__(self, numero='', interes=0, titulares=[Persona('nombre','ape1','dni')], saldo=0) -> None:
        if self.__valida_titulares(titulares):
            super().__init__(numero, interes, titulares, saldo)
    
    def __valida_titulares(self, titulares):
        salida = False
        for persona in titulares:
            if type(persona) is PersonaJoven:
                salida = True
                break
        return salida
    
    def __valida_interes(self):
        if self.__saldo > 5000:
            self.__interes = 0.05
        else:
            self.__interes = 0.01
    
    def ingresar(self, suma):
        if suma > 1000:
            return super().ingresar(suma+10)
        else:
            return super().ingresar(suma)

    def retirar(self, resta):
        if resta <= self.__saldo/2:
            return super().retirar(resta)
        else:
            return super().retirar(self.__saldo/2)
    