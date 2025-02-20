import unittest
from calculo_desplazamiento import calculo_desplazamiento  # Importar la función desde su módulo

class TestCalculoDesplazamiento(unittest.TestCase):
    def test_caso_normal(self):
        self.assertAlmostEqual(calculo_desplazamiento(10, 2, 5), 10*5 + 0.5*2*5**2, places=5)

    def test_sin_aceleracion(self):
        self.assertAlmostEqual(calculo_desplazamiento(10, 0, 5), 10*5, places=5)

    def test_sin_velocidad_inicial(self):
        self.assertAlmostEqual(calculo_desplazamiento(0, 2, 5), 0.5*2*5**2, places=5)

    def test_tiempo_cero(self):
        self.assertEqual(calculo_desplazamiento(10, 2, 0), 0)

    def test_aceleracion_negativa(self):
        self.assertAlmostEqual(calculo_desplazamiento(10, -2, 5), 10*5 + 0.5*(-2)*5**2, places=5)

    def test_valores_negativos(self):
        self.assertAlmostEqual(calculo_desplazamiento(-10, -2, 5), -10*5 + 0.5*(-2)*5**2, places=5)

    def test_valores_grandes(self):
        self.assertAlmostEqual(calculo_desplazamiento(1e6, 1e3, 1e3), 1e6*1e3 + 0.5*1e3*(1e3**2), places=5)

if __name__ == '__main__':
    unittest.main()
