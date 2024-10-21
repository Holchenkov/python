#Задание 1 
x = int(input("Введите число: "))
y = "*" * x 
if x > 100:
    print("*")
elif x < 0:
    print()
else:
    print(y)
#Задание 2 
x = input("Введите первую строку: ")
y = input("Введите вторую строку: ")
if x == y:
    print(True)
else:
    print(False)

#Задание 3
r = int(input("Введите значение красного: "))
g = int(input("Введите значение зеленого: "))
b = int(input("Введите значение голубого: "))
if r == 0 and g == 0 and b == 0:
    print("Черный цвет")
elif r == 255 and g == 255 and b == 255:
    print("Белый цвет")
elif r == 255 and g == 0 and b == 0:
    print("Красный цвет")
elif r == 0 and g == 255 and b == 0:
    print("Зеленый цвет")
elif r == 0 and g == 0 and b == 255:
    print("Голубой цвет")
else:
    print("Нет цвета")
