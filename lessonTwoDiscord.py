
# Keep in mind the conditions
# Things like True and False

print(5 > 2) # True
print(5 < 2) # False

print(5 == 2) # False
print(5 == 5) # True
print(5.0 == 5) # True
# ^Those are all booleans

# You can also assign True and False to a variable
bool1 = True
bool2 = False
print(type(bool1), type(bool2)) # Prints the type it is
peanut = "Peanut Butter" # String
eight = 8 # Integer
twenty = 20.0 # Float
print(type(peanut), type(eight), type(twenty))

#fake_bool1 = true # Error on line 22 "NameError: name 'true' is not defined"
#fake_bool2 = false

#print(type(fake_bool1), type(fake_bool2))
# ---------- ^^ Line 22, 23, and 25 don't work ^^ -------------- #

# Booleans are pretty much used in if/else statements

income = float(input("Please input your income in dollars:"))
if (income < 20000):
    print("You qualify for welfare")
else:
    print("You do not qualify for welfare at this time.")

print("Let's compare two integers.")
integer_X = float(input("Input integer 1: "))
integer_Y = float(input("Input integer 2: "))
if (integer_X > integer_Y):
    print(integer_X,"is greater than", integer_Y)
elif (integer_Y > integer_X):
    print(integer_Y, "is greater than", integer_X)
else:
    print(integer_X, "equals", integer_Y)

# Let's look at lists ----------------------
x = [1, 2, 3, 4, 5]
# ^ This is a list. What's inside the list are called elements
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])
# ^ Prints individual elements in the list
print(x)
# ^ Prints all the elements in the list

# This is a way to modify them
x[0] = "4" # The element in the 0 position changes to 4

# Lists don't have to have the same data types. 
y = ["Jeff", True, 1, 1.618] # You can have Strings, Bools, Int, and Floats in here
print(y)
# Calling upon an index that doesn't exist, it gives an error
#print(y[100000000]) # Error on line 65 "IndexError: list index out of range"
#print(y[15])

# We can use the len() function to tell the length of the list
print(len(x))
print(len(y)) # Note: The order of a list starts with 0, 1, 2, 3...etc.

z = [6, 5, 4] # Testing
print(z)

# The next thing that we're going to introduce are methods
# Methods use .METHODTHINGY() <-- They use a dot followed by
# the type of method that it uses. Like a function but it's 
# only for one object. (Only used for the thing that it's 
# going to affect) such as y.insert()

# Let's consider list's x and y.

y.insert(0, "Tom") # This would insert "Tom" at index 0
x.insert(3, 3.141) # This would insert 3.141 at index 3








