import unittest

from sistemadenumeracion import decimal_a_binario

class TestDecimalABinario(unittest.TestCase):

    def test_decimal_a_binario(self):
        self.assertEqual(decimal_a_binario(10), "1010")
        self.assertEqual(decimal_a_binario(42), "101010")
        self.assertEqual(decimal_a_binario(128), "10000000")
        self.assertEqual(decimal_a_binario(255), "11111111")

if __name__ == '__main__':
    unittest.main()