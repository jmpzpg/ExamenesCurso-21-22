'''
Jose Manuel Peres Puig - Examen de Programación del segundo trimestre
Tests para la clase Persona
'''

import unittest
from clase_cuenta import Cuenta
from clase_persona import Persona

class TestClaseCuenta(unittest.TestCase):
    def test_existencia(self):
        c = Cuenta('12345678912345678900')
        self.assertIsNotNone(c)
    
    def test_constructor_con_parametros(self):
        p = Persona('Pepe','Alba','12345678V','Segundo')
        c = Cuenta('12345678912345678900', 0.02, [p], 25)
        self.assertEqual(c.numero, '12345678912345678900')
        self.assertEqual(c.interes, 0.02)
        self.assertEqual(c.titulares, p.nombre)
        self.assertEqual(c.saldo, 25)
