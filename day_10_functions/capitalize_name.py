def capitalizer(f_name, l_name):
    name = f_name.capitalize()
    last_name = l_name.capitalize()
    return f"{name} {last_name}"


def format_name(f_name, l_name):
    return f"{f_name.title()} {l_name.title()}"


print(capitalizer("joe", "monster"))
print(format_name("joe", "MONSTER"))
