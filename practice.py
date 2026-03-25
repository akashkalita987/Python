n = int(input("\nEnter how many number:"))
student = []
for i in range(n):
    name = input("\nEnter the name of the  student")
    roll = int(input("\nEnter the roll no of the student"))
    grade = input("\nEnter the grade of the student")
    student.append(name)
    student.append(roll)
    student.append(grade)

# Print only the names of the students
print(*student[::3], sep='\n')