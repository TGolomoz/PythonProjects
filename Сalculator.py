first_number = float(input('Input first number\n'))
second_number = float(input('Input second number\n'))
operation = input('Select the operation (+, -, *, /)\n')

def addition (first_number, second_number):
  return first_number + second_number

def subtraction (first_number, second_number):
  return first_number - second_number

def multiplication (first_number, second_number):
  return first_number * second_number

def division (first_number, second_number):
  if second_number == 0:
    return 'Division by zero is prohibited'
  else:
    return first_number / second_number

if operation == '+':
  print('Result >>> ', addition(first_number, second_number))
elif operation == '-':
  print('Result >>> ', subtraction(first_number, second_number))
elif operation == '*':
  print('Result >>> ', multiplication(first_number, second_number))
elif operation == '/':
  print('Result >>> ', division(first_number, second_number))
else:
  print('Wrong operation')
