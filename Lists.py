#Необходимо создать функцию, которая будет генерировать список (list) самостоятельно в псевдослучайном порядке.
#Функция должна обладать аргументами, которые будут ограничивать длину списка, а также максимальное цифровое значение элементов этого списка.
#Например:Сгенерировать список из 10 чисел, каждое из которых может быть в диапазоне от 1 до 9.
import random
length = int(input('Input a list length\n'))
minimum_value = 0
maximum_value = 0
my_list = []

def inputValues():
    global minimum_value
    minimum_value = int(input('Input a list minimum value\n'))
    global maximum_value
    maximum_value = int(input('Input a list maximum value\n'))

inputValues()

while(maximum_value < minimum_value):
    print('Maximum value should be greater than minimum value')
    inputValues()
for i in range(length):
    my_list.append(random.randint(minimum_value,maximum_value))
print(my_list)
