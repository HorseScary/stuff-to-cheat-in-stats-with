"""
WAYS TO WIN
ascending order
3 of the same suite 
all face cards
"""
from deckOfCards import getCard
def draw():
    card1 = getCard()
    card2 = getCard()
    card3 = getCard()

    while card1 == card2 or card1 == card3 or card2 == card3:

        print ("This ran")

        if card1 == card2 or card3:
            card1 = getCard()
        
        elif card2 == card3 or card1:
            card2 = getCard()

def winning(card1, card2, card3):
    if card1[1] == 'a' or 'j' or 'k' or 'q' and card2[1] == 'a' or 'j' or 'k' or 'q' and card3[1]=='a' or 'j' or 'k' or 'q' :
        print("3 face cards!")