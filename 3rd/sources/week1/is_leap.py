leap = False
def is_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap = True
        return leap

year = int(input("Is leap? "))
print(is_leap(year))
