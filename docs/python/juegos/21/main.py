from deck import Deck
from hand import Hand

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    def play(self):
        player_hand = Hand()
        player_hand.add_card(self.deck.deal())
        print("Tu mano es: ", player_hand.cards,
              "lo que hace un total de: ", player_hand.calculate_value())
        while player_hand.value < 21:
            action = input("Quieres hit o stay? ").lower()
            if action == "hit":
                player_hand.add_card(self.deck.deal())
                print("Tu mano es: ", player_hand.cards,
                      "lo que hace un total de: ", player_hand.calculate_value())
            else:
                print("Tu puntuación final es de",
                      player_hand.calculate_value())
                return
        print("has PERDIDO.")
        print("Tu puntuación final es de",
              player_hand.calculate_value())

if __name__ == '__main__':
    print("hola")
    game = Game()
    game.play()
