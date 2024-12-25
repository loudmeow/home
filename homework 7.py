
def read_last(lines, f):
    if lines < 0 and not lines.isdigig():
     print('Задано не положительное натуральное число')
     return
    b = 0
    for i in range(0,lines+1):
        b = b+1
        last_lines = n - b
    for row in rows[last_lines:]:
        print (rows)
f = open('text1.txt', encoding = 'utf-8' )   
lines = input('Введите количество последних выводимых строк:')
n = len(f.readlines())




