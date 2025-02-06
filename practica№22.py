class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = {100: True, 101: True, 102: True, 103: True,
                      200: True, 201: True, 202: True, 203: True}

    def print_rooms(self):
        print(f"Отель:{self.name}")
        for i, g in self.rooms.items():
            if g == True:
                print(f"Номер № {i} свободен")
            else:
                print(f"Номер № {i} занят")

    def book_room_by_number(self, number):
        if number in self.rooms:
            if self.rooms[number] == True:
                self.rooms[number] = False
                print(f"Комната {number} забронирована")
            else:
                print(f"Номер {number} уже занят")
        else:
            print("Ошибка! Такого номера нет.")

    def finish_number_by_number(self, number):
        if number in self.rooms:
            if self.rooms[number] == False:
                self.rooms[number] = True
                print(f"\nКомната {number} разбронирована")
            else:
                print(f"Номер {number} не занят")
        else:
            print(f"Ошибка! Такого номера нет.\nНомер {number} не забронирован. ")

hotel = Hotel(" У Олега")
while True:
    input_bro = input("[1] - Вывести занятость всех номеров\n[2] - Занять номер\n[3] - Снять бронь с номера\n[4] - Выход\n>")
    if input_bro == "1":
        hotel.print_rooms()
    elif input_bro == "2":
        hotel.book_room_by_number(int(input("Введите номер для брони: ")))
    elif input_bro == "3":
        hotel.finish_number_by_number(int(input("Введите номер для снятия брони: ")))
    elif input_bro == "4":
        break
    else:
        print("Неверный ввод")
