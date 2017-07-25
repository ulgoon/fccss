# import randint in random library
from random import randint


# get random integer 1 to 100 and save as answer
answer = randint(1,100)
print(answer)

# get username, 1 integer for guessing and print username
username = input("Hi, What is your name? ")
guess = eval(input("Hi, %s. Guess the number(1 to 100) - " % (username)))

# main logic to compare with guess(user input) and answer
if guess = answer:
    print("Correct!")
else:
    print("Wrong!")
