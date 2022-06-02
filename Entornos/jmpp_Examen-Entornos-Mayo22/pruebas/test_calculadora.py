import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    '''
        clase que recoge las pruebas unitarias a la clase Calculadora
    '''

    def test_existencia(self):
        calc = Calculadora()
        self.assertIsNotNone(calc)
        

    def test_suma_con_enteros(self):
        calc = Calculadora()
        resp = calc.suma(2,3)
        self.assertEqual(resp, 5)

    def test_suma_con_float(self):
        calc = Calculadora()
        resp = calc.suma(2.0,3.0)
        self.assertEqual(resp, 5.0) 

    def test_suma_con_str_dev_typeerror(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):calc.suma('2',3)

    def test_suma_con_letra_dev_typeerror(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):calc.suma('a',3)

    def test_resta_con_enteros(self):
        calc = Calculadora()
        resp = calc.resta(3,2)
        self.assertEqual(resp, 1)

    def test_resta_con_float(self):
        calc = Calculadora()
        resp = calc.resta(3.0,2.0)
        self.assertEqual(resp, 1.0) 

    def test_resta_con_str_dev_typeerror(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):calc.resta('2',3)

    def test_resta_con_letra_dev_typeerror(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):calc.resta('a',3)

    def test_multiplicacion_con_enteros(self):
        calc = Calculadora()
        resp = calc.multiplicacion(2,3)
        self.assertEqual(resp, 6)

    def test_multiplicacion_con_float(self):
        calc = Calculadora()
        resp = calc.multiplicacion(2.0,3.0)
        self.assertEqual(resp, 6.0) 

    def test_multiplicacion_con_letra_no_dev_lo_esperado(self):
        calc = Calculadora()
        resp = calc.multiplicacion('a',3)
        self.assertEqual(resp, 'aaa')

    def test_multiplicacion_con_str_no_dev_lo_esperado(self):
        calc = Calculadora()
        resp = calc.multiplicacion('2',3)
        self.assertNotEqual(resp, 6)

    def test_division_con_enteros(self):
        calc = Calculadora()
        resp = calc.division(4,2)
        self.assertEqual(resp, 2)

    def test_division_con_float(self):
        calc = Calculadora()
        resp = calc.division(4.0,2.0)
        self.assertEqual(resp, 2.0) 

    def test_division_con_str_dev_typeerror(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):calc.division('4',2)

    def test_division_con_letra_dev_typeerror(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):calc.division('a',2)

    def test_suma_con_algun_arg_nulo_dev_nulo(self):
        calc = Calculadora()
        resp = calc.suma(4, None)
        self.assertEqual(resp, None)

    def test_resta_con_algun_arg_nulo_dev_nulo(self):
        calc = Calculadora()
        resp = calc.resta(4, None)
        self.assertEqual(resp, None)
    
    def test_multiplicacion_con_algun_arg_nulo_dev_nulo(self):
        calc = Calculadora()
        resp = calc.multiplicacion(4, None)
        self.assertEqual(resp, None)

    def test_division_con_arg_nulo_en_numerador_dev_nulo(self):
        calc = Calculadora()
        resp = calc.division(None, 2)
        self.assertEqual(resp, None)

    def test_division_con_arg_nulo_en_denominador_dev_nulo(self):
        calc = Calculadora()
        resp = calc.division(6, None)
        self.assertEqual(resp, None)

    def test_division_por_cero_dev_eror_de_division_por_cero(self):
        calc = Calculadora()
        with self.assertRaises(ZeroDivisionError):calc.division(5,0)

    