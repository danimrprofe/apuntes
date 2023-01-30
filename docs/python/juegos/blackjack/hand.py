class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.rank in ["Jack", "Queen", "King"]:
                self.value += 10
            elif card.rank == "Ace":
                has_ace = True
                self.value += 11
            else:
                self.value += int(card.rank)
        if has_ace and self.value > 21:
            self.value -= 10
        return self.value
