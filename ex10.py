class Account:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited Amount:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn Amount:", amount)
        else:
            print("Insufficient Balance!")

    def display(self):
        print("\nAccount Details")
        print("Account Number:", self.acc_no)
        print("Account Holder Name:", self.name)
        print("Account Type:", self.acc_type)
        print("Current Balance:", self.balance)


# Creating an object
a1 = Account(101, "Rahul", "Savings", 5000)

# Performing operations
a1.display()
a1.deposit(2000)
a1.withdraw(1000)
a1.display()