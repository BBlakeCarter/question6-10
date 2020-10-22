first = open('test1.txt')
second = open('test2.txt')
data = first.read() + '\n' + second.read()
file = open('test1.txt', 'w')
file.write(data)
file.close