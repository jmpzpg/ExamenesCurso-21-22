import unittest
from OO.classPersona import Persona
import codigo

class TestCodigo(unittest.TestCase):

    def test_si_no_arg_devuelve_cero(self):
        resp = codigo.sumar([])
        self.assertEqual(resp, 0)

    def test_si_lista_de_int_o_float_devuelve_suma(self):
        resp = codigo.sumar([1,3,5.5])
        self.assertEqual(resp,9.5)
       
    def test_si_cadenas_devuelve_cero(self):
        resp = codigo.sumar(['c', 3])
        self.assertEqual(resp, 0)

    def test_si_num_complejos_devuelve_cero(self):
        resp = codigo.sumar([2+3j, 3])
        self.assertEqual(resp, 0)

    def test_si_obj_no_numericos_devuelve_cero(self):
        p = Persona('Jose', 17, '12345678K')
        resp = codigo.sumar([p])
        self.assertEqual(resp, 0)
    