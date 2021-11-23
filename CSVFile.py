class CSVFile():
    def __init__(self, name, file):
        self.name = name
        self.file = file
    def get_data(self):
        my_list = []
        my_file = open(self.file, 'r')
        for line in my_file:
            elem = line.split(',')
            if elem[0] != 'Date':
                my_list.append(elem)
        
        my_file.close()
        return my_list;

mia_lista = []
obj = CSVFile('Vendite shampoo', 'shampoo_sales.csv')
mia_lista = obj.get_data()
print('Nome file: {}'.format(obj.name))
print('Contenuto: ')
for x in mia_lista:
    #print("['{}, {}']".format(x[0], x[1]))
    print(x)