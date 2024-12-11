#Зададние 1
import math

vvod = int(input("Введите число: "))
print(f"Квадратный корень числа {vvod} - {math.sqrt(vvod)} ")
print(f"Значение синуса и косинуса для числа {vvod} - {math.sin(vvod)} и {math.cos(vvod)}  ")
print(f"Факториал числа {vvod} - {math.factorial(vvod)}  ")
#Зададние 2
import random

q = []
for i in range(5):
    q.append(random.randint(1, 50))
print(f"Пять случайных чисел от 1 до 50 - {q}")
spisok = [10, 20, 30, 40, 50]
y = random.choice(spisok)
print(f"Случайное число из списка - {y}")
z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(z)
print(f"Перемешанный список - {z}")
#Задание 3
import datetime

print(f"Текущая дата и время - {datetime.datetime.today()}")
print(f"Текущий год, месяц и день - {datetime.date.today()}")
today = datetime.date.today()
future = today + datetime.timedelta(days=7)
print(f"Дата через 7 дней от текущего момента - {future}")
#Задание 4
import random, time
from colorama import Fore, Style

print("Программа генерирует число... ")
time.sleep(3)
random_chislo = random.randint(0,10)
q = 0
while True:
    vvod = int(input("Введите число: "))
    if vvod > 10:
        print(Fore.RED + "Введите число от 0 до 10." + Style.RESET_ALL)
    elif vvod > random_chislo:
        print(Fore.RED + "Ваше число больше." + Style.RESET_ALL)
        q += 1
    elif vvod < random_chislo:
        print(Fore.RED + "Ваше число меньше." + Style.RESET_ALL)
        q += 1
    else:
        print(Fore.GREEN + "Вы угадали!" + Style.RESET_ALL)
        print(f"Попыток было: {q}")
        break
#Задание 5
import time, random

print("Добро пожаловать в игру 'Бросок кубика для двоих'!")
kybik = ("[       ]\n"
         "[   *   ]\n"
         "[       ]",

        "[*      ]\n"
        "[       ]\n"
        "[      *]",

        "[*      ]\n"
        "[   *   ]\n"
        "[      *]",

        "[*     *]\n"
        "[       ]\n"
        "[*     *]",

        "[*     *]\n"
        "[   *   ]\n"
        "[*     *]",

        "[*     *]\n"
        "[*     *]\n"
        "[*     *]",)

while True:
    print("Бросок кубика для компьютера... ")
    time.sleep(3)
    comp = random.randint(0,5)
    print(f"Выпало число: {comp +1}")
    print(kybik[comp])
    input("Теперь ваша очередь! Нажмите Enter для броска кубика.")
    print("Бросок кубика для вас... ")
    time.sleep(3)
    people = random.randint(0,5)
    print(f"Выпало число: {people + 1}")
    print(kybik[people])
    if comp > people:
        print("Компьютер победил!")
        break
    elif comp < people:
        print("Вы победили!")
        break
    else:
        print("Ничья! Бросаем кубик снова...")
        time.sleep(3)
