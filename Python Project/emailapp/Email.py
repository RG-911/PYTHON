import random


class Email:
    # Constructor to receive the first name and last name
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.company_suffix = "xzy.com"
        self.mailbox_capacity = 500

        # Call a method asking for the department - return the department
        self.department = self.set_department()

        # Call the method returns a random password
        self.password = self.random_password()
        print("Your password is: " + self.password)

        # Combine element to generate an email
        self.email = self.first_name.lower() + "." + self.last_name.lower() + "@" + self.department + "." + \
                     self.company_suffix

    # Ask for the department
    def set_department(self):
        dep_choice = input("DEPARTMENT CODES\n1 for Sales\n2 for Development\n3 for Accounting\n0 for none\n "
                           "Enter the department code: ")
        if dep_choice == "1":
            return "sales"
        elif dep_choice == "2":
            return "dev"
        elif dep_choice == "3":
            return "acct"
        else:
            return ""

    # Generate a random password
    def random_password(self, length=10):
        password_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
        rand = ''.join(random.sample(password_set, length))
        return rand

    # Set the mailbox capacity
    def set_mailbox_capacity(self, capacity=500):
        self.mailbox_capacity = capacity

    # Set the alternate Email
    def set_alternate_email(self, alt_email):
        self.alternate_email = alt_email

    # Change the password
    def change_password(self, password):
        self.password = password

    # Get Email data
    def get_mailbox_capacity(self):
        return self.mailbox_capacity

    def get_alternate_email(self):
        return self.alternate_email

    def get_password(self):
        return self.password

    def show_info(self):
        return "DISPLAY NAME: " + self.first_name + " " + self.last_name + "\nCOMPANY EMAIL: " + self.email + \
               "\nMAILBOX CAPACITY:" + str(self.mailbox_capacity) + "mb "



