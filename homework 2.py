a = input('Ведите первое число:')
b = input('Ведите второе число:')
if not a.isdigit() or not b.isdigit():
    print('Вводи числа')
else:
    a, b = map(float, (a, b))
    if b == 0:
        print('Второе число не может равняться нулю!')
    else:
        c = round(a/b, 4)
        print(f'Деление первого числа на втрое равно: {c}')



