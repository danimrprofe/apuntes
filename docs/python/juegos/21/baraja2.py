import random
from carta import Carta

class Baraja:
    def __init__(self):
        self.cartas = []

        valores = ["As","2","3","4","5","6","7","8","9","10","jota","reina","rey"]
        palos = ["picas","corazones","tréboles","diamantes"]

        for palo in palos:
            for valor in valores:
                cartanueva = Carta(palo, valor)
                self.cartas.append(cartanueva)
    def mezclar(self):
        random.shuffle(self.cartas)

    def contar(self):
        return len(self.cartas)


mibaraja = Baraja()
'''
print(mibaraja.cartas)
mibaraja.mezclar()
print(mibaraja.cartas)
'''
numero_cartas = mibaraja.contar()
print(numero_cartas)
