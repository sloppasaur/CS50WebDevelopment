# this file explores sets in Python:

s = set()

# add elements to the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)

print(s)

# 3 will not show up since each value wil be unique and will only appear once
s.add(3)
print(s)

s.remove(2)
print(s)

# print the elments of the list:
print(f"This set has {len(s)} elements")