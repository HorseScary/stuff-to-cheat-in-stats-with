import random
net = 0
for i in range(1000):
    a = random.randint(1, 4)
    if a == 1:
        net += 9
    else:
        net += -2
    print (f"Roll: {a}\nNet gain: {net}")