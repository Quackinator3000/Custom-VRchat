import math
import random
#This version is in a pre - pre - alpha stage. just trying to get a printable card deck and avoid repititions
#TEST VERSION 0.0.1
i = 0
j = 0
k = 0

class Card: # Creates a set of values to generate a card from
    value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suit = ["spades", "clubs", "hearts", "diamonds"]

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f'{self.value} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in Card.suit for value in Card.value]
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

    def __repr__(self):
        return f'Deck of {len(self.cards)} cards'    


while True:

    # Example usage:
    deck = Deck()
    print(deck)  # Output: Deck of 52 cards

    # Draw a card:
    drawn_card = deck.draw_card()
    print(drawn_card)  # Output example: 7 of Clubs
    print(deck)  