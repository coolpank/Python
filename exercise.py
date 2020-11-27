from random import shuffle

class Card:
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return f"{self.count()} cards"

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
# c = Card("Heart", 'A')
d = Deck()
print(d.cards)
print(d)
d.shuffle()
print(d.cards)
d.shuffle()
print(d.cards)
