def thing(prob, trial):
    trial -= 1
    otherProb = 1-prob

    return((prob * otherProb) ** trial)

for i in range(6):
    print(thing(.2, i+1))
