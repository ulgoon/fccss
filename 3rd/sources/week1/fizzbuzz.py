num = int(input("type the number: "))

for i in range(1,num+1):
        print("fizz"*(not i%3) + "buzz"*(not i%5) or i)

