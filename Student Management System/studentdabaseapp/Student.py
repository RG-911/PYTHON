class Student:
    courses = " "
    tuition_balance = 0
    cost_of_course = 600
    id = 1000

    # Constructor: prompt user to enter student's name and year
    def __init__(self):
        self.first_name = str(input("Enter student's first name: "))
        self.last_name = str(input("Enter student's last name: "))
        self.grade_year = input("1 - Fresmen\n2 - Sophmore\n3 - Junior\n4 - Senior\nEnter student's class level: ")
        self.set_student_id()
        self.enroll()
        self.pay_tuition()


    # Generate ID
    def set_student_id(self):
        self.id += 1
        self.student_ID = self.grade_year + "" + str(self.id)

    # Enroll in courses
    def enroll(self):
        while True:
            print("Enter course to enroll (Q to quit): ")
            course = input()
            if course != "Q":
                self.courses = self.courses + "\n" + course
                self.tuition_balance = self.tuition_balance + self.cost_of_course

            else:
                break

    # View  balance
    def view_balance(self):
        print("Your balance is: $" + str(self.tuition_balance))

    # Pay tuition
    def pay_tuition(self):
        self.view_balance()
        print("Enter your payment: $")
        payment = int(input())
        self.tuition_balance = self.tuition_balance - payment
        print("Thank your for payment of $" + str(payment))
        self.view_balance()

    # Show status
    def __str__(self):
        return "Name: {} {}".format(self.first_name,self.last_name) + \
               "\n" + "Grade Level: {}".format(self.grade_year) + \
               "\n" + "Student ID: {}".format(self.student_ID) + \
               "\n" + "Courses Enrolled: {}".format(self.courses) + \
               "\n" + "Balance: ${}".format(self.tuition_balance)


