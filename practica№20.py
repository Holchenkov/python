#Задание 1
file = open("new file.txt", "w")
file.write("Hello, world!")
file.close()
#Задание 2
file1 = open("input.txt", "w")
file1.write("Hello, world!")
file1.close()
file2 = open("output.txt", "w")
file2.close()

file1 = open("input.txt", "r")
content = file1.read()
file1.close()

file2 = open("output.txt", "w")
file2.write(content + "<copy>")
file2.close()
#Задание 3
from datetime import *

def add_entry(x: str):
    y = datetime.today()
    with open( "log note.txt", "a") as file:
        file.write(f"{y}: {x}\n")

add_entry("Запись 1")
#Задание 4
with open("data.txt", "r") as file:
    c = file.read()
count = 0
s = c.split()
for i in s:
    if i == "John":
        count += 1
print(count)
#Задание 5
slovar = {'б':'а', 'в':'б', 'г':'в', 'д':'г', 'е':'д', 'ё':'е', 'ж':'ё', 'з':'ж', 'и':'з', 'й':'и', 'к':'й', 'л':'к', 'м':'л',
'н':'м', 'о':'н', 'п':'о', 'р':'п', 'с':'р', 'т':'с', 'у':'т', 'ф':'у', 'х':'ф', 'ц':'х', 'ч':'ц', 'ш':'ч',
'щ':'ш', 'ъ':'щ', 'ы':'ъ', 'ь':'ы', 'э':'ь', 'ю':'э', 'я':'ю', 'а':'я', 'О':'1', 'Д':'2', 'Т':'3', 'Ч':'4',
'П':'5', 'Ш':'6', 'С':'7', 'В':'8', 'Е':'9', 'Я':'0', '/':'.', '_':'!', ',':' ', ' ':',', '^':':', '*':'\n'}
with open("encrypt_mess.txt", "r", encoding="utf-8") as file:
    c = file.read()
for i in c:
    if i in slovar:
        print(slovar[i], end='')
    else:
        print(i, end='')
#Задание 6
vvod = str(input("Введите текстовое сообщение: "))
print("Хотите ли вы сохранить это сообщение?(yes/no) ")
vvod2 = input(">")
if vvod2 == 'yes':
    vvod3 = input('Введите имя файла, в котором сохранится ваше сообщение: ')
    with open( vvod3 , "w") as file:
        file.write(f"{vvod}")
else:
    print('no save')
