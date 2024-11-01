def read_last(lines, file):
    if lines < 0 and not lines.isdigig():
     print('Задано не положительное натуральное число')
     return
    b = 0
    for i in range(0,lines+1):
        b = b+1
        last_lines = n - b
    for row in rows[lines:]:
        print (row)
f = r'H:\rhrthrh\home\text1.txt'   
lines = input('Введите количество последних выводимых строк:')
file = open(f, 'r', encoding='utf-8')
n = len(f.readlines())




