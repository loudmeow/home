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




for i in range(1, 10):
    for j in range(1, 10):
        print(i, "*", j, "=", i * j, end='\t')