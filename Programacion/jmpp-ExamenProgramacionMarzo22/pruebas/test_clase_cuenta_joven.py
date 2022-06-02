'''
Jose Manuel Peres Puig - Examen de Programación del segundo trimestre
'''

import unittest
from clase_cuenta import Cuenta
from clase_cuenta_joven import CuentaJoven, PersonaJoven
from clase_persona import Persona

class TestClaseCuentaJoven(unittest.TestCase):
    def test_existencia(self):
        pj = PersonaJoven('Alberto', 'lucas', '12345678G', 17)
        cj = CuentaJoven('12345678912345678900', [pj])
        self.assertIsNotNone(cj)

    def test_todos_titulares_mayores_18_dev_excepcion(self):
        p1 = Persona('pepe', 'ape1', '12345678F')
        p2 = Persona('maria', 'ape1', '00045678K')
        cj = CuentaJoven('12345678912345678900', [p1,p2])
        self.assertRaises(Exception)

    def test_un_titular_menor_18_dev_instancia(self):
        p1 = Persona('pepe', 'ape1', '12345678F')
        p2 = PersonaJoven('maria', 'ape1', '00045678K', 16)
        cj = CuentaJoven('12345678912345678900', [p1,p2])
        self.assertIsNotNone(cj)
