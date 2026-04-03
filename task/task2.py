class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{self.owner} поповнив рахунок на {amount} грн.")
        else:
            print("Сума поповнення має бути додатною!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{self.owner} зняв {amount} грн.")
        else:
            print("Недостатньо коштів або некоректна сума!")

    def get_balance(self):
        return self.__balance


acc1 = BankAccount("Іван", 1000)
acc2 = BankAccount("Марія", 500)
acc3 = BankAccount("Олег")

print(f"Баланс {acc1.owner}: {acc1.get_balance()} грн")
acc1.deposit(300)
acc1.withdraw(200)
print(f"Баланс {acc1.owner}: {acc1.get_balance()} грн\n")

print(f"Баланс {acc2.owner}: {acc2.get_balance()} грн")
acc2.withdraw(600)
acc2.deposit(100)
print(f"Баланс {acc2.owner}: {acc2.get_balance()} грн\n")

print(f"Баланс {acc3.owner}: {acc3.get_balance()} грн")
acc3.deposit(700)
acc3.withdraw(200)
print(f"Баланс {acc3.owner}: {acc3.get_balance()} грн")