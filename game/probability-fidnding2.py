f = open("/home/violetayers/repos/stuff-to-cheat-in-stats-with/game/penis.txt", 'r')

lines = f.readlines()

Counter = 0
sameCardx3 = 0
sameCardx2 = 0
sameNumx3 = 0
sameSuitex3 = 0
sameNumx2 = 0
sameSutex2 = 0
nothing = 0

for line in lines:
#   if card1[0] == card2[0] and card3[0] and card1[1] == card2[1] and card3[0]: #3 of the same card
    if line[0] == line[7] and line[14] and line[1] == line[8] and line[14]: #3 of the same card
        sameCardx3 += 1
    elif line[0] == line[7] and line[1] == line[8] or line[0] == line[14] and line[1] == line[15] or line[7] == line[14] and line[8] == line[15]: #2 0f the same card
        sameCardx2 += 1
    elif line[0] == line[7] and line[14]: #3 of the same number
        sameNumx3 += 1
    elif line[1] == line[8] and line[15]: #3 of the same suite
        sameSutex2 += 1
    elif line[0] == line[7] or line[0] == line[14] or line[7] == line[14]: #2 of the same number
        sameNumx2 += 1
    elif line[1] == line[8] or line[1] == line[15] or line[8] == line[15]:
        sameSutex2 += 1
    else:
        Counter += 1

print(f"3 same: {sameCardx3}\n2 same: {sameCardx2}\nsame num 3: {sameNumx3}\nsame num 2: {sameNumx2}\nsame suite 3: {sameSuitex3}\nsame suite 2: {sameSutex2}\nnothing: {Counter}")



"""
0, 7, 14
card1[0] = line[0]
card2[0] = line[7]
card3[0] = line[14]

card1[1] = line[1]
card2[1] = line[8]
card3[1] = line[15]
"""

# sp
# di
# cl
# he