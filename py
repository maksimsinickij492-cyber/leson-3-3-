
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Гроші успішно додано!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Гроші успішно знято!")
        else:
            print("Недостатньо коштів на рахунку!")

account = BankAccount("123456", 1000)

account.deposit(500)


account.withdraw(300)

print("Номер рахунку:", account.account_number)
print("Баланс рахунку:", account.balance)
