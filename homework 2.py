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



a = float(input('Введите стоимость товаров:'))
if a>20:
    c = a//0.65
    k = (a%0.65)
    d = round(k*100, 0)
    print(f'Стоимоть покупок с учётом скидки в 35% равна: {c} рублей {d} копеек')
else:
    g = a//1
    h = a%1
    l = round(h*100, 0)
    print(f'Скидки нет. Окончательная стоимость покупок равна: {g} рублей {h} копеек')


 
