line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]

treasure_map = [line1, line2, line3]
abc = ["A", "B", "C"]
result = list(input("Where do you want to hide treasure? (eg. B2)").upper())

column = abc.index(result[0])
row = int(result[1]) - 1

treasure_map[row][column] = "X"

print(f"{treasure_map[0]}\n{treasure_map[1]}\n{treasure_map[2]}")
