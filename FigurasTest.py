import unittest
from figuras import Figuras


class TestFiguras(unittest.TestCase):

    def setUp(self):
        self.figuras = Figuras()

    def test_area_cuadrado_lado_5(self):

        resultado = self.figuras.cuadrado(5)
        self.assertEqual(25, resultado)

    def test_area_cuadrado_lado_6(self):

        resultado = self.figuras.cuadrado(6)
        self.assertEqual(36, resultado)

    def test_area_cuadrado_lado_g(self):

        resultado = self.figuras.cuadrado('g')
        self.assertEqual('dato incorrecto', resultado)

    def test_area_cuadrado_lado_4_punto_5(self):

        resultado = self.figuras.cuadrado(4.5)
        self.assertEqual(20.25, resultado)

    def test_area_rectangulo_base_5_altura_6(self):

        resultado = self.figuras.rectangulo(5, 6)
        self.assertEqual(30, resultado)

    def test_area_rectangulo_base_5_punto_5_altura_6_punto_4(self):

        resultado = self.figuras.rectangulo(5.5, 6.4)
        self.assertEqual(35.2, resultado)

    def test_area_rectangulo_g_f(self):

        resultado = self.figuras.rectangulo('g', 'f')
        self.assertEqual('dato incorrecto', resultado)

    def test_area_triangulo_base8_altura_7(self):

        resultado = self.figuras.triangulo(8, 7)
        self.assertEqual(28, resultado)

    
if __name__ == '__main__':
    unittest.main()
