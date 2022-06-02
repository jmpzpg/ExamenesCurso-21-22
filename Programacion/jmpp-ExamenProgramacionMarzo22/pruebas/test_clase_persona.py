'''
Jose Manuel Peres Puig - Examen de Programación del segundo trimestre
Tests para la clase Persona
'''

import unittest
from clase_persona import Persona

class TestClasePersona(unittest.TestCase):
    def test_existencia(self):
        p = Persona('Pepe','Alba','12345678V')
        self.assertIsNotNone(p)

    def test_constructor_con_parametros_obligatorios(self):
        p = Persona('Pepe','Alba','12345678V')
        r1 = p.nombre
        r2 = p.apellido1
        r3 = p.apellido2
        r4 = p.dni
        self.assertEqual(r1,'Pepe')
        self.assertEqual(r2,'Alba')
        self.assertEqual(r3,None)
        self.assertEqual(r4,'12345678V')
    
    def test_constructor_con_todos_los_parametros(self):
        p = Persona('Pepe','Alba','12345678V','Segundo')
        r1 = p.nombre
        r2 = p.apellido1
        r3 = p.apellido2
        r4 = p.dni
        self.assertEqual(r1,'Pepe')
        self.assertEqual(r2,'Alba')
        self.assertEqual(r3,'Segundo')
        self.assertEqual(r4,'12345678V')

    def test_impresion(self):
        p = Persona('Pepe','Alba','12345678V','Segundo')
        resp = p.__str__()
        salida = 'Pepe Alba Segundo con DNI: 12345678V'
        self.assertEqual(resp, salida)
    