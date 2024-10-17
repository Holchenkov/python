#Задание 1 
age = int(input("Введите ваш возраст: "))
if age<18:        
    print("Вы несовершеннолетний")
elif 18<= age <=65:    
    print("Вы трудоспособный человек")
else:    print("Вы пенсионер")
#Задание 2 
x = int(input("Введите стоимость покупки: "))
if x<1000:
    print("Скидка не предоставляется")
elif 1000<= x <=5000:
    print("Скидка 5%")
else:
    print("Скидка 10%")
#Задание 3
x = int(input("Введите число: "))
y = int(input("Введите второе число: "))
z = input("Введите операцию: ")
if z == "+":
    print("Результат вычислений:", x + y)
elif z == "-":
    print("Результат вычислений:", x - y)
elif z == "*":
    print("Результат вычислений:", x * y)
elif z == "/":
    print("Результат вычислений:", x / y)
else: 
    print("Неверная операция.")
#Задание 4 
x = int(input("Введите число: "))
if x % 2 == 0 and "x"[-1] == 2 or "x"[-1] == 6:
    print("True")
else:    
    print("False")
#Задание 5 
password = 12345
n = int(input("Введите пароль: "))
if n == password:
    print("Доступ разрешен ")
else:
    print("Неверный пароль ")
#Задание 6 
x = input("Введите координаты квадрата: ")
if x == "B1" or x == "B3" or x == "B7" or x == "C1" or x == "C4" or x == "C5" or x == "C6" or x == "C8" or x == "C9":
    print("В данном квадрате обитает синий попугай")
elif x == "B2" or x == "B4" or x == "B6" or x == "B8" or x == "C2" or x == "C7" or x == "C10" or x == "C11":
    print("В данном квадрате обитает зеленый попугай")
else:
    print("Квадарат пустой")
#Задание 7 
n = int(input("Введите число: "))
k = int(input("Введите второе число: "))
if n % k == 0:
    print("Кратно")
else: 
    print("Не кратно")
#Задание 8 
lvl = int(input("Введите ваш уровень: "))
hp = int(input("Введите ваше здоровье: "))
if lvl<0 or hp>100:
    print("Некорректные данные")
else:
    if lvl<5:
        print("Ваш уровень слишком низкий для выполнения миссии")
    else:
        if hp > 50:
            print("Вы готовы к миссии!")
        elif 20 < hp:
            print("Ваше здоровье низкое, будьте осторожны.")
        else:
            print("Ваше здоровье слишком низкое для выполнения миссии.")
#Задание 9 
inventory = ["яблоко", "шариковая ручка"]
missing_items = [] 
if "ключ" not in inventory:
    missing_items.append("ключ") 
if "фонарь" not in inventory:
    missing_items.append("фонарь") 
if len(missing_items)>0:
    print("Не хватает предметов для прохождения: " +", " .join(missing_items))
else:
    print("Проходите")
#Задание 10
king = "Enemies are coming! Are the archers ready?"
warrior = "For the Alliance!"
magician = "The spell is ready."
if king [-1] == "?" or king [-1] == "!" or king [-1] == ".":
    print("Знак имеется")
else:
    print("Знака нету")
if warrior [-1] == "?" or warrior [-1] == "!" or warrior [-1] == ".":
    print("Знак имеется")
else:
    print("Знака нету")
if  magician [-1] == "?" or magician [-1] == "!" or magician [-1] == ".":
    print("Знак имеется")
else:
    print("Знака нету")




        
                
                    
        









