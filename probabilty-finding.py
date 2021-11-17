deck = ["aspade", "2spade", "3spade", "4spade", "5spade", "6spade", "7spade", "8spade", "9spade", "0spade", "jspade", "qspade", "kspade", "aheart", "2heart", "3heart", "4heart", "5heart", "6heart", "7heart", "8heart", "9heart", "0heart", "jheart", "qheart", "kheart", "aclubs", "2clubs", "3clubs", "4clubs", "5clubs", "6clubs", "7clubs", "8clubs", "9clubs", "0clubs", "jclubs", "qclubs", "kclubs", "adiamo", "2diamo", "3diamo", "4diamo", "5diamo", "6diamo", "7diamo", "8diamo", "9diamo", "0diamo", "jdiamo", "qdiamo", "kdiamo"]

f = open("possibility.txt", "a")
for a in range(52):
    for b in range(52):
        for c in range(52):
            f.write(f"{deck[a]} {deck[b]} {deck[c]}\n")
