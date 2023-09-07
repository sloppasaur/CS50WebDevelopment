# This file uses an if statement to be an example of boolean:

num = int(input("Number: ")) # keep in mind that the int is required to make the input an int indstead of string.

# if num > 0, print that nums is positive
if (num > 0):
    print(f'{num} is positive')
elif (num < 0):
    print(f'{num} is less than zero')
else:
    print(f'{num} is indeed zero')