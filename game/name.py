import random
describe = ["attractive", "bald", "beautiful", "chubby", "clean", "dazzling", "drab", "elegant", "fancy", "fit", "flabby", "glamorous", "gorgeous", "handsome", "long", "magnificent", "muscular", "plain", "plump", "quaint", "scruffy", "shapely", "short", "skinny", "stocky", "ugly", "unkempt", "unsightly", "ashy", "black", "blue", "gray", "green", "icy", "lemon", "mango", "orange", "purple", "red", "salmon", "white", "yellow", "alive", "better", "careful", "clever", "dead", "easy", "famous", "gifted", "hallowed", "helpful", "important", "inexpensive", "mealy", "mushy", "odd", "poor", "powerful", "rich", "shy", "tender", "unimportant", "uninterested", "wrong", "vast", "aggressive", "agreeable", "ambitious", "brave", "calm", "delightful", "eager", "faithful", "gentle", "happy", "jolly", "kind", "lively", "nice", "obedient", "polite", "proud", "silly", "thankful", "victorious", "witty", "wonderful", "zealous", "aggressive", "agreeable", "ambitious", "brave", "calm", "delightful", "eager", "faithful", "gentle", "happy", "jolly", "kind", "lively", "nice", "obedient", "polite", "proud", "silly", "thankful", "victorious", "witty", "wonderful", "zealous", "angry", "bewildered", "clumsy", "defeated", "embarrassed", "fierce", "grumpy", "helpless", "itchy", "jealous", "lazy", "mysterious", "nervous", "obnoxious", "panicky", "pitiful", "repulsive", "scary", "thoughtless", "uptight", "worried", "abundant", "billions", "enough", "few", "full", "hundreds", "incalculable", "limited", "little", "many", "most", "millions", "numerous", "scarce", "some", "sparse", "substantial", "thousands", "breezy", "bumpy", "chilly", "cold", "cool", "cuddly", "damaged", "damp", "dirty", "dry", "flaky", "fluffy", "freezing", "greasy", "hot", "icy", "loose", "melted", "prickly", "rough", "shaggy", "sharp", "slimy", "sticky", "strong", "tight", "uneven", "warm", "weak", "wet", "wooden"  , "ancient", "brief", "early", "fast", "future", "late", "long", "modern", "old", "old-fashioned", "prehistoric", "quick", "rapid", "short", "slow", "swift", "young"]
card = ["cards", "decks", "draws"]
"""
for i in range(100): 
    print(f"{describe[random.randint(0, (len(describe) - 1))]} {describe[random.randint(0, (len(describe) - 1))]} {card[random.randint(0, len(card) -1)]}")
"""

f = open("names.txt", "a")

for a in range(len(card)):
    for b in range(len(describe)):
        for c in range(len(describe)):
            f.write(f"{describe[b - 1]} {describe[c - 1]} {card[a - 1]}\n")