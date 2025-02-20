import unittest
import numpy as np
from lanzamiento_proyectiles import alcance, altura_max  # Importar funciones desde el módulo

class TestMovimientoParabolico(unittest.TestCase):
    # ---- Pruebas para alcance ----
    def test_alcance_angulo_45(self):
        vi = 10  # m/s
        theta = 45
        esperado = (vi**2 * np.sin(np.radians(90))) / 9.81  # Máximo alcance
        self.assertAlmostEqual(alcance(vi, theta), esperado, places=5)

    def test_alcance_angulo_0(self):
        self.assertEqual(alcance(10, 0), 0)

    def test_alcance_angulo_90(self):
        self.assertEqual(alcance(10, 90), 0)

    def test_alcance_velocidad_cero(self):
        self.assertEqual(alcance(0, 45), 0)

    def test_alcance_velocidad_alta(self):
        vi = 1000  # m/s
        theta = 30
        esperado = (vi**2 * np.sin(np.radians(60))) / 9.81
        self.assertAlmostEqual(alcance(vi, theta), esperado, places=2)

    def test_alcance_angulo_negativo(self):
        with self.assertRaises(ValueError):
            alcance(10, -10)

    def test_alcance_angulo_mayor_180(self):
        with self.assertRaises(ValueError):
            alcance(10, 190)

    def test_alcance_entrada_invalida(self):
        with self.assertRaises(TypeError):
            alcance("10", 45)
        with self.assertRaises(TypeError):
            alcance(10, None)

    # ---- Pruebas para altura_max ----
    def test_altura_max_angulo_90(self):
        vi = 10  # m/s
        theta = 90
        esperado = (vi**2 * np.sin(np.radians(90))**2) / (2 * 9.81)
        self.assertAlmostEqual(altura_max(vi, theta), esperado, places=5)

    def test_altura_max_angulo_0(self):
        self.assertEqual(altura_max(10, 0), 0)

    def test_altura_max_velocidad_cero(self):
        self.assertEqual(altura_max(0, 45), 0)

    def test_altura_max_velocidad_alta(self):
        vi = 1000  # m/s
        theta = 75
        esperado = (vi**2 * np.sin(np.radians(theta))**2) / (2 * 9.81)
        self.assertAlmostEqual(altura_max(vi, theta), esperado, places=2)

    def test_altura_max_angulo_negativo(self):
        with self.assertRaises(ValueError):
            altura_max(10, -10)

    def test_altura_max_angulo_mayor_180(self):
        with self.assertRaises(ValueError):
            altura_max(10, 190)

    def test_altura_max_entrada_invalida(self):
        with self.assertRaises(TypeError):
            altura_max("10", 45)
        with self.assertRaises(TypeError):
            altura_max(10, None)

if __name__ == '__main__':
    unittest.main()
