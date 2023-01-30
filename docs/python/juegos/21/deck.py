import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["♥", "♦", "♣", "♠"]
        ranks = ["As", "2", "3", "4", "5", "6", "7",
                 "8", "9", "10", "Jota", "Reina", "Rey"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def deal(self):
        return self.cards.pop()
