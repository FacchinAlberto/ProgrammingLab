def Stampa(list):
    for item in list:
        print(item)

def Statistiche(list, n):
    max = int(list[0])
    min = max
    somma = 0
    for item in list:
        somma += int(item)
        if int(item) > max:
            max = int(item)
        elif int(item) < min:
            min = int(item)
    media = somma/int(n)
    return max, min, somma, media

def Somma_vettoriale(list1, list2, n):
    for i in range(int(n)):
        list3[i] =  list2[i] + list2[i]

my_list1 = []
my_list2 = []
n = input('Inserire numero elementi della lista: ')
for i in range(int(n)):
    my_list1.append(input('Inserire {}\212 elemento lista1: '.format(i)))
    my_list2.append(input('Inserire {}\212 elemento lista2: '.format(i)))

print('\n')
Stampa(my_list1)
print('\n')
Stampa(my_list2)

max, min, somma, media = Statistiche(my_list1, n)
print('\nLista 1\nMax: {}, Min: {}, Somma: {}, Media: {}'.format(max, min, somma, media))
max, min, somma, media = Statistiche(my_list2, n)
print('\nLista2\nMax: {}, Min: {}, Somma: {}, Media: {}'.format(max, min, somma, media))

print('\nSomma vettoriale:')
my_list3 = Somma_vettoriale(my_list1, my_list2, n)
for item in my_list3:
    print(item)