import random


answer = random.randint(1,100)
print(answer)

username = input("What is your name? ")

while True:
    guess = eval(input("Hi, " + username + ". Guess the number: "))

    if guess == answer:
        print("Correct!")
        break
    else:
        print("You are wrong!")
