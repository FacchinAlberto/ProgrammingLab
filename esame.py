import os

class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def get_data(self):
        if os.path.isfile(self.name):   #controllo se il file esiste e/o se quello che viene passato come parametro nella __init__ è un file
            my_list = []
            try:
                my_file = open(self.name, 'r')
                for line in my_file:
                    elem = line.rstrip().split(',')
                    if elem[0] != 'date':
                        elem[1] = int(elem[1])  #converto le migliaia di passeggeri in intero
                        my_list.append(elem)
                my_file.close()
                return my_list;
            except Exception as e:
                print('ERROR: impossibile aprire file "{}"'.format(self.name))
        else:
            raise ExamException('ERROR: file non leggibile o inesistente')

def compute_avg_monthly_difference(time_series, first_year, last_year):
    years = []
    months = []
    passengers = []
    first_year = int(first_year)
    last_year = int(last_year)

    for item in time_series:
        elem = str(item[0])
        year_and_month = elem.rstrip().split('-')   #in year_and_month viene messa una lista del tipo ['1953', '05']
        if int(year_and_month[0]) >= first_year and int(year_and_month[1])<= last_year:
            years.append(int(year_and_month[0]))
            months.append(int(year_and_month[1]))   #da verificare che io possa fare int()
            passengers.append(int(item[1]))
    
    diff = last_year - first_year
    avg_variation = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #inizializzo la lista delle variazioni medie con ogni elemento = 0, in modo da poter utilizzare successivamente il +=
    for i in range(0, 12):
        for j in range(0, diff):    #dovrei scrivere diff-1, ma visto che per es. 2021-2019 = 2, ed io devo considerare 3 anni (2019, 2020, 2021) poosso usare diff
            #print(passengers[(12*(j+1))+i]-passengers[(12*j)+i])    
            avg_variation[i] += passengers[(12*(j+1))+i]-passengers[(12*j)+i]   #esempio della prima iterazione del ciclo "esterno" (utilizzando 1949, 1950, 1951):
            # avg_variation[0] += passengers[12]-passengers[0]
            # avg_variation [0] += passengers[24]-passengers[12]

            #esempio della seconda iterazione del ciclo "esterno" (utilizzando 1949, 1950, 1951):
            # avg_variation[0] += passengers[13]-passengers[1]
            # avg_variation [0] += passengers[25]-passengers[13]

    for i in range (0, 12): #utilizzo questo for per dividere ogni elemento di aus per il "numero di sottrazioni fatte" che corrisponde a diff
        avg_variation[i] /= diff

    return avg_variation

time_series_file = CSVTimeSeriesFile('data.csv')
time_series = time_series_file.get_data()
#for item in time_series:
    #print(item)
avg_variation = compute_avg_monthly_difference(time_series, '1949', '1952')
print('\n')
print(avg_variation)