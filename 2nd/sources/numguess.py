import random

# store answer to answer
answer = random.randint(1,100)
print(answer)
# ask username and set chance to 3
username = input("What is your name? ")
chance = 3
# main process evaluate input and compare with answer
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









