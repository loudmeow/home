#a = input('Введите текст:')
#с = a.replace('н', '!')
#b = a.count('нн')
#print(с)
#print(b)



a = input('Введите текст:')
i = 0
while a[i] != '(':
    i += 1
i += 1
while a[i] != ')':
    print(a[i], end='')
    i += 1

