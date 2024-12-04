def time_to_travel_around_planet(robot_speed,planet_diameter):
    if robot_speed <= 0 or planet_diameter <= 0:
        return "Скорость и диаметр должны быть положительными числами!"
    time = 3.14159 * b / a
    return time

a = int(input("Введите скорость робота: "))
b = int(input("Введите диаметр планеты: "))

calculation_1 = time_to_travel_around_planet(a, b)
print(f"Роботу необходимо {calculation_1:.2f} часов, чтобы объехать вокруг планеты.")
