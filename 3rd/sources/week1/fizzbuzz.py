num = int(input("type the number: "))

for i in range(1,num+1):
    if i % 3 == 0 or i % 5 == 0:
        print("fizz"*(not i%3) + "buzz"*(not i%5))
    else:
        print(i)

