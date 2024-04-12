student_score = input().split()

max_score = 0

for score in student_score:
    if int(score) > max_score:
        max_score = int(score)

print(f"Max score is {max_score}")
