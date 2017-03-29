import random


answer = random.randint(1,100)
print(answer)

username = input("What is your name? ")
chance = 3

while True:
    guess = eval(input("Hi, " + username + ". Guess the number: "))

    if guess == answer:
        print("Correct!")
        break
    elif guess > answer:
        chance -= 1
        print("Too High. (%d times left)" % (chance))
    elif guess < answer:
        chance -= 1
        print("Too Low. (%d times left)" % (chance))
    
    if chance == 0:
        print("You are dead.")
        break









