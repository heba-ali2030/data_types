# Write a python function that takes a number as a parameter and returns number's square..
# Also check if there is a built in function that does the  same

# number=int(input('Choose a number: '))
# 1- using the power operator**
# print(number**2)

# # 2- multiply the number in itself
# print(number*number)
 
#  # 3- using the power built in function
# print(number.__pow__(2))

#  using function
# def num_square():
#     return(number**2)

# print(num_square)
# using function
# name= input('what is your name? ')
# def greet(name):
    
# print('hello'+' '+ name +' '+'how are you?') 

# def num_square(number):
    
#     print(number.pow(2))

# num_square(number)

Num= int(input('Choose a number: '))
def number_square(Num):
   result = Num**2
   return result



print("The number square is", number_square(Num))