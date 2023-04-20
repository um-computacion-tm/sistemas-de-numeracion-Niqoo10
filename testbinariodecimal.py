import unittest

from sistemadenumeracion import binario_a_decimal

class TestBinarioADecimal(unittest.TestCase):

    def test_binario_a_decimal(self):
        self.assertEqual(binario_a_decimal("1010"), 10)
        self.assertEqual(binario_a_decimal("101010"), 42)
        self.assertEqual(binario_a_decimal("10000000"), 128)
        self.assertEqual(binario_a_decimal("11111111"), 255)

if __name__ == '__main__':
    unittest.main()
