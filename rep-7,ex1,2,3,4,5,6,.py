#Задание 1
def create_car(brand, color, max_speed):
    return f"Марка: {brand} Цвет: {color} Максимальная скорость: {max_speed} км/ч"

car_1 = create_car("Lada", "Красный", 470)
car_2 = create_car("Honda", "Серый", 180)

print(car_1)
print(car_2)
#Задание 2
switch_1 =True
switch_2 = False
switch_3 = None

def switch_check(switch):
    if switch == True:
        print("True работает")
    elif switch == False:
        print("False не работает")
    else:
        print(f"{switch} сломан")

switch_check(switch_1)
switch_check(switch_2)
switch_check(switch_3)
#Задание 3
def fun(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        p = a + b + c
        pp = p / 2
        s = (pp * (pp - a) * (pp - b) * (pp - c)) ** 0.5
        s = round(s, 2)
        if a == b == c:
            print("----------------------------------\n"
                f"Длина сторон треугольника: {a},{b},{c}\n"
                "----------------------------------\n"
                "Информация:\n"
                "Равносторонний треугольник.\n"
                f"Периметр: {p}\n"
                f"Площадь: {s}\n"
                "----------------------------------\n")
        elif a == b or a == c or b == c:
            print("----------------------------------\n"
                f"Длина сторон треугольника: {a},{b},{c}\n"
                "----------------------------------\n"
                "Информация:\n"
                "Равнобедренный треугольник.\n"
                f"Периметр: {p}\n"
                f"Площадь: {s}\n"
                "----------------------------------\n")
        else:
            print("----------------------------------\n"
                f"Длина сторон треугольника: {a},{b},{c}\n"
                "----------------------------------\n"
                "Информация:\n"
                "Разносторонний треугольник.\n"
                f"Периметр: {p}\n"
                f"Площадь: {s}\n"
                "----------------------------------\n")
    else:
        print("Некорректные стороны. Невозможно построить треугольник.")

fun(15,15,15)
fun(15,20,15)
fun(15,20,25)
fun(1,2,3)
#Задание 4
def number_change(input_number, output_number):
    if input_number < output_number:
        x = 0
        while input_number != output_number:
            input_number += 1
            x += 1
        q = x, input_number, output_number
        print(q)
    elif input_number > output_number:
        y = 0
        while output_number != input_number:
            input_number -= 1
            y += 1
        w = y, input_number, output_number
        print(w)
    else:
        e = 0, input_number, output_number
        print(e)

number_change(2,10)
number_change(5,1)
number_change(3, 3)
#Задание 5
player = 0

def info_player():
    print(f"Игрок пробежал {player} км.")

def run_player(km):
    global player
    x = km/2
    player += x

info_player()
run_player(30)
run_player(12.5)
info_player()
#Задание 6
def info_number(number: int) -> str:
    """
    Выполняет операции над числом.

    Функция определяет:
    - Является ли число больше 5.
    - Является ли число четным.
    - Квадарат числа.

    Параметры:
    number (int): Целое положительное число.

    Возвращает:
    str: Строка с информацией о числе, больше ли оно 5, является ли оно четным и его квадрат.
    Если число меньше 5, возвращает сообщение об ошибке.

    Пример:
     >> info_number(4)
    Число: 4
    Больше 5: False
    Ошибка. Число меньше 5.
     >> info_number(7)
    Число: 7
    Больше 5: True
    Четное: False
    Ошибка. Число нечетное
    >> info_number(8)
    Число: 8
    Больше 5: True
    Четное: True
    Квадрат числа: 64
    """

    # Проверка, является ли число больше 5
    if number < 5:
        return "Ошибка. Число меньше 5."

    # Проверка, является ли число чётным
    if number % 2 == 0:
        even = True
    else:
        even = False
        return "Ошибка. Число нечетное."

    # Поиск квадрата числа
    x = number ** 2

    return f"Число: {number}\nЧётное: {even}\nКвадрат числа: {x}"

# Пример использования:
print(info_number.__doc__)  # Документация функции
print(info_number(4))  # Вывод сообщения об ошибке
print(info_number(7))  # Вывод сообщения об ошибке
print(info_number(8))  # Вывод квадрата четного числа, которое больше пяти
