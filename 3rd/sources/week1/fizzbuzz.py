num = int(input("type the number: "))

fizzbuzz_list = ["fizz"*(not i%3) + "buzz"*(not i%5) or i for i in range(1,num+1)]
print(fizzbuzz_list)

