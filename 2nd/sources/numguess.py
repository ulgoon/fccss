import random


answer = random.randint(1,100)
print(answer)

username = input("What is your name? ")

while True:
    guess = eval(input("Hi, " + username + ". Guess the number: "))

    if guess == answer:
        print("Correct!")
        break
    elif guess > answer:
        print("Too High")
    elif guess < answer:
        print("Too Low")
    else:
        print("You are wrong!")









