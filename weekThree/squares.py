# This program practices importing files 

from functions import square

'''
If you import the functions profile, you'd have to rewrite the code like this:

for i in range (10):
    print(f"the square of {i} is {functions.square(i)})
'''

for i in range(10):
    print(f"the square of {i} is {square(i)}")