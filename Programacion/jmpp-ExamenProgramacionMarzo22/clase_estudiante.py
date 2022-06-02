'''
Jose Manuel Peres Puig - Examen de Programación del segundo trimestre
'''

class Estudiante():
    min_aprobado = 50

    def __init__(self, nombre='', nota=0) -> None:
        self.__nombre = nombre
        self.__nota = nota

    @property
    def nombre(self):
        return self.__nombre
    @property
    def nota(self):
        return self.__nota


    def __str__(self) -> str:
        return f'Alumno: {self.__nombre} --> nota: {self.__nota}'

    def es_aprobado(self):
        if self.__nota >= Estudiante.min_aprobado:
            return 'Aprobado'
        else:
            return 'Suspenso'

    
# ========================================

#e = Estudiante('Antonio', 52)
#print(e.es_aprobado())

#Estudiante.min_aprobado = 60
#print(e.es_aprobado())
