import unittest
from math import sqrt
from caida_libre import caida_libre  # Importar la función desde su módulo

class TestCaidaLibre(unittest.TestCase):
    def test_caso_normal(self):
        self.assertAlmostEqual(caida_libre(10, 9.81), sqrt((2*10)/9.81), places=5)

    def test_gravedad_terrestre(self):
        self.assertAlmostEqual(caida_libre(100, 9.81), sqrt((2*100)/9.81), places=5)

    def test_altura_cero(self):
        self.assertEqual(caida_libre(0, 9.81), 0)

    def test_gravedad_cero(self):
        with self.assertRaises(ZeroDivisionError):
            caida_libre(10, 0)

    def test_altura_negativa(self):
        with self.assertRaises(ValueError):
            caida_libre(-10, 9.81)

    def test_gravedad_negativa(self):
        with self.assertRaises(ValueError):
            caida_libre(10, -9.81)

    def test_valores_grandes(self):
        self.assertAlmostEqual(caida_libre(1e6, 9.81), sqrt((2*1e6)/9.81), places=5)

if __name__ == '__main__':
    unittest.main()
