class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.rank in ["Jota", "Reina", "Rey"]:
                self.value += 10
            elif card.rank == "As":
                has_ace = True
                self.value += 11
            else:
                self.value += int(card.rank)

        return self.value
