import unittest
from CSVFile import CSVFile
from CSVFile import DateCSVFile

#python -m unittest TestCSVFile.py

class TestCSVFile(unittest.TestCase):
    def test_nomefile(self):
        print('\n')
        csvfile = CSVFile('Vendite shampoo', 'shampoo_sales.csv')
        self.assertEqual(csvfile.name, 'Vendite shampoo')
    def test_get_date_vendite(self):
        datecsvfile = DateCSVFile('Vendite shampoo', 'shampoo_sales.csv')
        date_list = datecsvfile.get_data()
        self.assertEqual(datecsvfile.get_data(), date_list)