import deck as deck

# create poker_deck object with 52 cards
poker_deck = deck.Deck()

# create blackjack_deck with 312 cards
blackjack_deck = deck.Deck()
for i in range(5):
    blackjack_deck.add_deck()


# create Player class with constructor containing name and hand
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []


# function to setup blackjack game
def blackjack(*player):
    
    # allow us to access players variable outside of the function
    global players
    
    # create list of players as objects
    players = [Player(p) for p in player]
    
    # shuffle blackjack deck (312 cards)
    blackjack_deck.shuffle()

    # deal 2 cards to each player using the deal method from deck_OOP
    for i in range(2):
        for player in players:
            card = blackjack_deck.deal()
            player.hand.append(card)
    return players


# function to setup poker game            
def poker(*player):

    # allow us to access players variable outside of the function
    global players

    # create list of players as objects
    players = [Player(p) for p in player]

    # shuffle poker deck (52 cards)
    poker_deck.shuffle()

    # deal 5 cards to each player using the deal method from deck_OOP
    for i in range(5):
        for player in players:
            card = poker_deck.deal()
            player.hand.append(card)
    return players


# function to report the hands of a player formatted with tabs
def hand_reporter(player):
    print(player.name + "'s hand:")
    for card in player.hand:   
        print("\t", card.rank, "of", card.suit)


# prompt user for 3 player names and game
player1 = input("Enter Player 1 name: ")
player2 = input("Enter Player 2 name: ")
player3 = input("Enter Player 3 name: ")
game_type = input("(B)lackjack or (P)oker? ")


# if user chose blackjack, call blackjack function and report hands of players
if game_type == "B":
    blackjack(player1, player2, player3)
    for player in players:
        hand_reporter(player)

# if user chose poker, call poker function and report hands of players
if game_type == "P":
    poker(player1, player2, player3)
    for player in players:
        hand_reporter(player)
