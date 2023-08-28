import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
class Deck:
    def __init__(self):
        self.rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.suit = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
        self.reset()

    def reset(self):
        self.deck = [Card(rank, suit) for suit in self.suit for rank in self.rank]
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        if len(self.deck) == 0:
            return None
        return self.deck.pop()
    
    def count(self):
        return len(self.deck)
    
print("Card Dealer")
print()
print("There is a deck of 52 Cards.")
print()

deck = Deck()

deck.shuffle()

cardsDealt = int(input("How many cards would you like?:     "))
dealtCards = []

for i in range(cardsDealt):
    card = deck.deal()
    if card is not None:
        dealtCards.append(f"{card.rank} of {card.suit}")
    else:
        print("No more cards in the deck")
if dealtCards:
    print("Dealt Cards:")
    for card in dealtCards:
        print(card)
        
remaining_count = deck.count()
print(f'There are {remaining_count} cards left in the deck')

print("Good Luck!")
    