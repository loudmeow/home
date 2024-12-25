import math
def formula(x, y):
    return round((x*x)/((math.sqrt(x**2 + y**2))*(math.sqrt(x**2))), 3)
def vektor(x, y):
    return (f'({x};{y})')
def koordinata():
    while True:
        try:
            koordinats = list(map(float, input('Введите координаты точки через пробел (x y): ').split()))
            if len(koordinats) != 2:
                print('Ошибка: нужно ввести две координаты')
                continue
            x, y = koordinats
            return x, y
        except ValueError:
            print('Ошибка: введите корректные числа.')
areas = []
areas2 = []
for i in range(1,4):
    print(f'Введите координаты {i}-ой точки: ')
    x, y = koordinata()
    areas2.append(vektor(x, y))
    areas.append(formula(x, y))
if areas[0] > areas[1] and areas[0] > areas[2] :
  print((f'Координаты 1-го вектора: {areas2[0]}'))
  print((f'Косинус угла между осью абцис и первым вектором равен: {areas[0]}'))
elif areas[1] > areas[0] and areas[1] > areas[2]:
    print((f'Координаты 2-го вектора: {areas2[1]}'))
    print((f'Косинус угла между осью абцис и вторым вектором равен: {areas[1]}'))
else:
      print((f'Координаты 3-го вектора: {areas2[2]}'))
      print((f'Косинус угла между осью абцис и третьим вектором равен: {areas[2]}'))

x = input('Введите предел:')
x = int(x)
b = 0
for i in range(b, x):
    while b <= x:
        b = str(b)
        if b == b[::-1]:
            print(f'{b}')
        b = int(b)
        b = b + 1
    break
