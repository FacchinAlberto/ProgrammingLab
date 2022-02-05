class ExamException(Exception):
    pass

class MovingAverage():
    def __init__(self, finestra):
        if type(finestra) == int and finestra >= 1:
            self.finestra = finestra 
        elif finestra is None:
            raise ExamException('Errore, valore della finestra incompatibile')
        else:
            raise ExamException('Errore, tipo: {}, valore: {}'.format(type(finestra), finestra))

    def type_ok(self, values):
        ok = True
        if isinstance(values, list):
            for item in values:
                if type(item) != int and type(item) != float:
                    ok = False
        else:
            ok = False
        return ok

    def empty_list(self, values):
        if len(values) < 1:
            return True
        else:
            return False

    def finestra_ok(self, lenght):
        ok = True
        if self.finestra > lenght:
            ok = False
        return ok

    def compute(self, values):
        if values is None:
            raise ExamException('Errore, valore della lista: None')
        elif self.type_ok(values) and not self.empty_list(values):
            if self.finestra_ok(len(values)):
                result = []
                somma = 0
                media = 0
                for i in range (0, len(values)-self.finestra+1):
                    for j in range(i, i+self.finestra):
                        somma += values[j]
                    media = somma/self.finestra
                    result.append(media)
                    somma = 0
                return result
            else:
                raise ExamException('Errore, valore della finestra incompatibile')
        elif not self.type_ok(values):
            raise ExamException('Errore, valori della lista non computabili')
        else:
            raise ExamException('Errore, lista vuota')

"""
obj = MovingAverage(1)
values = [2, 4, 8, 16]
result = obj.compute(1)
print(result)"""