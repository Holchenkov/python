import random

print("Начинаем игру. Повороты: [a]-Налево, [w]-Прямо, [d]-Направо Куда идти?")
vlevo = 0
vpered = 0
vpravo = 0
while True:
    vvod = input()
    if vvod not in ["w", "a" ,"d"]:
        print("Введите ещё раз")
    elif vvod == "w":
        if random.randint(1,10) == 1:
            vpered += 1
            print(f"Пошел прямо. Выход найден. Ты выиграл. Для того, чтобы найти выход ты {vlevo} раз повернул налево, {vpered} раз пошел прямо и {vpravo} раз повернул направо.")
            break
        else:
            print("Пошел прямо. Выхода пока нет... Куда идти?")
            vpered += 1
    elif vvod == "a":
        if random.randint(1,10) == 1:
            vlevo += 1
            print(f"Повернул налево. Выход найден. Ты выиграл. Для того, чтобы найти выход ты {vlevo} раз повернул налево, {vpered} раз пошел прямо и {vpravo} раз повернул направо.")
            break
        else:
            print("Повренул налево. Выхода пока нет... Куда идти?")
            vlevo += 1
    elif vvod == "d":
        if random.randint(1,10) == 1:
            vpravo += 1
            print(f"Повернул направо. Выход найден. Ты выиграл. Для того, чтобы найти выход ты {vlevo} раз повернул налево, {vpered} раз пошел прямо и {vpravo } раз повернул направо.")
            break
        else:
            print("Повренул направо. Выхода пока нет... Куда идти?")
            vpravo += 1
