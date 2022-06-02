import unittest
from jmpp_ejercicio_2 import binario2decimal

class TestEjercicio2(unittest.TestCase):
    def test_binario_0_dev_decimal_0(self):
        lista = [0]
        resp = binario2decimal(lista)
        self.assertEqual(resp, 0)

    def test_binario_01_dev_decimal_1(self):
        lista = [0,1]
        resp = binario2decimal(lista)
        self.assertEqual(resp, 1)

    def test_binario_0001_dev_decimal_1(self):
        lista = [0,0,0,1]
        resp = binario2decimal(lista)
        self.assertEqual(resp, 1)

    def test_binario_101_dev_decimal_5(self):
        lista = [1,0,1]
        resp = binario2decimal(lista)
        self.assertEqual(resp, 5)

    def test_binario_1011101_dev_decimal_93(self):
        lista = [1,0,1,1,1,0,1]
        resp = binario2decimal(lista)
        self.assertEqual(resp, 93)