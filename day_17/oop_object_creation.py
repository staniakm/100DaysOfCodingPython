# constructor

class Car:
    def __init__(self, mark, model, seats):
        print("Constructor triggered")
        self.seats = seats
        self.mark = mark
        self.model = model


car = Car(mark="Toyota", model="Corolla", seats=5)

print(car.seats)
print(car.mark)
