#Задание 1
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('matrix:')
for i in matrix:
    print(i)
x = []
y = 0
for z in matrix:
    for b in z:
        if b % 2 != 0:
            x.append(b)
        else:
            y += 1
print("Все нечётные числа matrix:\n", x)
print("Кол-во чётных чисел:\n", y)
#Задание 2
matrix_1 = [[2, 4, 3, 6], [5, 7, 1, 5]]
matrix_2 = [[2, 9, 0, 2], [3, 4, 7, 6]]
answer_matrix = [[0, 0, 0, 0], [0, 0, 0, 0]]
for i1 in range(len(matrix_1)):
    for i2 in range(len(matrix_2[0])):
        answer_matrix[i1][i2] = matrix_1[i1][i2] * matrix_2[i1][i2]
print(answer_matrix)
print(answer_matrix[0], "Сумма строки: ", answer_matrix[0][0] + answer_matrix[0][1] + answer_matrix[0][2] + answer_matrix[0][3])
print(answer_matrix[-1], "Сумма строки: ", answer_matrix[1][0] + answer_matrix[1][1] + answer_matrix[1][2] + answer_matrix[1][3])
#Задание 3
fruits = [['Banana', 'apple'], ['apricot', 'Avocado'], ['lime', 'lemon'], ['Mango', 'grapes']]
x = []
for i in fruits:
    for fruit in i:
        if fruit[0].isupper():
            x.append(fruit)
print(x)
#Задание 4
random_elements = [['toy', 'bee', 'cheese', 'ear'],
[False, 'word', '0110110', 10],
['happiness', '(」°ロ°)」', 'luck', None],
['car', '<- code ->', 4.7, True]]
for i in random_elements:
    for index, element in enumerate(i):
        if index % 2 == 0:
            print(f"Индекс: {index}, Элемент: {element}")
#Задание 5
x = int(input("Введите количество строк: "))
y = int(input("Введите количество столбцов: "))
matrix = []
for i in range(x):
    stroki = []
    for g in range(y):
        p = int(input(f"Введите значение элемента [{i}][{g}]:"))
        stroki.append(p)
    matrix.append(stroki)
print("Ваша матрица:")
for stroki in matrix:
    print(stroki)
