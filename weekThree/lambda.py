people = [
    {"name" : "Harry", "house": "Gryffindor"},
    {"name" : "Cho", "house" : "Ravenclaw"},
    {"name" : "Draco", "house" : "Slytherin"}
]

# people.sort wouldn't work

# def f(person):
#     return person["house"]
# people.sort(key=f)

people.sort(key=lambda person: person["name"])


print(people)