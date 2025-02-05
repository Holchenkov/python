import random
class BankAccount:
    def __init__(self, owner, balance, popolnenie, snatie, trans, polychik):
        self.owner = owner
        self.balance = balance
        self.popolnenie = popolnenie
        self.snatie = snatie
        self.trans = trans
        self.polychik = polychik
    def get_balance(self):
        print(f"-----------------------------\nВладелец: {self.owner}\nНомер счёта: {"".join(str(random.randint(0, 10)) for i in range(10))}\nБаланс: {self.balance}\n-----------------------------")

    def deposit(self):
        print(f"Пополнение {self.popolnenie}. Баланс: {self.popolnenie + self.balance}\n-----------------------------")

    def withdraw(self):
        if self.balance >= self.snatie:
            print(f"Снятие {self.snatie}. Баланс {self.balance + self.popolnenie - self.snatie}\n-----------------------------")
        else:
            print(f"Снятие невозжможно! Не хватает средств.\n-----------------------------")

    def transfer(self):
        print(f"Перевод {self.trans} выполнен на счёт {self.polychik}")
        print("-----------------------------")
        print()
        print()

owner_1 = BankAccount("Д. Нагиев", 10000,  4000, 1000, 2000, "Petyx")
owner_1.get_balance()
owner_1.deposit()
owner_1.withdraw()
owner_1.transfer()
owner_2 = BankAccount("Ж. Акака", 4000, 5666, 2313, 2000, "qwerty")
owner_2.get_balance()
owner_2.deposit()
owner_2.withdraw()
owner_2.transfer() 
