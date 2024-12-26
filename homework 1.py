import math
r = float(input('Введите радиус окружности в сантиметрах: \n'))
s = round(math.pi*r*r, 2)
l = round(math.pi*r*2, 2)
print(f'Площадь окружности равна {s} сантиметров квадратных') 
print(f'Длина окружности равна {l} сантиметров') 




x=10
y=55
print("До замены:\nx =",x," \ny =",y)
c=x
x=y
y=c
print("После замены:\nx =",x, " \ny =",y)



import math
L = int(input('Введите длину маятника: '))
g = 9.81
T = 2 * math.pi * math.sqrt(L / g)
print(round(T, 2)) 