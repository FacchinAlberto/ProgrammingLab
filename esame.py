class ExamException(Exception):
    pass

class Diff():
    def __init__(self, ratio=1):
        if type(ratio) == int or type(ratio) == float:
            if ratio <= 0:
                raise ExamException('Errore, valore di ratio: {}'.format(ratio))
            else:
                self.ratio = ratio
        else:
            raise ExamException('Errore, tipo: {}, valore: {}'.format(type(ratio), ratio)) 
            
    def type_ok(self, values):
        ok = True
        for item in values:
            if type(item) != int and type(item) != float:
                ok = False
        if ok:
            return True
        else:
            raise ExamException('Errore, valori della lista non computabili')
    
    def is_list(self, values):
        if isinstance(values, list):
            return True
        else:
            raise ExamException('Errore, non è stata fornita in ingresso una lista')

    def lenght_list_ok(self, values):
        if len(values) < 2:
            raise ExamException('Errore, lista vuota')
        else:
            return False

    def compute(self, values):
        if values is None:
            raise ExamException('Errore, valore della lista: None')
        elif self.is_list(values) and self.type_ok(values) and not self.lenght_list_ok(values):
            result = []
            print(self.ratio)
            for i in range (0, len(values)-1):
                result.append((values[i+1] - values[i])/self.ratio)
            return result