import unittest
from conversion_velocidades import conversion_velocidades  # Importar la función desde su módulo

class TestConversionVelocidades(unittest.TestCase):
    def test_kmh_a_ms(self):
        self.assertAlmostEqual(conversion_velocidades(36, 1), 10, places=5)

    def test_ms_a_kmh(self):
        self.assertAlmostEqual(conversion_velocidades(10, 2), 36, places=5)

    def test_valor_cero(self):
        self.assertEqual(conversion_velocidades(0, 1), 0)
        self.assertEqual(conversion_velocidades(0, 2), 0)

    def test_valores_negativos(self):
        self.assertAlmostEqual(conversion_velocidades(-36, 1), -10, places=5)
        self.assertAlmostEqual(conversion_velocidades(-10, 2), -36, places=5)

    def test_opcion_invalida(self):
        self.assertEqual(conversion_velocidades(50, 3), "Opción no válida")
        self.assertEqual(conversion_velocidades(50, 0), "Opción no válida")
        self.assertEqual(conversion_velocidades(50, -1), "Opción no válida")

    def test_valores_grandes(self):
        self.assertAlmostEqual(conversion_velocidades(1e6, 1), (1e6 * 1000 / 3600), places=5)
        self.assertAlmostEqual(conversion_velocidades(1e6, 2), (1e6 * 3600 / 1000), places=5)

if __name__ == '__main__':
    unittest.main()
