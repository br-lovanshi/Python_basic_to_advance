class Account:
    def __init__(self, account, balance):
        self.__account = account
        self.__balance = balance

    def debit(self, amount):
        self.__balance -= amount
        print(amount, "Has been deducted")
        print("Available balance is", self.available_balance(), "\n")

    def credit(self, amount):
        self.__balance += amount
        print(amount, "Has been credited")
        print("Available balance is", self.available_balance(), "\n")

    def available_balance(self):
        return self.__balance


acc = Account(989893, 1000)
acc.credit(66666)
acc.debit(7000)
acc.debit(3000)
acc.debit(8334)
acc.debit(5000)

