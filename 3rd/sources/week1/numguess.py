# import randint in random library
from random import randint


# get random integer 1 to 100 and save as answer
answer = randint(1,100)
print(answer)

# get username, 1 integer for guessing and print username
username = input("Hi, What is your name? ")

# limitation of trying
trial = 5

# repeat ask and print loop
while True:
    guess = eval(input("Hi, %s. Guess the number(1 to 100) - " % (username)))

    # main logic to compare with guess(user input) and answer
    if guess == answer:
        print("Correct!")
        break
    elif guess > answer:
        trial -= 1
        print("Too High! Try again!(%d times left)" % (trial))
    elif guess < answer:
        trial -= 1
        print("Too Low! Try again!(%d times left)" % (trial))

    if trial == 0:
        print("Wrong! The answer was", str(answer))
        break
