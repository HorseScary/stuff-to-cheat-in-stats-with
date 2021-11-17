from typing import Counter


f = open("possibility.txt", 'r')

lines = f.readlines()

Counter = 0

for line in lines:
    if line[1] == line[8] and line[0] == line[7] and line[1] == line[15] and line[0] == line[14]:
        Counter+=1
print(Counter)

# line 14

# sp
# di
# cl
# he