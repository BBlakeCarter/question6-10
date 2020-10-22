file = open('b9k.txt').read().split('\n')
s = (input('Введите строку S: '))
file.insert(0, s)

result = open('b9k.txt', 'w')
for i in file:
    result.write(i)
result.close()
