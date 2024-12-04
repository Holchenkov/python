def time_to_travel_around_planet(robot_speed,planet_diameter):
    if robot_speed <= 0 or planet_diameter <= 0:
        return "Скорость и диаметр должны быть положительными числами!"
    time = 3.14159 * planet_diameter / robot_speed
    return time

calculation_1 = time_to_travel_around_planet(3, 18)
print(f"Роботу необходимо {calculation_1:.2f} часов, чтобы объехать вокруг планеты.")
