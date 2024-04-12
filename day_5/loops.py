# for loop

fruits = ["Apple", "Orange", "Peach", "Pear"]
print("For loop ...")
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print("End of for loop")

print("Practice")

student_heights = input().split()
print(len(student_heights))

# convert to int
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total = 0
number = 0

for student in student_heights:
    total += student
    number += 1

average = total / len(student_heights)

print(student_heights)

print(f"Total height: {total}")
print(f"Number of students: {number}")
print(f"Average {average}")
