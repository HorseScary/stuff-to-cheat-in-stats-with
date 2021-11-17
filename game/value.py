sameCardx3 = 95
sameCardx2 = 20
sameNumx3 = 15
sameSuitex3 = 10
sameNumx2 = 5
sameSutex2 = 0
nothing = -10

thing = 140608
value = ((sameCardx3*(52/thing)) + (sameCardx2*(8008/thing)) + (sameNumx3*(832/thing)) + (sameNumx2*(30784/thing)) + (sameSuitex3*(8788/thing)) + (sameSutex2*(87880/thing)) + nothing*(41184/140608))

print(value)
