num = int(input("type the number: "))

fizzbuzz_list = ["fizz"*(not i%3) + "buzz"*(not i%5) or i for i in range(1,num+1)]
print(fizzbuzz_list)

# first fizzbuzz
# num = int(input("type the number: "))
#
# for i in range(1, num+1):
#    if i % 15 == 0:
#        print("fizzbuzz")
#    elif i % 3 == 0:
#        print("fizz")
#    elif i % 5 == 0:
#        print("buzz")
#    else:
#        print(i)

# edit fizzbuzz conditions
# if i % 3 == 0 or i % 5 == 0:
#     print("fizz"*(not i%3) + "buzz"*(not i%5))
# else:
#     print(i)

# edit fizzbuzz without conditions
# print("fizz"*(not i%3) + "buzz"*(not i%5) or i)

