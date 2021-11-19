my_file = open('shampoo_sales.txt', 'r')
print(my_file.read())
my_file.close()

# Apro il file
my_file = open('shampoo_sales.txt', 'r')
# Leggo il contenuto
my_file_contents = my_file.read()
# Stampo a schermo i primi 50 caratteri
if len(my_file_contents) > 50:
    print(my_file_contents[0:50] + ' ecc.')
else:
   print(my_file_contents)
# Chiudo il file
my_file.close()

my_file = open('shampoo_sales.txt', 'r')
print(my_file.readline())
print(my_file.readline())

my_file = open('shampoo_sales.txt', 'r')
for x in my_file:
    print(x)

my_file = open('saluti.txt', 'w')
my_file.write('Ciao mondo!')
my_file.close()