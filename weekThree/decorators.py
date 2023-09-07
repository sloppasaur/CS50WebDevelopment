# This program looks at functional programming in python:

def announce(f): # announce is the decorator
    def wrapper(): # called a wrapper function
        print("About to run the function...")
        f()
        print("Done with function")
    return wrapper

@announce
def hello():
    print("Hello, world!")


hello()