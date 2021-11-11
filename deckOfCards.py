import random

deck = ["aspade", "2spade", "3three", "4spade", "5spade", "6spade", "7spade", "8spade", "9spade", "0spade", "jspade", "qspade", "kspade", "aheart", "2heart", "3three", "4heart", "5heart", "6heart", "7heart", "8heart", "9heart", "0heart", "jheart", "qheart", "kheart", "aclubs", "2clubs", "3three", "4clubs", "5clubs", "6clubs", "7clubs", "8clubs", "9clubs", "0clubs", "jclubs", "qclubs", "kclubs", "adiamo", "2diamo", "3three", "4diamo", "5diamo", "6diamo", "7diamo", "8diamo", "9diamo", "0diamo", "jdiamo", "qdiamo", "kdiamo"]

def getCard():
    deck = ["aspade", "2spade", "3spade", "4spade", "5spade", "6spade", "7spade", "8spade", "9spade", "0spade", "jspade", "qspade", "kspade", "aheart", "2heart", "3heart", "4heart", "5heart", "6heart", "7heart", "8heart", "9heart", "0heart", "jheart", "qheart", "kheart", "aclubs", "2clubs", "3clubs", "4clubs", "5clubs", "6clubs", "7clubs", "8clubs", "9clubs", "0clubs", "jclubs", "qclubs", "kclubs", "adiamo", "2diamo", "3diamo", "4diamo", "5diamo", "6diamo", "7diamo", "8diamo", "9diamo", "0diamo", "jdiamo", "qdiamo", "kdiamo"]
    return(deck[random.randint(0,51)])

def getCardClean():
    dirty = getCard()
    number = dirty[0]
    suite = dirty[1] + dirty[2] + dirty[3] + dirty[4] + dirty[5]
    
    if suite == 'spade':
        suite = 'Spades'
    elif suite == 'heart':
        suite == 'Hearts'
    elif suite == 'diamo':
        suite = 'Diamonds'
    elif suite == 'clubs':
        suite == 'Clubs'
    else:
        return(f'something weird happed! The suite was "{suite}"')

    if number == '0':
        number = '10'
    elif number == 'j':
        number = 'Jack'
    elif number == 'q':
        number = 'Queen'
    elif number == 'k':
        number = 'King'
    else:
        return(f'something weird happed! The number was "{suite}"')
    


    return(f"You drew a {number} of {suite}!") 

