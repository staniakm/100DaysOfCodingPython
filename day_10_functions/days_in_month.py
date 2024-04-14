def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap")
                return True
            else:
                print("Not leap")
                return False
        else:
            print("Leap")
            return True
    else:
        print("Not leap")
        return False


days_in_month = [
    31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
]


def days_in_month(year, month):
    if (month == 2):
        if is_leap(year):
            return 29
        else:
            return days_in_month[month - 1]
    else:
        return days_in_month[month - 1]


year = int(input("What year?"))
month = int(input("What month?"))
print(f"Days in month: {days_in_month(2024, 2)}")
