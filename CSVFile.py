class CSVFile():
    def __init__(self, name, file):
        self.name = name
        self.file = file
    def get_data(self, my_list):
        my_list = []
        file = open('shampoo_sales.csv', 'r')
        for line in file:
            elem = line.split(',')
            if elem[0] != 'Date':
                my_list.append(elem)
        
        file.close()
        return my_list;

mia_lista = []
obj = CSVFile('Vendite shampoo', 'shampoo_sales.csv')
mia_lista = obj.get_data(mia_lista)
print('Nome file: {}'.format(obj.name))
print('Contenuto: ')
for x in mia_lista:
    #print("['{}, {}']".format(x[0], x[1]))
    print(x)