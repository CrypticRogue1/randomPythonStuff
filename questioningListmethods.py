
# Testing to see hos .insert() and .remove() affect the list
# Connect to lessonTwoDiscord.py

y = [0, 1, 2, 3, 4]
x = [0, 1, 2, 3, 4]

print(y)
print(x)

y.insert(0, "This is index zero") # This pushes things to the right. Saying that it literally inserts it onto index 0
x.insert(4, "This is index 4") # Literally inserts at index 4

print(y)
print(x)

y.remove(2) # Literally removes index 2 from y
x.remove(2) # Literally removes index 2 from x

print(y)
print(x)



