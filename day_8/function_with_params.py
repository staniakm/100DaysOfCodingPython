def greet(name):
    print("Hello")
    print(name)
    print("!!!")


greet("Joe")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Great to see you from {location}")


greet_with(name="Joe", location="Poland")
greet_with(location="USA", name="Paul")
