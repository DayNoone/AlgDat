from sys import stdin

class Kubbe:
    vekt = None
    neste = None
    def __init__(self, vekt):
        self.vekt = vekt 
        self.neste = None

def spor(kubbe):
    storste = kubbe.vekt
    while kubbe.neste != None:
        if storste < kubbe.neste.vekt:
            storste = kubbe.neste.vekt
        kubbe = kubbe.neste
    print storste
    

# Oppretter lenket liste
forste = None
siste = None
for linje in stdin:
    forrige_siste = siste
    siste = Kubbe(int(linje))
    if forste == None:
        forste = siste
    else:
        forrige_siste.neste = siste

# Kaller loesningsfunksjonen og skriver ut resultatet
spor(forste)
