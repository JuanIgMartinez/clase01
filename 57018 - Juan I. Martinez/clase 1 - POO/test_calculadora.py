#Juan I. Martinez, Legajo 57018

import unittest
from calculadora import *

class TestCalculadora(unittest.TestCase):

    def test_nro_1(self):
        c1 = Calculadora()
        c1.ingresar('1')
        c1.ingresar('+')
        c1.ingresar('1')
        c1.ingresar('=')
        self.assertEqual(c1.resultado, 2)

    def test_nro_2(self):
        c1 = Calculadora()
        c1.ingresar('3')
        c1.ingresar('+')
        c1.ingresar('5')
        c1.ingresar('=')
        self.assertEqual(c1.resultado, 8)

    def test_nro_3(self):
        c1 = Calculadora()
        c1.ingresar('1')
        c1.ingresar('1')
        c1.ingresar('1')
        c1.ingresar('+')
        c1.ingresar('1')
        c1.ingresar('=')
        self.assertEqual(c1.resultado, 112)

    def test_nro_4(self):
        c1 = Calculadora()
        c1.ingresar('1')
        c1.ingresar('+')
        c1.ingresar('1')
        c1.ingresar('1')
        c1.ingresar('1')
        c1.ingresar('1')
        c1.ingresar('=')
        self.assertEqual(c1.resultado, 1112)

    def test_nro_5(self):
        c1 = Calculadora()
        c1.ingresar('1')
        c1.ingresar('+')
        c1.ingresar('2')
        c1.ingresar('+')
        c1.ingresar('3')
        c1.ingresar('+')
        c1.ingresar('4')
        c1.ingresar('=')
        self.assertEqual(c1.resultado, 10)

    def test_nro_6(self):
        c1 = Calculadora()
        c1.ingresar('3')
        c1.ingresar('-')
        c1.ingresar('2')
        c1.ingresar('=')
        self.assertEqual(c1.resultado, 1)

    def test_nro_7(self):
        c1 = Calculadora()
        c1.ingresar('3')
        c1.ingresar('*')
        c1.ingresar('2')
        c1.ingresar('=')
        self.assertEqual(c1.resultado, 6)

    def test_nro_8(self):
        c1 = Calculadora()
        c1.ingresar('6')
        c1.ingresar('%')
        c1.ingresar('3')
        c1.ingresar('=')
        self.assertEqual(c1.resultado, 2)

    def test_nro_9(self):
        c1 = Calculadora()
        c1.ingresar('4')
        c1.ingresar('-')
        c1.ingresar('2')
        c1.ingresar('=')
        self.assertEqual(c1.resultado, 2)

#9 test funcionando, leer notas en el otro archivo para mejorar el codigo y así poder hacer que funcione con mas argumentos


if __name__ == '__main__':
    unittest.main()