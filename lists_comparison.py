#Необходимо написать функцию, которая будет брать два случайно сгенерированных списка (задача №7)
# и сравнивать их между собой. Уникальные числа (которые есть только в одном списке)
# выводить в консоль с любым комментарием.
import random
length = int(input('Input a list length\n'))
minimum_value = 0
maximum_value = 0
my_first_list = []
my_second_list = []
result_list = []

def inputValues():
    global minimum_value
    minimum_value = int(input('Input a list minimum value\n'))
    global maximum_value
    maximum_value = int(input('Input a list maximum value\n'))

def finding (first_list, second_list):
    third_list = []
    for i in range(len(second_list)):
        if not first_list.__contains__(second_list[i]):
            third_list.append(second_list[i])
    return third_list

def append_to_result (first_list, second_list, result_list):
    temp_list = []
    temp_list = finding(first_list, second_list)
    for i in range(len(temp_list)):
        result_list.append(temp_list[i])

inputValues()

while(maximum_value < minimum_value):
    print('Maximum value should be greater than minimum value')
    inputValues()
for i in range(length):
    my_first_list.append(random.randint(minimum_value,maximum_value))
    my_second_list.append(random.randint(minimum_value,maximum_value))
print(my_first_list)
print(my_second_list)

append_to_result(my_first_list, my_second_list, result_list)
append_to_result(my_second_list, my_first_list, result_list)

print ('The result is ' + str(set(result_list)))