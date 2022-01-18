import random

class Automa():
    def __init__(self):
        self.biancheria = None
        self.calzini = None
        self.maglia = None
        self.pantaloni = None
        self.calzatura = None
    
    def __str__(self):
        return('\nBiancheria: {}\nCalzini: {}\nMaglia: {}\nPantaloni: {}\nCalzatura: {}'.format(self.biancheria, self.calzini, self.maglia, self.pantaloni, self.calzatura))

    def biancheria_up(self):
        try:
            self.biancheria = True
            return 1
        except Exception as e:
            return 0
    
    def calzini_up(self):
        try:
            self.calzini = True
            return 1
        except Exception as e:
            return 0

    def maglia_up(self):
        try:
            self.maglia = True
            return 1
        except Exception as e:
            return 0

    def pantaloni_up(self):
        try:
            self.pantaloni = True
            return 1
        except Exception as e:
            return 0

    def calzatura_up(self):
        try:
            self.calzatura = True
            return 1
        except Exception as e:
            return 0

def esegui(Automa, capo):
    capo = str(capo)
    ris = 0
    if capo == 'biancheria':
        ris = Automa.biancheria_up()
    elif capo == 'calzini':
        ris = Automa.calzini_up()
    elif capo == 'maglia':
        ris = Automa.maglia_up()
    elif capo == 'pantaloni':
        ris = Automa.pantaloni_up()
    else:
        ris = Automa.calzatura_up()
    print('+ Ho indossato '+capo)
    return ris

################## MAIN ##################

aut = Automa()
capi_vestiario = ['biancheria', 'calzini', 'maglia', 'pantaloni', 'calzatura']
vestito = True
res = 0

while(vestito):
    capo = str(random.choice(capi_vestiario))
    try:
        if capo == 'calzatura' and aut.calzatura is None:
            if aut.calzini is None or aut.pantaloni is None:
                print('Indossare '+capo+' ora va contro la procedura')
            else:
                res = esegui(aut, capo)
        elif capo == 'pantaloni' and aut.pantaloni is None:
            if aut.biancheria is None:
                print('Indossare '+capo+' ora va contro la procedura')
            else:
                res = esegui(aut, capo)
        elif capo == 'maglia' and aut.maglia is None:
            if aut.biancheria is None:
                print('Indossare '+capo+' ora va contro la procedura')
            else:
                res = esegui(aut, capo)
        elif capo == 'calzini' and aut.calzini is None:
            res = esegui(aut, capo)
        elif capo == 'biancheria' and aut.biancheria is None:
            res = esegui(aut, capo)
        
        if res == 0:
            raise Exception('Azione di indossare '+capo+' non andata a buon fine')
            #print('Azione di indossare '+capo+' non andata a buon fine')
        elif aut.biancheria is not None and aut.calzini is not None and aut.maglia is not None and aut.pantaloni is not None and aut.calzatura is not None:
            vestito = False
    except Exception as e:
        print('Non sono riuscito ad indossare il capo: '+capo)

print('\nMi sono vestito completamente') """