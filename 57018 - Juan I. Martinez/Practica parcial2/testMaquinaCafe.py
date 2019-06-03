import unittest
from maquinaCafe import Maquina_de_cafe

class test_Maquina_de_cafe(unittest.TestCase):

    def setUp(self):
        self.client = Maquina_de_cafe(100, 100)

    def test_numero1(self):
        self.assertEqual(self.client.check_moneda(1), "moneda ok")
        self.assertEqual(self.client.check_vaso("si"), "vaso ok")
        self.assertEqual(self.client.check_leche("si"), "con leche")
        self.assertEqual(self.client.check_azucar(3), 3)

if __name__ == '__main__':
    unittest.main()