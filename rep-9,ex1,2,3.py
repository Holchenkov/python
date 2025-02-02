#Задание 1
class Create_Personage:

    def __init__(self, name, class_pr, hp, dps):
        self.name = name
        self.class_pr = class_pr
        self.hp = hp
        self.dps = dps
    def show_info(self):
        print(f"Имя: {self.name}\nКласс: {self.class_pr}\nЖизни: {self.hp}\nУрон: {self.dps}")
        print()
    def go_on_a_trip(self):
        print("Ваш персонаж отправился в путешестие.")
        print()
    def go_back(self):
        print("Ваш персонаж возвращается обратно.")
        print()
    def start_training(self):
        self.dps += 2
        print("Вы начали тренировку. Тренировка повысила ваш урон.")
        print()
    def start_the_battle(self):
        print("Ваш персонаж готовится к битве.")
        print(f"Текущие характеристики:\nЖизни: {self.hp}\nУрон: {self.dps}")
      
pers_1 = Create_Personage("Боря", "Маг", 100, 16)
pers_1.show_info()
pers_1.go_on_a_trip()
pers_1.go_back()
pers_1.start_training()
pers_1.show_info()
pers_1.start_the_battle()
#Задание №2
class Room:
    items = []
    another_room = items

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def print_items(self):
        print(f"Все предметы в комнате {self.name}: {', '.join(self.items)}")

    def add_item(self, *item):
        self.items.extend(item)

    def del_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Все предметы в комнате: {', '.join(self.items)}")
        else:
            print("Такого предмета нет в комнате.")

#Выбрал второй вариант

    def rename_room(self, new_name):
        self.name = new_name

    def describe_room(self):
        print(f"Описание комнаты: имя комнаты - {self.name}, список предметов в комнате - {', '.join(self.items)}")

    def merge_rooms(self, another_room):
        print(f"Содержимое двух комнат: {', '.join(self.another_room)}")

    def is_empty(self):
        if len(self.items) == 0:
            print("Комната пуста")
        else:
            print("Комната не пуста")

    def get_room_size(self):
        print(f"Площадь {self.name} - {self.size}")

room1 = Room("Кухня", 50)
room1.add_item("Холодильник", "Стул", "Стол")
room1.print_items()
room1.del_item("Стул")
room1.rename_room("Спальня")
room1.describe_room()
room2 = Room("Туалет", 15)
room2.add_item("Унитаз", "Туалетная бумага")
room2.merge_rooms("Туалет")
room1.is_empty()
room2.is_empty()
room1.get_room_size()
room2.get_room_size()
#Задание 3
class Car:

    def __init__(self, marca, model, probeg, god_vipuska):
        self.marca = marca
        self.model = model
        self.probeg = probeg
        self.god_vipuska = god_vipuska
    def print_info(self):
        print(f"Марка автомобиля - {self.marca}\nМодель автомобиля - {self.model}\nПробег - {self.probeg}\nГод выпуска - {self.god_vipuska}")
        print()

    def updated_probeg(self, new_probeg):
        if new_probeg > 0:
            self.probeg = new_probeg
        print(f'Обновленный пробег - {self.probeg}')
        print()

    def proverka(self):
        if self.probeg < 10000:
            print("Автомобиль новый, так как пробег меньше 10000 км.")
            print()
        else:
            print("Автомобиль старый, так как пробег больше 10000 км.")
            print()


car_1 = Car("Honda", "Urus", 7000, 2008)
car_1.print_info()
car_1.updated_probeg(6000)
car_1.proverka()
car_2 = Car("Laga", "2107", 18000, 1970)
car_2.print_info()
car_2.updated_probeg(24000)
car_2.proverka() 
