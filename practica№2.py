#Задание 1
x = int(input("Введите число байтов: "))
y = (x*8) 
print("Число бит: ", y)
#Задание 2
S = int(input("Введите количество страниц: "))
C = int(input("Введите количество строк: "))
N = int(input("Введите количесто символов: "))
V1 = (S * C * N)
V2 = (V1/1024)
print("Объём текстого файла в Кбайтах: ",V2)
