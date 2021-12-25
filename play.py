import deck as deck

# setup blackjack_deck with 312 cards
blackjack_deck = deck.Deck()
for i in range(5):
    blackjack_deck.add_deck()

# create Player class with constructor containing name and hand
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.bust = False
        self.value = 0

    def get_value(self):
        has_ace = False
        for card in self.hand:
            if card.rank == 'A':
                has_ace = True
                
        # handle ace        
        if has_ace == True:
            self.value = 0
            for card in self.hand:
                if card.rank == 'A':
                    self.value += card.value[1]
                else:
                    self.value += card.value
                    
            if self.value > 21:
                self.value = 0
                for card in self.hand:
                    if card.rank == 'A':
                        self.value += card.value[0]
                    else:
                        self.value += card.value
                    
        else:
            self.value = 0
            for card in self.hand:
                self.value += card.value
        if self.value > 21:
            self.bust = True
            
# setup game and deal
blackjack_deck.shuffle()
user = Player('Andrew')
dealer = Player('Computer')
players = [user, dealer]
for i in range(2):
    for player in players:
        card = blackjack_deck.deal()
        player.hand.append(card)

# function to report the hands of a player formatted with tabs
def hand_reporter():
    for player in players:
        print(player.name)
        for card in player.hand:   
            print("\t", str(card.rank) + card.suit)

dealer.get_value()
user.get_value()
if dealer.value == 21:
    print('dealer has blackjack')
    hand_reporter()
else:
    if user.value == 21:
        print(user.name, 'has blackjack')
        hand_reporter()
    else:
        print('dealer is showing ' + str(dealer.hand[0].rank) + str(dealer.hand[0].suit))
        while True:
            
            # display hands  
            userhand = ''
            for card in user.hand:
                userhand += ' ' + str(card.rank) + str(card.suit)
            print('You have' + userhand)

            # check if user busts
            user.get_value()
            if user.bust == True:
                print('you bust')
                break

            # hit or stay
            hit_or_stay = input('(H)it or (S)tand? ')

            # handle hit
            if hit_or_stay == 'H':
                user.hand.append(blackjack_deck.deal())
                continue

            # handle stay
            elif hit_or_stay == 'S':
                while True:
                    dealerhand = ''
                    for card in dealer.hand:
                        dealerhand += ' ' + str(card.rank) + str(card.suit)
                    print('dealer has' + dealerhand)
                    dealer.get_value()

                    if dealer.value < 17:
                        print('dealer hits')
                        dealer.hand.append(blackjack_deck.deal())
                        continue
                    
                    else:
                        if dealer.bust == True:
                            print('dealer busts')
                            break
                        else:
                            if dealer.value > user.value:
                                print('dealer wins')
                            elif dealer.value < user.value:
                                print('player wins')
                            elif dealer.value == user.value:
                                print('push')
                    break
                break
