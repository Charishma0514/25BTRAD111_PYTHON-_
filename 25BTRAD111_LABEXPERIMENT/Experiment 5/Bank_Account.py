class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance or invalid amount")

    def check_balance(self):
        print("Current Balance:", self.__balance)


account = BankAccount("Rahul", 5000)

account.check_balance()
account.deposit(2000)
account.withdraw(1000)
account.check_balance()
account.withdraw(10000)
