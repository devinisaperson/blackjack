import random
import time

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def print_card(self):
        if self.suit == "C":
            suitName = "Clubs"
        elif self.suit == "D":
            suitName = "Diamonds"
        elif self.suit == "H":
            suitName = "Hearts"
        elif self.suit == "S":
            suitName = "Spades"
        
        if type(self.value) is int:
            valueName = str(self.value)
        elif self.value == "J":
            valueName = "Jack"
        elif self.value == "Q":
            valueName = "Queen"
        elif self.value == "K":
            valueName = "King"
        elif self.value == "A":
            valueName = "Ace"

        print(valueName + " of " + suitName)
    
    def evaluate_hand(hand):
        aces = 0
        total = 0
        for card in hand:
            if type(card.value) is int:
                total += card.value
            elif card.value == "J":
                total += 11
            elif card.value == "Q":
                total += 12
            elif card.value == "K":
                total += 13
            elif card.value == "A":
                total += 11
                aces += 1
        
        while total > 21 and aces > 0:
            aces -= 1
            total -= 10
        
        return total

deck = []
for suit in ["C", "D", "H", "S"]:
    for value in range(2,11):
        deck.append(Card(suit, value))
    
    for value in ["J", "Q", "K", "A"]:
        deck.append(Card(suit, value))

# dealer blackjack seed: 1738291217
# player blackjack seed: 1738294687
# 20 against 21 seed: 1738294687
# double blackjack seed: 1738380865
seed = int(time.time())
print()
print("-----")
print("SEED: " + str(seed))
print("-----")
print()
random.seed(seed)

random.shuffle(deck)

dealer_hand = []
dealer_in = True
player_hand = []
player_in = True
message = ""

def print_hands(hidden_cards):
    print("dealer's hand: ")
    for card in dealer_hand:
        if hidden_cards > 0:
            hidden_cards -= 1
            print("HIDDEN CARD")
        else:
            card.print_card()
    print()
    
    print("your hand: ")
    for card in player_hand:
        card.print_card()
    print()

while dealer_in or player_in:
    if dealer_in:
        dealer_in = Card.evaluate_hand(dealer_hand) < 17

        dealer_winning = Card.evaluate_hand(dealer_hand) > Card.evaluate_hand(player_hand)
        if (not player_in) and dealer_winning:
            dealer_in = False
    
    if dealer_in:
        # pop(0) removes the first item from the list
        # append adds the item to the other list
        dealer_hand.append(deck.pop(0))
        if (Card.evaluate_hand(dealer_hand) > 21):
            message = "The dealer busted! - You win!"
            break

    if player_in:
        print_hands(1)
        action = input("hit or stand? ")
        print()
        player_in = action == "hit"
    
    if player_in:
        player_hand.append(deck.pop(0))
        if (Card.evaluate_hand(player_hand) > 21):
            message = "You busted! - You lose!"
            break
    

if message == "":
    if (Card.evaluate_hand(player_hand) > 
            Card.evaluate_hand(dealer_hand)):
        message = "You win!"
    elif (Card.evaluate_hand(player_hand) < 
            Card.evaluate_hand(dealer_hand)):
        message = "You lose!"
    else:
        message = "Tie!"

print_hands(0)
print(message)

while (True):
    pass