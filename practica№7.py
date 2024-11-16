#Задание 1
print('начальный список')
x = [
    ['folder', 'coursework.doc', 'folder', 'pict.png', 'data.accdb'],
    ['icon.ico', 'script.js', 'index.html', 'style.css', 'prog.py'],
    ['my_song.mp3', 'anapa-2003.jpg', 'cs_1.6.exe', 'folder', 'cheat.txt'],
    ['notes.txt', 'main.py', 'work.pdf', 'cartoon.mp4', 'array.py'],
    ['project.psd', 'cycle.py', 'folder', 'cycle.js', 'turtle.py']
    ]
for i in x:
    print(i)
print('без папок и с заменой data ')
for i in x:
    while 'folder' in i:
        i.remove("folder")
    for a in range(len(i)):
        if i[a] == 'data.accdb':
            i[a] = 'data.sql'
for i in x:
    print(i)
print('все файлы.py ')
p = []
for i in x:
    for a in i:
        if a[-3:] == ".py":
            p.append(a)
print(p)
print("все new_файлы.js ")
v = []
for i in x:
    for a in i:
        if a[-3:] == ".js":
            v.append('new_' + a)
print(v)
#Задание 2
word_numb = ["ноль", "один", "два", "три", "четыре", "пять",
"шесть", "семь", "восемь", "девять"]
n = int(input("Введите число от 0 до 9:" ))
if n > 9:
    print('Введите число <= 9')
else:
    for i in range(n+1):
        print(word_numb[i])
#Задание 3
bin_sy = ['11011111', '11011101', '11000111', '11011100',
'11011110']
gg = []
for i in bin_sy:
    print(int(i, 2))
    gg.append(int(i, 2))
print(f"Максимальное  значение - {max(gg)}")
print(f"Минимальное значение - {min(gg)}")
#Задание 4
matrix = [
    [-446, 281, -80],
    [465, 432, -122],
    [13, 'error', 8]
    ]
summ = 0
for g in matrix:
    for i, mat in enumerate(g):
        if isinstance(mat, str):
            g[i] = len(mat)
        summ += g[i]
print("Сумма всех элементов матрицы: ", summ)
#Задание 5
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
x = matrix[0][0] + matrix[1][1] + matrix[2][2]
print(x)
