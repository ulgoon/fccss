# Ethiopian Multiplication

# Define operation with function
def halve(x):
    return x // 2

def double(x):
    return x * 2

def even(x):
    return not x % 2

# Get user input
numberset = str(input("Type two number with SPACE: ")).split()

# Main Process
def ethiopian(first, second):
    result = 0
    # 첫번째 수가 0이 될 때 까지 진행
    while first >= 1:
        # 짝수일때, struck 출력
        if even(first):
            print("%4d %7d struck" % (first, second))
        # 홀수일때, keep 출력 및 result에 second 값 더하기
        else: 
            print("%4d %7d keep" % (first, second))
            result += second

        # first halve 연산, second double 연산
        first = halve(first)
        second = double(second)

    # 최종 결과 출력
    print("The result is ", result)

# ethiopian 실행명령
ethiopian(int(numberset[0]), int(numberset[1]))
