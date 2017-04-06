year = int(input("type the year what you want: "))
# leap year checking function
def is_leap(year, leap=False):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap = True
    return leap
# run function
leap = is_leap(year)
# print result depend on leap
def print_result():
    if leap == True:
        print("This is leap year")
    else:
        print("This is common year")

print_result()
