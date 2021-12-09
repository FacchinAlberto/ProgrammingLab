class Model():
    def fit(self, data):
        raise NotImplementedError("Metodo non implementato")
    def predict(self, data):
        raise NotImplementedError("Metodo non implementato")
    def check_data(self, data):
        if len(data)<2:
            return 'Impossibile fare previsione, numero di dati insufficienti'
        else:
            return true
        

class IncrementedModel(Model):
    def preditct(self, data):
        if check_data:
            inc = 0
            for i in range(0, len(data)-1):
                inc += data[i+1] - data[i]
            prediction = inc/len(data)
            return prediction
        else:
            print(check_data)