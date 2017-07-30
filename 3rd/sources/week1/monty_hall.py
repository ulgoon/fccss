# import random library
import random

# initialize stay, switch
stay = 0
switch = 0

# set doors 1 car(1), 2 goats(0)
# get user's choice with randrange
# if user's choice was 1, stay + 1
# if not, switch + 1
for i in range(1000):
    doors = [1, 0, 0]
    random.shuffle(doors)

    choice = random.randrange(3)

    user = doors[choice]

    if user == 1:
        stay = stay + 1
    else:
        switch = switch + 1

# after 1000 times of simulation, print the results
print("stay: %4d" % stay)
print("switch: %4d" % switch)
