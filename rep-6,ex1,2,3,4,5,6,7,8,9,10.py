#Задание 1
names = ["Richard", "Igor", "Jonathan", "Alice", "Mary", "Bonnie"]
for i in names:
    print("Hello", i ,"!")
#Задание 2
phrase = "I'm learning cycles."
for i in range(10):
    print(phrase)
#Задание 3
stations = ["Малиновка", "Рябиновка", "Суслово", "Дрожжино", "Звягино"]
for i in range(5):
    station = stations[i]
    if i == 4:
       print(f"Поезд на станции: {station} Конечная!")
    else:
        print(f"Поезд на станции: {station}")
#Задание 4
shop = ["Laptop", "Smartphone", "Watch", "Tablet", "Headphones"]
for i in shop:
    print(i)
    if i == "Laptop":
        print("I'm buying this.")
    else:
        print("I don't need it.")
#Задание 5
tasks = ["Сдать проект (Важная)", "Сходить в магазин", "Позвонить врачу (Важная)", "Убраться в комнате", "Подготовить отчёт"]
for index, task in enumerate(tasks, start = 1):
    if "Важная" in task:
        print(f"{index}!: {task}") 
    else:
        print(f"{index}: {task}")
#Задание 6
x = int(input("Введите кол-во чисел: "))
z = 0
for i in range(x):
    y = int(input("Введите сами числа: "))
    z += y
print("Сумма чисел:", z)
#Задание 7
x = 0 
while x < 10:
    print(f"Цикл сработал {x} раз")
    x += 1
#Задание 8 
while True:
    x = input()
    if x == "w":
        print("Персонаж идёт вперёд")
    elif x == "a":
        print("Персонаж идёт влево")
    elif x == "s":
        print("Персонаж идёт назад")
    elif x == "d":
        print("Персонаж идёт вправо")
    elif x == "stop":
        print("Программа остановлена")
        break
    else:
        print("Неизвестная команда! Попробуйте снова.")
#Задание 9
while True:
    x = int(input("Введите число от 1 до 9: "))
    if x < 1 or x > 10:
        print("Число вне диапозона. Попробуйте снова.")
    else:
        break
y = 1
while y <= 10:
    z = y * x 
    print(f"{x} * {y} = {z}")
    y += 1
#Задание 10
x = "Все"
y = 3
print(f"Попыток осталось: {y}\nЗагадка: Сколько отжиманий сделал Евгений Шатаев вчера?")
while y > 0:
    z = input("ответ: ")
    if z == x:
        print("Загадка разгадана. Поздравляю!")
        break
    else:
        print(f"Неправильно!\nПопыток осталось: {y-1}\nЗагадка: Сколько отжиманий сделал Евгений Шатаев вчера?")
        y -= 1
    
    
        
    
    

    

