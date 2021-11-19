def Somma(values):
    somma  = 0.0
    for item in values:
        somma += float(item)
    return somma

my_file = open('shampoo_sales.txt')
values = []
somma = 0.0
for line in my_file:
    elem = line.split(',')
    if elem[0] != 'Date':
        value = float(elem[1])
        values.append(value)
        somma = Somma(values)

print('La somma è: {}'.format(somma))

my_file.close()