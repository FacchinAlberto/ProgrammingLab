from calcolatrice import Calcolatrice
import unittest

#python -m unittest Test_calcolatrice.py

class TestCalcolatrice(unittest.TestCase):
    def test_type_ok(self):
        calc = Calcolatrice()
        self.assertFalse(calc.type_ok('test'))

    def test_somma(self):
        calc = Calcolatrice()
        self.assertEqual(calc.somma(8, -2), 6) #8 + (-2) = 6
        self.assertRaises(TypeError, calc.somma, 8, 'test')
    
    def test_sottrazione(self):
        calc = Calcolatrice()
        self.assertEqual(calc.sottrazione(8, -7), 15)  #8 - (-7) = 15
    
    def test_prodotto(self):
        calc = Calcolatrice()
        self.assertEqual(calc.prodotto(5, -2), -10)

    def test_divisione(self):
        calc = Calcolatrice()
        self.assertEqual(calc.divisione(5, -5), -1)
        self.assertEqual(calc.divisione(8, 1), 8)
        self.assertRaises(ZeroDivisionError, calc.divisione, 8, 0)

    def test_potenza(self):
        calc = Calcolatrice()
        self.assertEqual(calc.potenza(2, 4), 16)
        self.assertEqual(calc.potenza(-2, 2), 4)
        self.assertEqual(calc.potenza(2, -1), 0.5)
        
    def test_radice(self):
        calc = Calcolatrice()
        self.assertEqual(calc.radice(4), 2.0)
        self.assertRaises(TypeError, calc.radice, 'ciao') 
        self.assertRaises(ValueError, calc.radice, -2)

    def test_modulo(self):
        calc = Calcolatrice()
        self.assertEqual(calc.modulo(7, 4), 3)
        self.assertEqual(calc.modulo(-2, 2), 0)

    def test_cambio_base(self):
        calc = Calcolatrice()
        self.assertEqual(calc.cambio_base(8), '1000')