import random


stay = 0
switch = 0

for i in range(1000):
    doors = [1, 0, 0]
    random.shuffle(doors)

    choice = random.randrange(3)

    user = doors[choice]

    if user == 1:
        stay = stay + 1
    else:
        switch = switch + 1

print("stay: %4d" % stay)
print("switch: %4d" % switch)
