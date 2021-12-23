import random


class Card:

    # Card objects have two attributes: suit and rank
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

class Deck:

    # Deck objects have one attribute: cards (list)
    def __init__(self):
        self.cards = []
        # Deck objects are instiated with one standard deck
        self.add_deck()

    # Add one standard deck to self.cards
    def add_deck(self):
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        for suit in suits:
            for rank in ranks:
                card = Card(rank = rank, suit = suit)
                self.cards.append(card)

    # Randomize item order in self.cards
    def shuffle(self):
        return random.shuffle(self.cards)

    # Remove and return an item in self.cards
    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop()

class Hand():
    # Hand objects has one attribute,an empty list
    def __init__(self):
        self.cards = []
