import random

clubs = '\u2663'
diamonds = '\u2666'
hearts = '\u2665'
spades = '\u2660'


class Card:

    # Card objects have two attributes: suit and rank
    def __init__(self, rank, suit, value):
        self.suit = suit
        self.rank = rank
        self.value = value

class Deck:

    # Deck objects have one attribute: cards (list)
    def __init__(self):
        self.cards = []
        # Deck objects are instiated with one standard deck
        self.add_deck()

    # Add one standard deck to self.cards
    def add_deck(self):
        suits = [clubs, diamonds, hearts, spades]
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        values = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10, 'A':[1,11]}
        for suit in suits:
            for rank in ranks:
                card = Card(rank = rank, suit = suit, value = values[rank])
                self.cards.append(card)

    # Randomize item order in self.cards
    def shuffle(self):
        return random.shuffle(self.cards)

    # Remove and return an item in self.cards
    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop()

#class Hand():
    # Hand objects has one attribute,an empty list
    #def __init__(self):
        #self.cards = []
