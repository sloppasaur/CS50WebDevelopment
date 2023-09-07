# this program looks at OOP in Python

class Point():
    def __init__(self, input1, input2): # self represents the object in question
        self.x = input1
        self.y = input2

'''
p = Point(2, 8)
print(p.x)
print(p.y)
'''

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # Here are some internal functions for the class flight:
    def addPassenger(self, name):
        if not self.openSeats():
            return False 

        self.passengers.append(name)
        return True

    def openSeats(self): # Returns the open seats on a plane
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]

for person in people:
    #success = flight.addPassenger(person)
    #if success:
    if flight.addPassenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"no available seats for {person}")
