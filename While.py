#Необходимо написать функцию с тремя аргументами (А, Б и В), которая будет делать следующее:
#Сравнивать аргументы А и Б, если А меньше Б, то увеличивать на инкремент В (прибавлять А к В)
#Полученный результат повторно сравнивать с Б, если все еще меньше Б - повторить предыдущий шаг
#Когда А станет больше Б, вывести радостное сообщение в консоль
#Вся история сравнений также выводится в консоль
a = int(input ('Input the first number\n'))
b = int(input ('Input the second number\n'))
c = int(input ('Input the third number\n'))
while a <= b:
  if a < b:
    print(str(a) + ' < ' + str(b))
  else: print(str(a) + ' = ' + str(b))
  a = a + c

print('Congratilation:')
print(str(a) + ' > ' + str(b))