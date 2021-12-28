class BankAccount:
    balance = 0
    amount = 0
    previous_transaction = 0

    def __init__(self):
        self.customer_name = input("Enter your customer name: ")
        self.customer_id = input("Enter you customer ID: ")

    def deposit(self, amount):
        self.amount = amount
        if self.amount != 0:
            self.balance += int(amount)
            self.previous_transaction = amount

    def withdraw(self, amount):
        if self.amount != 0:
            self.balance -= int(amount)
            self.previous_transaction = -int(amount)

    def get_prev_trans(self):
        if self.previous_transaction > 0:
            print("Deposited: " + str(self.previous_transaction))

        elif self.previous_transaction < 0:
            print("Withdrawn: " + str(abs(self.previous_transaction)))

        else:
            print("No transaction occurred")

    def show_menu(self):
        print("\nWelcome " + self.customer_name)
        print("Your ID is " + self.customer_id)
        print("\nA ==> Check Balance")
        print("B ==> Deposit")
        print("C ==> Withdraw")
        print("D ==> Previous Transaction")
        print("E ==> Exit")
        option = ""
        while option != "E":
            print("==============================================")
            print("Enter an option")
            print("==============================================")
            option = input("")

            if option == "A":
                print("..............................................")
                print("Balance = " + str(self.balance))
                print("..............................................")

            elif option == "B":
                print("..............................................")
                print("Enter an amount to deposit: ")
                print("..............................................")
                amount_input = input()
                self.deposit(amount_input)

            elif option == "C":
                print("..............................................")
                print("Enter an amount to withdraw: ")
                print("..............................................")
                amount_input = input()
                self.withdraw(amount_input)

            elif option == "D":
                print("..............................................")
                self.get_prev_trans()
                print("..............................................")

            elif option == "E":
                print("**********************************************")
                print("Thank you for using our services.")

            else:
                print("Invalid Option! Please, enter again.")

    def __str__(self):
        return str(self.show_menu())


account1 = BankAccount()
print(account1)
