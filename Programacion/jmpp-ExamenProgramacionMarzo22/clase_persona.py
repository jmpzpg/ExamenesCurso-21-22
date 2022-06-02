'''
Jose Manuel Peres Puig - Examen de Programación del segundo trimestre
'''


class Persona():
    def __init__(self, nombre, apellido1, dni, apellido2=None) -> None:
        self.__nombre = nombre
        self.__apellido1 = apellido1
        self.__apellido2 = apellido2
        self.__dni = dni
    
    @property
    def nombre(self):
        return self.__nombre
    @property
    def apellido1(self):
        return self.__apellido1
    @property
    def apellido2(self):
        return self.__apellido2
    @property
    def dni(self):
        return self.__dni

    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    @apellido1.setter
    def apellido1(self, new_apellido1):
        self.__apellido1 = new_apellido1
    @apellido2.setter
    def apellido2(self, new_apellido2):
        self.__apellido2 = new_apellido2
    @dni.setter
    def dni(self, new_dni):
        self.__dni = new_dni

    def __str__(self) -> str:
        return f'{self.__nombre} {self.__apellido1} {self.apellido2} con DNI: {self.__dni}'


# ==================================================

p = Persona('Pepe','Alba','12345678V','Segundo')
print(p)