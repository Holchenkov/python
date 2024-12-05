#Задание 1
x = lambda a, b: a * b
print(x(2,3))
#Задание 2
spisok = []
vvod1 = int(input("Всего чисел будет: "))
for i in range(vvod1):
    vvod2 = int(input(""))
    spisok.append(vvod2)
new1 = list(filter(lambda n: (n % 5 == 0 and n % 3 == 0), spisok))
print(new1)
