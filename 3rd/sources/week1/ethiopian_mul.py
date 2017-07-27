numbers = str(input("two nums with space: ")).split()

result = 0
num1 = int(numbers[0])
num2 = int(numbers[1])

while num1 >= 1:
    if num1 % 2 == 0:
        print("%4d %7d struck" % (num1, num2))
    else:
        print("%4d %7d keep" % (num1, num2))
        result = result + num2

    num1 = num1 // 2
    num2 = num2 * 2

print("The result is ", result)

