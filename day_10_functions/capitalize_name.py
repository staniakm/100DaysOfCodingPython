def capitalizer(f_name, l_name):
    name = f_name.capitalize()
    last_name = l_name.capitalize()
    return f"{name} {last_name}"


print(capitalizer("joe", "monster"))
