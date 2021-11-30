class Automobile():
    def __init__(self, casa_automo, modello, numero_posti, targa):
        self.casa_automo = casa_automo
        self.modello = modello
        self.numero_posti = numero_posti
        self.targa = targa

    def __str__(self):
        print('Casa automobilistica: {}\nModello: {}\nNumero posti: {}\nTarga: {}'.format(self.casa_automo, self.modello, self.numero_posti, self.targa))

    def parla(self):
        print('\nBroom Broom')
    
    def confronta(self, casa_automo, modello, numero_posti):
        if self.casa_automo == casa_automo and self.modello == modello and self.numero_posti == numero_posti:
            return True
        else:
            return False

class Transformer(Automobile):
    def __init__(self, casa_automo, modello, numero_posti, targa, nome, generazione, grado, reparto):
        super().__init__(casa_automo, modello, numero_posti, targa)
        self.nome = nome
        self.generazione = generazione
        self.grado = grado
        self.reparto = reparto
    def scheda_militare(self):
        print('\nNome: {}\nGrado: {}\nReparto: {}'.format(self.nome, self.grado, self.reparto))

auto = Automobile('Fiat', 'Panda', 5, 'HR544HT')
auto.parla()
if auto.confronta('Fiat', 'Panda', 5) == True:
    print('\nLe due auto sono uguali')
else:
    print('\nLe due auto sono diverse')
transformer = Transformer('Volkswagen', 'Maggiolino', 2, 'no targa', 'Bumblebee', 1, 'sergente', 'corpo a corpo')
transformer.parla()
transformer.scheda_militare()