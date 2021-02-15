# write a python function that returns the division of 2 numbers
num1 =int(input('write the first number : '))
num2 =int(input('write the second number : '))

def number_division():
    result = num1/num2
    return result
print("The number division is", number_division())


#Write a python function that converts celsius to fehranheit and the opposite
celsius =int(input('what is weather temperature now in celsius : '))

fahrenheit = (celsius * 1.8) + 32  
print('%0.1f  Celsius is equal to %0.1f degree Fahrenheit'%(celsius,fahrenheit))


celsius = (fahrenheit - 32) / 1.8
print('%0.1f  Celsius is equal to %0.1f degree Fahrenheit'%(celsius,fahrenheit))