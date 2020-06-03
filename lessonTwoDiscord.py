
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

# We can also remove
x.remove(3)
print(x)

# What about this?
# x.remove("Jeff") # What would happen? You would get this error message [shown below]
# "ValueError: list.remove(x): x not in list"


# Not sure how this next method works but supposedly it does.
# Let's remove the las element of the list
# Index "IndexError: pop index out of range"-->popped_item = x.pop(5) # <-- I'm not sure if that actually is
#print(x)                        # the element or the idex. I'm thinking
#print(popped_item)                        # it probably is the element


# You can also delete stuff using  del()
print(x)
#del(x) # <-- I'm not so sure why this is red. Gonna test.
# ^ The line above gives me the error code "NameError: name 'x' is not defined"
print(x)
#^ Even though when I print it, it displays the whole arr- list. It displays the list.

# It's actually pretty easy to sort a list. You just use the .sort() method and
z = [1,34,52,2,6,8,234,7,4,2,4,6,3,4]
print(z)
z.sort()
print(z)
#^ Just tested on the shell and it sorted it nicely
# You can also do it so it does the reverse.
z.reverse()
print(z)
# To add something to a list, just use the method, .append()
# to add something to the end of the list.
z.append("Hi there!")
print(z)
count = z.count(1) # <-- to count the number 1 in the list z
print(count) # <-- simply displays the line above
# Interestingly enough. You can add arrays into a single list
1_1 = [1, 2, 3, 4, 5]
1_2 = [6, 7, 8, 9, 10]
print(1_1 + 1_2) # <-- Will print both of them out.

# Let's take a look at Tuples
# not gonna lie, a bit confusing at first since I've never used them



# Tuples are like lists
# The only difference is:
# Tuples CANNOT be changed.
my_tuple = (1, 3)
my_tuple2 = (2, 4, 6)
my_tuple3 = (1, True, "Jeff", 3.1415)
# These are examples of tuples
print(my_tuple, my_tuple2, my_tuple3)
print(my_tuple[0])
print(my_tuple2[1])
print(my_tuple3[2])


# As you might have noticed. A way to differentiate from tuples and lists
# are it's syntax. 
# Lists use --> LIST_NAME = [] 
# Tuples use --> TUPLE_NAME = ()

# Would give an error --> my_tuple[0] = 100
my_tuple3.count("Jeff")
len(my_tuple)
del(my_tuple)
x = (1, 2, 3, 4)
y = (5, 6, 7, 8, 8, 10)
z = x + y
print(z)
# These are things you could do with a tuple




