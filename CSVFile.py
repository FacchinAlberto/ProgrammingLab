from datetime import datetime

class CSVFile():
    def __init__(self, name, file):
        self.name = name
        self.file = file

    def __str__(self):
        try:
            my_file = open(self.file, 'r')
            intex = my_file.readline().rstrip().split(',')
            my_file.close()
            return intex;
        except Exception as e:
            print('ERROR: Impossibile aprire file "{}"'.format(self.file))
    def get_data(self):
        my_list = []
        try:
            my_file = open(self.file, 'r')
            for line in my_file:
                elem = line.rstrip().split(',')
                if elem[0] != 'Date':
                    my_list.append(elem)
            
            my_file.close()
            return my_list;
        except Exception as e:
            print('ERROR: Impossibile aprire file "{}"'.format(self.file))

class NumericalCSVFile(CSVFile):
    def get_data(self):
        my_list = super().get_data()
        for item in my_list:
            try:
                item[1] = float(item[1])
            except ValueError:
                print('VALUE ERROR: Impossibile acquisire valore float, la variabile vale "{}"'.format(item[1]))
        return my_list

class DateCSVFile(CSVFile):
    def get_date_vendite(self):
        my_list = super().get_data()
        date_vendite = []
        for item in my_list:
            date_vendite.append(datetime.strptime(item[0], '%d-%m-%Y'))
        return date_vendite

obj = CSVFile(input('Nome file: '), input('Percorso file: '))
mia_lista = obj.get_data()
print('Nome file: {}'.format(obj.name))
print('Contenuto: ')
for x in mia_lista:
    print(x)
numobj = NumericalCSVFile(obj.name, obj.file)
mia_lista = numobj.get_data()
print('\nContenuto con conversione in float: ')
for x in mia_lista:
    print(x)
dateobj = DateCSVFile(obj.name, obj.file)
mia_lista = dateobj.get_date_vendite()
print('\nIntestazione: ')
print(dateobj.__str__())
print('\nLista di date: ')
for data in mia_lista:
    print(data.strftime('%d-%m-%Y'))