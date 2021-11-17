import random

def cleanUp(dirty):
    number = dirty[0]
    suite = dirty[1]
    
    if suite == "s":
        suite = "Spades"
    elif suite == "h":
        suite = "Hearts"
    elif suite == "d":
        suite = "Diamonds"
    elif suite == "c":
        suite = "Clubs"
    else:
        return(f"something weird happed! The suite was '{suite}'")

    if number == "0":
        number = "10"
    elif number == "j":
        number = "Jack"
    elif number == "q":
        number = "Queen"
    elif number == "k":
        number = "King"
    elif number == "a":
        number = "Ace"
    
    return(f"{number} of {suite}") 


def deviouslyDirtyDecks():
    deck = ["aspade", "2spade", "3spade", "4spade", "5spade", "6spade", "7spade", "8spade", "9spade", "0spade", "jspade", "qspade", "kspade", "aheart", "2heart", "3heart", "4heart", "5heart", "6heart", "7heart", "8heart", "9heart", "0heart", "jheart", "qheart", "kheart", "aclubs", "2clubs", "3clubs", "4clubs", "5clubs", "6clubs", "7clubs", "8clubs", "9clubs", "0clubs", "jclubs", "qclubs", "kclubs", "adiamo", "2diamo", "3diamo", "4diamo", "5diamo", "6diamo", "7diamo", "8diamo", "9diamo", "0diamo", "jdiamo", "qdiamo", "kdiamo"]

    card1 = deck[random.randint(0,51)]
    card2 = deck[random.randint(0,51)]
    card3 = deck[random.randint(0,51)]

    cards = f"Your cards were {cleanUp(card1)}, {cleanUp(card2)}, and {cleanUp(card3)}\n"

    if card1[0] == card2[0] and card3[0] and card1[1] == card2[1] and card3[0]: #3 of the same card
        return(f"{cards}[SAME CARDx3]\nYou won $100!")
    
    elif card1[0] == card2[0] and card1[1] == card2[1] or card1[0] == card3[0] and card1[1] == card3[1] or card2[0] == card3[0] and card2[1] == card3[1]: #2 0f the same card
        return(f"{cards}[SAME CARDx2]\nYou won $30!")
    
    elif card1[0] == card2[0] and card3[0]: #3 of the same number
        return(f"{cards}[SAME NUMBERx3]\nYou won $25!")
    
    elif card1[1] == card2[1] and card3[1]: #3 of the same suite
        return(f"{cards}[SAME SUITEx3]\nYou won $15!")

    elif card1[0] == card2[0] or card1[0] == card3[0] or card2[0] == card3[0]: #2 of the same number
        return(f"{cards}[SAME NUMBERx2]\nYou won $10!")
    
    elif card1[1] == card2[1] or card1[1] == card3[1] or card2[1] == card3[1]:
        return(f"{cards}[SAME SUITEx2]\nYoy won $5!")

    else:
        return(f"{cards}[NOTHING]\nYou won nothing :(")

print(deviouslyDirtyDecks())