#WORK 1
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


#WORK 2
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

#WORK 3
a = input('Введите номер месяца:')
if a.isdigit():
    a = int(a)
    if a<=12 and a>=1:
      if a>=3 and a<=5:
        print('Время года: Весна')
      if a>=6 and a<=8:
        print('Время года: Лето')
      if a>=9 and a<=11:
        print('Время года: Осень')
      if a>=1 and a<=2 or a ==12:
        print('Время года: Зима')
    else:
      print('Введён не корректный номер месяца')
if a==1:
  print('Месяц: Январь')
if a==2:
  print('Месяц: Февраль')
if a==3:
  print('Месяц: Март')
if a==4:
  print('Месяц: Апрель')
if a==5:
  print('Месяц: Май')
if a==6:
  print('Месяц: Июнь')
if a==7:
  print('Месяц: Июль')
if a==8:
  print('Месяц: Август')
if a==9:
  print('Месяц: Сентябрь')
if a==10:
  print('Месяц: Октябрь')
if a==11:
  print('Месяц: Ноябрь')
if a==12:
  print('Месяц: Декабрь')
    


 