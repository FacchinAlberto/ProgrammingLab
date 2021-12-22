import unittest
from automa import Automa, esegui

#python -m unittest Test_automa.py

class TestAutoma(unittest.TestCase):
    def test_capo_up(self):
        print('\n')
        aut = Automa()
        self.assertEqual(aut.biancheria_up(), 1)