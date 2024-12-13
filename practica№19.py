import webbrowser, urllib.request

print("Проверка подключения к интернету... ")
try:
    urllib.request.urlopen("http://google.com")
except IOError:
    print(f"Соединения не установлено\nПроверьте подключение к интеренету.")
else:
    print("Соединение стабильно")
    vvod1 = input("Введите запрос: ")
    while True:
        print(f"Выбор браузера для поиска\n [1] - Google, [2] - Яндекс.")
        vvod2 = int(input(">"))
        if vvod2 == 1:
            webbrowser.open('https://www.google.ru/search?q=' + vvod1)
        elif vvod2 == 2:
            webbrowser.open('https://ya.ru/search/?text=' + vvod1)
        else:
            print("Выберите из предложенных вариантов.")
