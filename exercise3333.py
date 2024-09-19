import math
g = 9,81
l = float(input('Введите длину маятника в метрах: \n'))
h = l/g
t = round(2*math.pi*(math.sqrt(h)), 2)
print(f'Период колебания мятника равен {t} ')      