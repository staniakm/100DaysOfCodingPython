def prime_checker(number):
    count = 0
    for l in range(1, number + 1):
        if number % l == 0:
            count += 1
        if count > 2:
            return False
    return count == 2


number = int(input("Give me a number"))
result = prime_checker(number)
print(f"{number} Is prime? {result}")
