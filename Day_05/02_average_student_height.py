student_heights = input('Input a list of student heights ').split()
for n in range(len(student_heights)):
    student_heights[n] = int(student_heights[n])

# total = sum(student_heights)
# print(total//len(student_heights))
length = 0
total = 0
for i in student_heights:
    length+=1
    total+=i

avg = round(total/length)
print(avg)