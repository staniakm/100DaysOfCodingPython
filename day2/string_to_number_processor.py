two_digit_numer = input("Provide two digit number")

if (len(two_digit_numer) != 2):
    print("Bad input")
else:
    result = int(two_digit_numer[0]) + int(two_digit_numer[1])
    print("Result is: " + str(result))
