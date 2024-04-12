line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]

treasure_map = [line1, line2, line3]

result = list(input("Where do you want to hide treasure? (eg. B2)").upper())

column = 0
if (result[0] == "A"):
    column = 0
elif result[0] == "B":
    column = 1
else:
    column = 2
row = int(result[1]) - 1

treasure_map[row][column] = "X"

print(f"{treasure_map[0]}\n{treasure_map[1]}\n{treasure_map[2]}")
