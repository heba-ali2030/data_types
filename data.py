# Write a python program that checks the number if its Even or Odd

# ask the user to write anumber
number =int(input('please choose any number from your mind : '))

# print(number/2)

# print(type(number/2))
print(number % 2)
# if number / 2 not give % print it is an even number
# if number/2 == 'classint'  :
#     print('The number you choosed is an even number')
if number % 2 == 0  :
    print('The number you choosed is an even number')

# # if number / 2 give % print it is an even number
else:
    print('The number you choosed is an odd number')





