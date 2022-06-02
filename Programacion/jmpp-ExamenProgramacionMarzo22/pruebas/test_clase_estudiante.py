import unittest

from clase_estudiante import Estudiante

class TestClaseEstudiante(unittest.TestCase):
    def test_existencia(self):
        e = Estudiante()
        self.assertIsNotNone(e)

    def test_constructor_con_parametros(self):
        e = Estudiante('Esperanza', 8)
        self.assertEqual(e.nombre, 'Esperanza')
        self.assertEqual(e.nota, 8)

    def test_nota_menor50_dev_suspenso(self):
        e = Estudiante('Esperanza', 45)
        resp = e.es_aprobado()
        self.assertEqual(resp, 'Suspenso')

    def test_nota_mayoroigual50_dev_aprobado(self):
        e = Estudiante('Esperanza', 50)
        resp = e.es_aprobado()
        self.assertEqual(resp, 'Aprobado')

    def test_modificar_minaprobado_dev_suspenso(self):
        e = Estudiante('Esperanza', 50)
        Estudiante.min_aprobado = 60
        resp = e.es_aprobado()
        self.assertEqual(resp, 'Suspenso')