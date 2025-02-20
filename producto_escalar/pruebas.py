import unittest
import numpy as np # type: ignore
from producto_escalar import producto_escalar, angulo_vectores  # Importar funciones desde el módulo

class TestVectores(unittest.TestCase):
    # ---- Pruebas para producto_escalar ----
    def test_producto_escalar_vectores_mismo_tamano(self):
        v1 = np.array([1, 2, 3])
        v2 = np.array([4, 5, 6])
        esperado = 1*4 + 2*5 + 3*6  # 32
        self.assertEqual(producto_escalar(v1, v2), esperado)

    def test_producto_escalar_vectores_con_negativos(self):
        v1 = np.array([-1, -2, -3])
        v2 = np.array([4, -5, 6])
        esperado = (-1*4) + (-2*-5) + (-3*6)  # -12
        self.assertEqual(producto_escalar(v1, v2), esperado)

    def test_producto_escalar_vectores_con_ceros(self):
        v1 = np.array([0, 0, 0])
        v2 = np.array([1, 2, 3])
        esperado = 0
        self.assertEqual(producto_escalar(v1, v2), esperado)

    def test_producto_escalar_vectores_grandes(self):
        v1 = np.ones(1000000)
        v2 = np.ones(1000000)
        esperado = 1000000
        self.assertEqual(producto_escalar(v1, v2), esperado)

    def test_producto_escalar_vectores_distinto_tamano(self):
        v1 = np.array([1, 2, 3])
        v2 = np.array([4, 5])
        with self.assertRaises(ValueError):
            producto_escalar(v1, v2)

    def test_producto_escalar_entrada_invalida(self):
        with self.assertRaises(TypeError):
            producto_escalar(5, np.array([1, 2, 3]))
        with self.assertRaises(TypeError):
            producto_escalar(None, np.array([1, 2, 3]))

    # ---- Pruebas para angulo_vectores ----
    def test_angulo_vectores_ortogonales(self):
        v1 = np.array([1, 0])
        v2 = np.array([0, 1])
        esperado = np.pi / 2  # 90 grados
        self.assertAlmostEqual(angulo_vectores(v1, v2), esperado, places=5)

    def test_angulo_vectores_identicos(self):
        v1 = np.array([1, 1])
        v2 = np.array([1, 1])
        esperado = 0  # Mismo vector, ángulo 0°
        self.assertAlmostEqual(angulo_vectores(v1, v2), esperado, places=5)

    def test_angulo_vectores_opuestos(self):
        v1 = np.array([1, 0])
        v2 = np.array([-1, 0])
        esperado = np.pi  # 180 grados
        self.assertAlmostEqual(angulo_vectores(v1, v2), esperado, places=5)

    def test_angulo_vectores_negativos(self):
        v1 = np.array([-1, -2])
        v2 = np.array([2, 1])
        esperado = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
        self.assertAlmostEqual(angulo_vectores(v1, v2), esperado, places=5)

    def test_angulo_vectores_con_ceros(self):
        v1 = np.array([0, 0])
        v2 = np.array([1, 1])
        with self.assertRaises(ValueError):
            angulo_vectores(v1, v2)  # No se puede calcular el ángulo con un vector nulo

    def test_angulo_vectores_distinto_tamano(self):
        v1 = np.array([1, 2, 3])
        v2 = np.array([4, 5])
        with self.assertRaises(ValueError):
            angulo_vectores(v1, v2)

    def test_angulo_vectores_entrada_invalida(self):
        with self.assertRaises(TypeError):
            angulo_vectores(5, np.array([1, 2, 3]))
        with self.assertRaises(TypeError):
            angulo_vectores(None, np.array([1, 2, 3]))

if __name__ == '__main__':
    unittest.main()
