def points_to_score(points):
    if 91 <= points <= 100:
        return "Outstanding"
    elif 81 <= points <= 90:
        return "Exceed Expectation"
    elif 71 <= points <= 80:
        return "Acceptable"
    else:
        return "Fail"


students_grades = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

students_score = {}

for student in students_grades:
    students_score[student] = points_to_score(students_grades[student])
print(f"{students_score}")
