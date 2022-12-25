student_Scores = {
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62,
}

student_grades = {}
for student in student_Scores:
    score = student_Scores[student]
    if score>90:
        student_grades[student] = "Outstanding"
    elif score>80:
        student_grades[student] = "Exceeds Expectations"
    elif score>70:
        student_grades[student] = "Accepatable"
    else:
        student_grades[student] = "Fail"

print(student_grades)