first_number = float(input('Input first number\n'))
second_number = float(input('Input second number\n'))

def compare_to (first_number, second_number):
  if first_number > second_number:
    return 'Successfully'
  elif first_number == second_number:
    return 'Almost'
  elif first_number < second_number:
   return 'Loser'

print('Result >>> ', compare_to(first_number, second_number))