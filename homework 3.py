a = input('Введите натуральное число от 2 до 100:')
b = 1
sum = 1
if  a.isdigit() :
    a = int(a)
    if a <= 100 and a > b:
        while b<a:
            b += 1
            c = b**3
            sum += c
        print(f'{sum}')
else:
    print('Неправильно введено число')
