import unittest
import numpy as np # type: ignore
from suma_vectores import suma_vectores  # Importar la función desde su módulo

class TestSumaVectores(unittest.TestCase):
    def test_vectores_mismo_tamano(self):
        v1 = np.array([1, 2, 3])
        v2 = np.array([4, 5, 6])
        esperado = np.array([5, 7, 9])
        np.testing.assert_array_equal(suma_vectores(v1, v2), esperado)

    def test_vectores_con_negativos(self):
        v1 = np.array([-1, -2, -3])
        v2 = np.array([4, -5, 6])
        esperado = np.array([3, -7, 3])
        np.testing.assert_array_equal(suma_vectores(v1, v2), esperado)

    def test_vectores_con_ceros(self):
        v1 = np.array([0, 0, 0])
        v2 = np.array([1, 2, 3])
        esperado = np.array([1, 2, 3])
        np.testing.assert_array_equal(suma_vectores(v1, v2), esperado)

    def test_vectores_grandes(self):
        v1 = np.ones(1000000)
        v2 = np.ones(1000000)
        esperado = np.full(1000000, 2)
        np.testing.assert_array_equal(suma_vectores(v1, v2), esperado)

    def test_vectores_distinto_tamano(self):
        v1 = np.array([1, 2, 3])
        v2 = np.array([4, 5])
        with self.assertRaises(ValueError):
            suma_vectores(v1, v2)

    def test_entrada_invalida(self):
        with self.assertRaises(TypeError):
            suma_vectores(5, [1, 2, 3])
        with self.assertRaises(TypeError):
            suma_vectores(None, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()