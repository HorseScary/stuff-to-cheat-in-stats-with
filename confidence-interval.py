import math
from re import I

def proportion(end1, end2):
    a = (end2 - end1)/2

    b = end1 + a

    return (a, b)

def interval(n, x):
    pHat = x/n
    qHat = 1 - pHat
    
    conf90 = 1.65
    conf95 = 1.96
    conf98 = 2.0537489
    conf99 = 2.575
    def lastthing(conf):
        thing = (pHat * qHat) / n
        thing = math.sqrt(thing) * conf

        return(pHat - thing, pHat + thing)

    return(f"90:{lastthing(conf90)}\n95:{lastthing(conf95)}\n98:{lastthing(conf98)}\n99:{lastthing(conf99)}")

print(interval(1029,494))