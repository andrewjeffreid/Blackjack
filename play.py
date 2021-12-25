import random

clubs = '\u2663'
diamonds = '\u2666'
hearts = '\u2665'
spades = '\u2660'

class Card:

    # Card objects have three attributes: suit, rank, and value
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


# setup blackjack_deck with 312 cards
blackjack_deck = Deck()
for i in range(5):
    blackjack_deck.add_deck()

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

# report players hands
def hand_reporter():
    for player in players:
        print(player.name)
        for card in player.hand:   
            print("\t", str(card.rank) + card.suit)
            
# setup players
name = input('Enter your name: ')
user = Player(name)
dealer = Player('Computer')
players = [user, dealer]
print('Hello', name)

# play game
while True:

    # handle user
    if user.money > 0:
        print('You have $' + str(user.money))
        play = input('(P)lay or (C)ash out? ')
        if play == 'P':

            # get new hands
            user.hand = []
            dealer.hand = []
            user.bust = False
            dealer.bust = False
            
            # handle bet
            while True:
                try:
                    bet = float(input('Place a bet: '))
                except:
                    continue
                else:
                    if bet > 0 and bet <= user.money:
                        break
                    elif bet > user.money:
                        print('Insufficient funds')
                        continue
                    elif bet <= 0:
                        print('Bet must be greater than 0')
                        continue
                    else:
                        print('Invalid bet')
                        continue
                
            # deal
            blackjack_deck.shuffle()
            for i in range(2):
                for player in players:
                    card = blackjack_deck.deal()
                    player.hand.append(card)

            # check for blackjack
            dealer.get_value()
            user.get_value()
            if dealer.value == 21:
                user.money -= bet
                print('Dealer has blackjack')
                hand_reporter()
            else:
                if user.value == 21:
                    user.money += (1.5 * bet)
                    print(user.name, 'has blackjack')
                    hand_reporter()

                # user plays
                else:

                    # display hands
                    print('Dealer is showing ' + str(dealer.hand[0].rank) + str(dealer.hand[0].suit))
                    while True:
                        userhand = ''
                        for card in user.hand:
                            userhand += ' ' + str(card.rank) + str(card.suit)
                        print('You have' + userhand)

                        # check if user busts
                        user.get_value()
                        if user.bust == True:
                            user.money -= bet
                            print('You bust')
                            break

                        # hit or stay
                        hit_or_stay = input('(H)it or (S)tand? ')

                        # handle hit
                        if hit_or_stay == 'H':
                            user.hand.append(blackjack_deck.deal())
                            continue

                        # handle stay
                        elif hit_or_stay == 'S':

                            # dealer plays
                            while True:
                                dealerhand = ''
                                for card in dealer.hand:
                                    dealerhand += ' ' + str(card.rank) + str(card.suit)
                                print('Dealer has' + dealerhand)
                                dealer.get_value()

                                # dealer hits until 17
                                if dealer.value < 17:
                                    print('Dealer hits')
                                    dealer.hand.append(blackjack_deck.deal())
                                    continue

                                # check if dealer busts
                                else:
                                    if dealer.bust == True:
                                        user.money += bet
                                        print('Dealer busts')
                                        break

                                    # determine winner
                                    else:
                                        if dealer.value > user.value:
                                            user.money -= bet
                                            print('Dealer wins')
                                        elif dealer.value < user.value:
                                            user.money += bet
                                            print('You win')
                                        elif dealer.value == user.value:
                                            print('Push')
                                break
                            break
                        
        # cash out
        elif play == 'C':
            break
        else:
            continue
        
    # user broke
    else:
        print('Not enough money to play | Balance: $' + str(user.money))
        break
