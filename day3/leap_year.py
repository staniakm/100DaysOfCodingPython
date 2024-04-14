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
