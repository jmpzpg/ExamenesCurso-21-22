import unittest
from jmpp_ejercicio_1 import invierte_palabras_en_cadena

class TestEjercicio1(unittest.TestCase):
    def test_cadena_una_palabra_menor_5_caracteres_dev_palabra_sin_cambios(self):
        cadena = 'rosa'
        resp = invierte_palabras_en_cadena(cadena)
        self.assertEqual(resp, cadena)

    def test_cadena_una_palabra_mayor_5_caracteres_dev_palabra_invertida(self):
        cadena = 'roseta'
        resp = invierte_palabras_en_cadena(cadena)
        self.assertEqual(resp, 'atesor')
    
    def test_cadena_con_palabra_mayores_y_menores_5_caracteres_dev_cad_con_palabras_invertidas(self):
        cadena = 'desde santurce a bilbao'
        resp = invierte_palabras_en_cadena(cadena)
        self.assertEqual(resp, 'edsed ecrutnas a oablib')