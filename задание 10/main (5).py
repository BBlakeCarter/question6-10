file = open('b9k.txt' , 'r')

file_list = file.readlines() 
k = int(input('Введите номер К: '))
file_list.insert(k , '\n')

result = open('b9k.txt', 'w')
for i in file_list:
  result.write(i)
result.close()