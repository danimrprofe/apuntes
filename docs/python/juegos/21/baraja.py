import random
from carta import Carta

class Baraja:
    def __init__(self):
        self.cartas = []
        palos = ["♥", "♦", "♣", "♠"]
        valores = ["As", "2", "3", "4", "5", "6", "7",
                   "8", "9", "10", "Jota", "Reina", "Rey"]
        for palo in palos:
            for valor in valores:
                self.cartas.append(Carta(palo, valor))

    def barajar(self):
        random.shuffle(self.cartas)

    def __repr__(self):
        return f"Baraja de {self.contar()} cartas"

    def contar(self):
        return len(self.cartas)

    def repartir(self):
        return self.cartas.pop()
