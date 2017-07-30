# get input with space
numbers = str(input("two nums with space: ")).split()

# initialize result, set num1, num2 with splited numbers
result = 0
num1 = int(numbers[0])
num2 = int(numbers[1])

# repeat until num1 equal to 1
# condition: struck(num1 == even), keep(num1 == odd, add to result)
# num1 divide by 2, num2 multiply by 2
while num1 >= 1:
    if num1 % 2 == 0:
        print("%4d %7d struck" % (num1, num2))
    else:
        print("%4d %7d keep" % (num1, num2))
        result = result + num2

    num1 = num1 // 2
    num2 = num2 * 2

# after while loop, print result with string
print("The result is ", result)

