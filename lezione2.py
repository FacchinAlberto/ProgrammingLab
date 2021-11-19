def Somma(my_list):
  somma = 0
  for item in my_list:
    somma = somma + item
  return somma

n=int(input('Inserisci il numero degli elementi: '))
my_list=[]
for i in range(n):
    n = int(input('Inserire {} valore'.format(i+1)))
    my_list.append(n)

print("La somma dei valori presenti nella lista è ", Somma(my_list))