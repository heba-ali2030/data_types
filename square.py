# Write a python function that takes a number as a parameter and returns number's square..
# Also check if there is a built in function that does the  same

number=int(input('Choose a number: '))
# 1- using the power operator**
print(number**2)

 # 2- multiply the number in itself
print(number*number)
 
 # 3- using the power built in function
print(number.__pow__(2))

# 4- using a def function
def number_square(number):
   result = number**2
   return result
print("The number square is", number_square(number))