### Types of variables ###

string = "this is a string"
integer = 12
float_double = 12.2 #The float in python is also a double which means that u don't need to specify
string_with_float = "this is a string with the number 12.2"   #the number will not change
my_boolean = True #could be False also
my_complex = 1 + 1j

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Starts here: ')

print(string)
print(integer)
print(float_double)
print(string_with_float)
print(my_boolean)
print(my_complex)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
## see the type of a variable

print(type(string))
print(type(integer))
print(type(float_double))
print(type(string_with_float)) #this will show as str but it include a float which could be integer
print(type(my_boolean))
print(type(my_complex))

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
## Adding variables ##
print(string + ", " + string_with_float)
print(integer + float_double) # It can be because python is dynamic typed
print(my_boolean - False) #This could be some difficult to understand
print(my_complex + 1j) #this is some math advance operation

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

## Variables in one code line

name, surname, age, email = "santiago", "beltran", 19, "sanfer851@gmail.com"
print(name, surname, age, email)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

## Operations with variables
# usually the operations going in this order = name_of_variable.operation

print(string.count("s")) #count the number of date which we gave into the variable
print(len(string)) # this count the lenght of all the variable starting in 1
print(string.capitalize()) #capitalize the first character
print(string.upper()) #Make the whole sentence mayus
print(string.islower()) #Tell us if the variable is lower, if not it will be False
print(string.join("hi")) #This will introduce the string which we gave into any part of the variable

print(integer + 1) #add
print(integer - 1) #substract
print(integer / 4) #division
print(integer * 2) #mult
print(integer // 5) #module

#you can see more in this channel (is not mine) https://www.youtube.com/watch?v=cQT33yu9pY8