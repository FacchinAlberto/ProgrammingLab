from matplotlib import pyplot

class CSVFile():
    def __init__(self, name, file):
        self.name = name
        self.file = file

    def write(self, line):
        my_file = open(self.file, 'a')
        my_file.write('\n'+line)
        my_file.close()

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

class Model():
    def fit(self, data):
        raise NotImplementedError("Metodo non implementato")
    def predict(self, data):
        raise NotImplementedError("Metodo non implementato")        

class IncrementModel(Model):
    def check_data(self, data):
        if len(data)<2:
            return 'Impossibile fare previsione, numero di dati insufficienti'
        else:
            return True
    #def preditct(self, data):  
    def __str__(self):
        return 'IncrementModel'

    def compute_avg_increment(self, data):
        if self.check_data(data):
            inc = 0.0
            for i in range(0, len(data)-1):
                inc += float(data[i+1]) - float(data[i])    
            avg_increment = inc/len(data)
            return avg_increment
        else:
            print(self.check_data(data))
    
    def predict(self, predict_data):
        avg_increment = self.compute_avg_increment(predict_data)
        return float(predict_data[-1]) + avg_increment

class FitIncrementModel(IncrementModel):
    def __str__(self):
        return 'FitIncrementModel'

    def fit(self, fit_data):
        # Calcolo l'incremento medio sui dati di fit
        self.global_avg_increment = self.compute_avg_increment(fit_data)

    def predict(self, predict_data):
        # Chiamo la predict della classe genitore "IncrementModel"
        parent_prediction = super().predict(predict_data)
        # Sottraggo l'ultimo valore alla predizione del genitore
        # cosi' da avre l'incremento "originale"
        parent_predict_increment = parent_prediction - float(predict_data[-1])
        # Ora medio l'incremento del fit con quello della predict
        prediction_increment = (self.global_avg_increment + parent_predict_increment) / 2
        # E lo ri-sommo all'ultimo elemento
        prediction = float(predict_data[-1]) + prediction_increment
        return prediction
        
## MAIN ##
csvobj = CSVFile('Vendite shampoo', 'shampoo_sales.csv')
my_list = csvobj.get_data()
data = []
for item in my_list:
    data.append(item[1])

"""
fitobj = FitIncrementModel()
fitobj.fit(data)


#numero di mesi di cui voglio predire i valori
number_of_months = 12

for i in range(1, number_of_months+1):
    prediction = fitobj.predict(data)
    print(prediction)
    data.append(prediction)
    csvobj.write('prediction '+str(i)+','+str(round(data[len(values)-1], 2)))
"""

number_of_months = 12
cutoff_month = len(data) - number_of_months

real_data = []
test_data = []

for i in range(len(data)):
    if i < cutoff_month:
        test_data.append(data[i])
    else:
        real_data.append(data[i])

incobj = IncrementModel()
fitobj = FitIncrementModel()
fitobj.fit(test_data)
predictions = []
fit_predictions = []
fit_error = 0
error = 0

for i in range(number_of_months):
    predict_data = data[cutoff_month+i-3-1:cutoff_month+i-1]
    prediction = incobj.predict(predict_data)
    predictions.append(prediction)
    prediction_fit = fitobj.predict(predict_data)
    fit_predictions.append(prediction_fit)
    print('"{}" (real) vs "{}" (fit pred) vs "{}" (pred)\n'.format(real_data[i], round(prediction_fit, 1), round(prediction,1 )))
    fit_error += abs(prediction_fit - float(real_data[i]))
    error += abs(prediction - float(real_data[i]))

fit_error /= number_of_months
error /= number_of_months
print('Fit error: {}\nNon fit error: {}'.format(fit_error, error))

pyplot.plot(test_data + predictions, color='tab:red')
pyplot.plot(test_data + fit_predictions, color='tab:green')
pyplot.plot(data, color='tab:blue')
pyplot.show()