# import randint in random library
from random import randint


# get random integer 1 to 100 and save as answer
answer = randint(1,100)
print(answer)

# get username, 1 integer for guessing and print username
username = input("Hi, What is your name? ")

# repeat ask and print loop
while True:
    guess = eval(input("Hi, %s. Guess the number(1 to 100) - " % (username)))

    # main logic to compare with guess(user input) and answer
    if guess == answer:
        print("Correct!")
        break
    elif guess > answer:
        print("Too High! Try again!")
    elif guess < answer:
        print("Too Low! Try again!")
