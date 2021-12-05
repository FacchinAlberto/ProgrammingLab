from datetime import datetime

class ErroreAIDA(Exception):
    def file_type(self, file):
        print('\nFile {} non supportato'.format(file))

    def range_lines(self, start, end):
        print('\nImpossibile leggere da riga {} a riga {}'.format(start, end))

    def float_conversion(self, x):
        print('\nVALUE ERROR: Impossibile acquisire valore float, la variabile vale "{}"'.format(x))

class CSVFile():
    def __init__(self, name, file):
        self.name = name
        if type(file) == str:
            self.file = file
        else:
            raise ErroreAIDA.file_type(file)

    def __str__(self):
        return self.name, self.file
    
    #funzione creata appositamente per Test_CSVFile.py
    def nome_file(self):
        return str(self.name)

    def intex(self):
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

    def get_data_start_end(self, start, end):
        my_list = []
        try:
            start = int(start)
            end = int(end)
        except TypeError:
            raise ErroreAIDA.range_lines(start, end)
            print('\nCausa intervallo di righe non leggibile ho letto tutto il file')
        try:
            my_file = open(self.file, 'r')
            my_list.append(my_file.readlines()[start:end+1])
            print(my_list)
            my_file.close()
        except Exception as e:
            print('ERROR: Impossibile aprire file "{}"'.format(self.file))

class NumericalCSVFile(CSVFile):
    def get_data(self):
        my_list = super().get_data()
        for item in my_list:
            try:
                item[1] = float(item[1])
            except ValueError:
                #raise ErroreAIDA.float_conversion(item[1])
                print('VALUE ERROR: Impossibile acquisire valore float, la variabile vale "{}"'.format(item[1]))
        return my_list

class DateCSVFile(CSVFile):
    def get_data(self):
        my_list = super().get_data()
        date_vendite = []
        for item in my_list:
            date_vendite.append(datetime.strptime(item[0], '%d-%m-%Y'))
        return date_vendite

obj = CSVFile(input('Nome file: '), input('Percorso file: '))
obj.get_data_start_end(input("\nStart: "), input("\nEnd: "))
#mia_lista = obj.get_data()
#print('Nome file: {}'.format(obj.name))
#print('Contenuto: ')
#for x in mia_lista:
    #print(x)
numobj = NumericalCSVFile(obj.name, obj.file)
mia_lista = numobj.get_data()
print('\nContenuto con conversione in float: ')
for x in mia_lista:
    print(x)
dateobj = DateCSVFile(obj.name, obj.file)
mia_lista = dateobj.get_data()
print('\nIntestazione: ')
print(dateobj.intex())
print('\nLista di date: ')
for data in mia_lista:
    print(data.strftime('%d-%m-%Y'))