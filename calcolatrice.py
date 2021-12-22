import math

class Calcolatrice():
    def __init__(self):
        pass

    def type_ok(self, a):
        if type(a) == int or type(a) == float:
            return True
        else:
            return False

    def somma(self, a, b):
        try:
            if self.type_ok(a) and self.type_ok(b):
                return a + b
            else:
                raise TypeError('\nErrore di tipo')
        except Exception as e:
            print('\nImpossibile calcolare {} + {}'.format(a, b))

    def sottrazione(self, a, b):
        try:
            if self.type_ok(a) and self.type_ok(b):
                return a - b
            else:
                raise TypeError('\nErrore di tipo')
        except Exception as e:
            print('\nImpossibile calcolare {} - {}'.format(a, b))

    def prodotto(self, a, b):
        try:
            if self.type_ok(a) and self.type_ok(b):
                return a * b
            else:
                raise TypeError('\nErrore di tipo')
        except Exception as e:
            print('\nImpossibile calcolare {} * {}'.format(a, b))

    def divisione(self, a, b):
        try:
            if self.type_ok(a) and self.type_ok(b):
                if b != 0:
                    return a / b
                else:
                    raise ZeroDivisionError('\nImpossibile dividere per 0')
            else:
                raise TypeError('\nErrore di tipo')
        except Exception as e:
            print('\nImpossibile calcolare {} / {}'.format(a, b))  

    def potenza(self, a, b):
        try:
            if self.type_ok(a) and self.type_ok(b):
                return a ** b
            else:
                raise TypeError('\nErrore di tipo')
        except Exception as e:
            print('\nImpossibile calcolare {} ** {}'.format(a, b))

    def modulo(self, a, b):
        try:
            if self.type_ok(a) and self.type_ok(b):
                return a % b
            else:
                raise TypeError('\nErrore di tipo')
        except Exception as e:
            print('\nImpossibile calcolare {} % {}'.format(a, b))

    def radice(self, a):
        try:
            if self.type_ok(a):
                if a >= 0:
                    return math.sqrt(a)
                else:
                    raise ValueError('\nImpossibile calcolare radice di un numero negativo')
            else:
                raise TypeError('\nErrore di tipo')
        except Exception as e:
            print('\nImpossibile calcolare sqrt({})'.format(a))  

    def cambio_base(self, a):
        try:
            if self.type_ok(a):
                b = str(bin(a))
                elem = b.split('b')
                return elem[1]
            else:
                raise TypeError('\nErrore di tipo')
        except Exception as e:
            print('\nImpossibile convertire {} in base 2'.format(a))  
    
calc = Calcolatrice()
print('\nSomma: '+str(calc.somma(-3, 1.0)))
print('\nSottrazione: '+str(calc.sottrazione(-3, 0.58)))
print('\nProdotto: '+str(calc.prodotto(5, 0.9)))
print('\nDivisione: '+str(calc.divisione(0, 0.1)))
print('\nPotenza: '+str(calc.potenza(0, 1)))
print('\nModulo: '+str(calc.modulo(3, 2)))
print('\nRadice: '+str(calc.radice(2)))
print('\nCambio base: '+str(calc.cambio_base(8)))