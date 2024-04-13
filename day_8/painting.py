import math


def paint_calc(height, width, coverage):
    return math.ceil((height * width) / coverage)


print(f"Need cans: {paint_calc(height=3, width=9, coverage=5)}")
