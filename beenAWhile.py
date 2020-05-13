
Num1 = 8
Num2 = 12
Name1 = 'Adrian'
Name2 = 'Cryptic'
# Initially I put this up here "uniChoice = input()" but I noticed that I need to initialize it the instant I need it


print("Well then... It's been a while hasn't it?")
print("I wonder if double quotes work on this.")
print('Well, I used single quotes on this one though.')
print('So, I still remember that my name is ' + Name1) #Note: Space is needed before and after a var w/out spaces
print('And that I am ' + str(Num1 + Num2) + ' years old') #Aaah there we go. 
#^The above wasn't working before, I needed to add the str() so that it knows to convert it into a string
#Interesting
print('And that at the end of the day my alias is ' + Name2)
print("There's something I don't know though which is, which university do you want to go to after community college?") 
#^Ooooooooo I just noticed something pretty cool with the line above. When I tried to make it so the code was also in the bottom
#^It didn't continue the code. Which means the indentation matters in Python. Hmmmm.
uniChoice = input()
print('Aaaaaa, ' + uniChoice + ', as I though so and suspected.')
