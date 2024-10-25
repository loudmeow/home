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

