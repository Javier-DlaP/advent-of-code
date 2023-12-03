import math
import numpy as np

# Read the file
matrix = []
with open('input.txt', 'r') as file:
    # Read the contents of the file as a matrix
    for line in file.readlines():
        line = list(line[:-1])
        matrix.append([None if char != '*' and not char.isdigit() else char for char in line])
matrix = np.array(matrix)


def locate_symbols(matrix: np.array) -> (np.array, list):
    list_symbols = []
    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            if elem == '*' and not elem.isdigit():
                list_symbols.append((i, j))
                matrix[i, j] = None
    return matrix, list_symbols


def mul_numbers_symbol(matrix: np.array, symbols_pos: tuple) -> (np.array, int):
    numbers = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            num_pos = (i + symbols_pos[0], j + symbols_pos[1])
            if matrix[num_pos] is not None:
                row, number = get_number(matrix[num_pos[0]], num_pos[1])
                numbers.append(number)
                matrix[num_pos[0]] = row
    total = 0
    if len(numbers) == 2:
        total = math.prod(numbers)
    return matrix, total


def get_number(row: np.array, j: int) -> (np.array, int):
    number = []
    number.append(row[j])
    row[j] = None
    tmp_j = j
    while tmp_j - 1 >= 0 and row[tmp_j - 1] is not None:
        number.insert(0, row[tmp_j - 1])
        tmp_j -= 1
        row[tmp_j] = None
    tmp_j = j
    while tmp_j + 1 < len(row) and row[tmp_j + 1] is not None:
        number.append(row[tmp_j + 1])
        tmp_j += 1
        row[tmp_j] = None
    number = int(''.join(number))
    return row, number


matrix, list_symbols = locate_symbols(matrix)
total = 0
for symbol in list_symbols:
    matrix, partial_sum = mul_numbers_symbol(matrix, symbol)
    total += partial_sum
print(total)
