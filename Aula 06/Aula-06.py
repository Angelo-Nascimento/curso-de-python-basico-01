# Aula 06
# Tipos primitivos
# OS 4 tipos primitivos mais básicos: int, float, bool e str
print('')
print('-----Sum of integer values-----')
num01 = int(input('Enter the first number: '))
num02 = int(input('Enter the second number: '))
sum = num01 + num02
print('The sum of {} + {} = {}'.format(num01, num02, sum))
print('')

print('----Sum of real values----')
Num01 = float(input('Enter the first floating point number: '))
Num02 = float(input('Enter the second floating point number: '))
Sum = Num01 + Num02
print('The sum of {} + {} = {}' .format(Num01, Num02, Sum))
print('')

print('----Putting words together----')
print('What is your first name?')
firstName = str(input('Type here: '))
print('What is your last name?')
lastName = str(input('Type here: '))
completeName = firstName + ' ' + lastName
print('Your first name is {} and your last name is {}. Your complete name is {}' .format(firstName, lastName, completeName))
print('')

print('----Field verification----')
value = bool(input('Enter something here: '))
print('Has the field been filled in?')
print('Result: {}'.format(value))
