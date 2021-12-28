import self as self

import studentdabaseapp
from studentdabaseapp import Student


class StudentDatabaseApp:
    # Ask how many new students we want to add
    print("Enter number of new students to enroll: ")
    num_of_students = int(input())
    students = [num_of_students]

    # Create n number of students
    for n in range(num_of_students):
        students[n-1] = studentdabaseapp.Student.Student()
        print(str(students[n-1]))
