# Dissecting this from the book. 
# Lines 8,9 are prompts asking the user a question. 
# Line 10 is when the user is presented with an opportunity to input their name.
# Line 11 is a greeting. Line 12 asks for the users name. Line 13 prompts that user to enter their age.
# Since we can't at integers and strings, we need to convert the string onto a number. 
# ^ We can do this since the user inputed a number.
# Wait let me test something
print('Hello, world!')
print('What is you name?')
myName = input() #Note: Also counts spaces.
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')


# Testing
print(myAge) #outputs the variable itself. (I just put it here as the control var)
print(int(myAge)) #counts the actual value
print(len(myAge)) #counts... entities? so ex. 20 would equal as 2 for length. 
                    #Interesting.
# O I didn't get a chance to test with str()
print(str(myAge))

# Let's test it with string values.
print(myName) # Ouput variable
#print(int(myName)) # *Error* "ValueError: invalid literal for int() with base 10: 'Adrian '"
print(len(myName)) # Ouput 6. Counted the length of the string in the var.
print(str(myName)) # Almost literally like the normal variable output
