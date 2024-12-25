string = str(input())
n_count = 0
n_count_max = 0
for i in string:
    if i == 'н':
        n_count += 1
    else:
        if n_count_max < n_count:
            n_count_max = n_count
        n_count = 0
stirng = string.replace('н', '!')
print(n_count_max)
print(stirng)



a = input('Введите текст:')
i = 0
while a[i] != '(':
    i += 1
i += 1
while a[i] != ')':
    print(a[i], end='')
    i += 1




text = str(input())
for i in text.split():
    if(i.startswith("а") or i.endswith("я")):
        print(i)