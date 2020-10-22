file1 = open('test1.txt').read().split('\n')
file2 = open('test2.txt').read().split('\n')
file1.extend(file2)
 
result = open('test1.txt', 'a')
for i in file2:
    result.write(i)
result.close()
