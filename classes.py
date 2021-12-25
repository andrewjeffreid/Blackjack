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

# create Player class with constructor containing name, hand, bust, and value
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.money = 500
        self.bust = False
        self.value = 0

    #check if ace in hand
    def get_value(self):
        has_ace = False
        for card in self.hand:
            if card.rank == 'A':
                has_ace = True
                
         # handle ace        
        if has_ace == True:
            self.value = 0

            # ace as 11
            for card in self.hand:
                if card.rank == 'A':
                    self.value += card.value[1]
                else:
                    self.value += card.value

            # ace as 1
            if self.value > 21:
                self.value = 0
                for card in self.hand:
                    if card.rank == 'A':
                        self.value += card.value[0]
                    else:
                        self.value += card.value
                        
        # no ace in hand  
        else:
            self.value = 0
            for card in self.hand:
                self.value += card.value

        # check if bust
        if self.value > 21:
            self.bust = True

