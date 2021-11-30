from datetime import datetime

class CSVFile():
    def __init__(self, name, file):
        self.name = name
        self.file = file
    def get_data(self):
        date_vendite = []
        try:
            my_file = open(self.file, 'r')
            for line in my_file:
                elem = line.rstrip().split(',')
                if elem[0] != 'Date':
                    date_vendite.append(datetime.strptime(elem[0], '%d-%m-%Y'))
            
            my_file.close()
            return date_vendite;
        except Exception as e:
            print('ERROR: Impossibile aprire file "{}"'.format(self.file))

obj = CSVFile(input('Nome file: '), input('Percorso file: '))
mia_lista = obj.get_data()
print('Nome file: {}'.format(obj.name))
print('Contenuto: ')
for data in mia_lista:
    print(data.strftime('%d-%m-%Y'))