import math
L = int(input('Введите длину маятника: '))
g = 9.81
T = 2 * math.pi * math.sqrt(L / g)
print(round(T, 2)) 