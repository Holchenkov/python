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
