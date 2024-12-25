def f(s):
    digits = '0123456789'
    n = s.find(':')
    if n == -1:
        return (0,0)
    if n > 1 and n < len(s)-3:
        if s[n-1] in digits and s[n-2] in digits and s[n+1] in digits and s[n+2] in digits:
            if s[n+3] == ':' and s[n+4] in digits and s[n+5] in digits:
                return (n-2,8)
            else:
                return (n-2,5)
s = input('Введите строку: ')
while f(s) != (0,0):
    num, l = f(s)
    s = s[:num] + 'TBD' + s[num + l:]
print(s)




p = []
s = input('Введите строку: ')
abr = ''
for i in range(len(s)):
    if ord(s[i]) in range(1040,1072):
        abr += s[i]
    elif s[i] == ' ' and i < len(s)-1:
        if ord(s[i+1]) not in range(1040,1072):
            if len(abr) > 1:
                p.append(abr[1:])
                abr = ''
        else:
            abr += ' '
print(p)