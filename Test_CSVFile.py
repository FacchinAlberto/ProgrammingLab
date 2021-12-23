import unittest
from CSVFile import CSVFile
from CSVFile import DateCSVFile
from CSVFile import ErroreAIDA

#python -m unittest Test_CSVFile.py

class TestCSVFile(unittest.TestCase):
    def test_nomefile(self):
        print('\n')
        csvfile = CSVFile('Vendite shampoo', 'shampoo_sales.csv')
        self.assertEqual(csvfile.name, 'Vendite shampoo')

    def test_get_date_vendite(self):
        datecsvfile = DateCSVFile('Vendite shampoo', 'shampoo_sales.csv')
        date_list = datecsvfile.get_data()
        self.assertEqual(datecsvfile.get_data(), date_list)

    def test_sum(self):
        csvfile = CSVFile('Vendite shampoo', 'shampoo_sales.csv')
        self.assertEqual(csvfile.get_data(), [['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ['01-03-2012', '183.1'], ['01-04-2012', '119.3'], ['01-05-2012', '180.3'], ['01-06-2012', '168.5'], ['01-07-2012', '231.8'], ['01-08-2012', '224.5'], ['01-09-2012', '192.8'], ['01-10-2012', '122.9'], ['01-11-2012', '336.5'], ['01-12-2012', '185.9'], ['01-01-2013', '194.3'], ['01-02-2013', '149.5'], ['01-03-2013', '210.1'], ['01-04-2013', '273.3'], ['01-05-2013', '191.4'], ['01-06-2013', '287.0'], ['01-07-2013', '226.0'], ['01-08-2013', '303.6'], ['01-09-2013', '289.9'], ['01-10-2013', '421.6'], ['01-11-2013', '264.5'], ['01-12-2013', '342.3'], ['01-01-2014', '339.7'], ['01-02-2014', '440.4'], ['01-03-2014', '315.9'], ['01-04-2014', '439.3'], ['01-05-2014', '401.3'], ['01-06-2014', '437.4'], ['01-07-2014', '575.5'], ['01-08-2014', '407.6'], ['01-09-2014', '682.0'], ['01-10-2014', '475.3'], ['01-11-2014', '581.3'], ['01-12-2014', '646.9']])
        self.assertEqual(csvfile.get_data_start_end(1, 36), csvfile.get_data())