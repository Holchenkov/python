import random, time, sys

def loading():
    print("Загрузка", end="")
    for i in range(5):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\nГотово!\n")


def finish_figure(figure):
    print("Должна получиться такая фигура:")
    for i in figure:
        print("".join(i))
    print()


def print_current_figure(figure):
    for i in figure:
        print("".join(i))
    print()


def generate_figure(elements):
    return [
        [random.choice(elements), random.choice(elements)],
        [random.choice(elements), random.choice(elements)]
    ]

def is_figure_complete(current, target):
    return current == target

def main():
    figure1 = [
        ["┏", "┓"],
        ["┗", "┛"]
    ]
    elements1 = ["┏", "┓", "┗", "┛"]

    figure2 = [
        ["╭", "╮"],
        ["╰", "╯"]
    ]
    elements2 = ["╭", "╮", "╰", "╯"]

    chosen = random.choice([1, 2])
    if chosen == 1:
        target_figure = figure1
        elements = elements1
    else:
        target_figure = figure2
        elements = elements2

    loading()

    finish_figure(target_figure)

    current_figure = generate_figure(elements)
    print("С помощью кнопок 1,2,3,4 меняйте направление элементов фигуры.")
    print_current_figure(current_figure)

    while not is_figure_complete(current_figure, target_figure):
        choice = input("> ").strip().lower()

        if choice in ['1', '2', '3', '4']:
            index = int(choice)

            pos_map = {1: (0, 0), 2: (0, 1), 3: (1, 0), 4: (1, 1)}
            r, c = pos_map[index]
            current_figure[r][c] = random.choice(elements)

            print_current_figure(current_figure)
        else:
            print("Неверный ввод. Попробуйте снова.")

    print("Ура! У тебя получилось!")
    print_current_figure(current_figure)

if __name__ == "__main__":
    main()
