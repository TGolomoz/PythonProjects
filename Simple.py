# Создать функцию, которая прибавляет элементы числа между собой.
# Например, есть число 123. Попав в нашу функцию, должно произойти
# следующее: 1 + 2 + 3 = 6.
# Результат суммирования - в консоль.
import re

number = str(input('Input a number\n'))

if not re.match("^[0-9]+$", number):
    print('You can input only numbers!')
else:
    result = 0
    count = len(number)
    while count > 0:
        result += int(number[count-1])
        count -= 1
    print('The result is ' + str(result))

