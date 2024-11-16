notebook = {}
print("[1] - Создать новую заметку. [2] - Показать все заметки. [3] - Удалить запись. [4] - Выход.")
while True:
    x = input("Введите что вы хотите сделать: ")
    if x == "1":
        k = input('Введите заголовок: ')
        v = input('Введите текст: ')
        notebook[k] = v
    elif x == "2":
        print(", ".join(notebook.keys()))
        if len(notebook.keys()) < 1:
            print("Заметок нет.")
        note = input("Какую заметку открыть? ")
        if note in notebook.keys():
            print(notebook[note])
        else:
            print("Такой заметки нет.")
    elif x == "3":
        print(", ".join(notebook.keys()))
        delete = input("Какую заметку удалить? ")
        if delete not in notebook.keys():
            print("Такой заметки нет.")
        elif delete in notebook.keys():
            notebook.pop(delete)
            print(f"Заметка {delete} удалена")
    elif x == "4":
        break
    else:
        print("Введите значение заново")
