import random
print('Количество строк не должно совпадать с количеством столбцов')
a = input('Введите количество столбцов:')
b = input('Введите количество строк:')
a = int(a)
b = int(b)
arr = [[random.randint(-50,50) for i in range(a)] for j in range(b)]
print(arr)
if a == b :
    print('Количество столбцов и строк совпадает')
else:
    maxsimum=[0]*b
    for i in range (a): maxsimum[i]=sum(arr[i])
    print (f'Строка с максимальной суммой {maxsimum.index(max(maxsimum))+1},сумма:{max(maxsimum)}')
    print (f'Строка с минимальной суммой {maxsimum.index(min(maxsimum))+1}, сумма:{min(maxsimum)}')





def replace_min_elements(matrix):
    new_matrix = []
    for row in matrix:
        min_value = min(row)
        min_index = row.index(min_value)
        new_row = row[:]
        if min_value % 2 == 0:
            new_row[min_index] = 0
        else:
            new_row[min_index] = 1
        new_matrix.append(new_row)
    return new_matrix
n = 4
m = 5 
matrix = [
    [5, 3, 9, 1, 7],
    [12, 4, 6, 8, 10],
    [13, 15, 11, 2, 14],
    [20, 17, 19, 16, 18]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

new_matrix = replace_min_elements(matrix)

print("\nНовая матрица:")
for row in new_matrix:
    print(row)



