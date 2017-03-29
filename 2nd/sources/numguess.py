import random


answer = random.randint(1,100)
print(answer)

username = input("What is your name? ")
guess = eval(input("Hi, " + username + ". Guess the number: "))
print(guess)
