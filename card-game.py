"""
WAYS TO WIN
acending order
3 of the same suite 
all face cards
"""

from deckOfCards import getCard

card1 = getCard()
card2 = getCard()
card3 = getCard()

while card1 == card2 or card1 == card3 or card2 == card3:

    if card1 == card2 or card3:
        card1 == getCard()
    
    elif card2 == card3 or card1:
        card2 == getCard()
    else:
        print("Why are we here?")
    print ("owo")

if card1[1] == 'a' or 'j' or'k' or 'q':
    print("Face card!")

print ('a')