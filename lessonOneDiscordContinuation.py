# Lecture 1 continued notes --> Listing 8 on Lecture 1 notes
            ###Listing 8
peeps1, peeps2 = (3,4)  #In python, this is called a Tuple 
# ^ A Tuple is something where you store and unpack information- as far as I know.

print(peeps1 + peeps2)

# peeps1 and peeps2 are variables, so we can also use them like variables
peeps3 = peeps1 + peeps2
print(peeps3)

peeps1, peeps2 = "3", "4"
print(peeps1 + peeps2) #Should print 34 since we didn't say we wanted a space
print(peeps1, peeps2) #Should print 3 4 since we used , <-- a separator

            ###Listing 9 - Long strings

longest_String = """The quick brown
fox jumped 
over
the lazy
dog.""" # <-- Using three quotation marks """ would make it so that your string could span lines and lines and lines and lines and line of code. Many lines
print(longest_String)
            ### Listing 10 - Problem

# Let's find the solution of these numbers with the Distance Formula

x1, y1 = 5,3
x2, y2 = 4,5
# Remember: Distance Formula --> ((x2-x1)**2 + (y2-y1)**2)**1/2
print(((x2-x1)**2+(y2-y1)**2)**1/2)

# ^ Just to show that you can also put formulas on here.
# They're just gonna look- well seem a bit iffy. 

            ### Listing 11 - Solution

first_name = "Jeff"
last_name = "Bezos"
print("Hey there", first_name, last_name) 
# ^ Will print "Hey thre Jeff Bezos" <-- Remember, "," means separate BUT it doesn't mean we shouldn't use the "+"

            ### Listing 12 - Taking Input from user

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
age = input("Please input your age: ")

print("Hey there", first_name, last_name)
print("You are", age, "years old.")

            ### Listing 13 - Task: Simple Email Creator

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

print("Your email is:", first_name + last_name + "@gmail.com")

            ### Listing 14 - Experimental Inputs

n1 = input("Please enter a number: ")
n2 = input("Please anter another number: ")

print(n1-n2) # <-- This would fail because it took the input as a string

            ### Listing 15 - Built-in Type Function

# We can interpret the type of n1 and n2 if we use the type() function

print(type(n1)) # <-- These should both be strings
print(type(n2))   # <-- String

            ### Listing 16 - Parsing Strings as Integers

# We can force a string to look like an integer if it kind of already loos like a number
n1 = int(input("Please enter a number: ")) # <-- interprets the input as an int instead of a str
n2 = int(input("Please enter another number: "))
print(n1-n2)

            ### Task: Tane an Age and Add 4

# Ask the user for their age and add 4 to it, print this pack to them
# Remember you can use the interactive python shell to test snipets of code.
userAge = int(input("Please enter your age: "))
print(userAge + 4)
userOldAge = userAge + 4
print("You'll be", userOldAge, "in 4 years. Congrats!")