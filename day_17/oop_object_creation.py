#constructor

class Car:
    def __init__(self):
        print("Constructor triggered")



car = Car()
car.seats = 5

print(car.seats)