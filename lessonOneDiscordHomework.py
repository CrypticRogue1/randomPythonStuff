
            ### Listing 1 - Broken Code

hourly_wage = int(input("Enter your wage per hour: "))
hours_worked = int(input("Enter hours worked this week: "))
tax_to_take_out = 2000
gross_pay = hourly_wage * hours_worked
netPay = gross_pay - tax_to_take_out

print("In a typical week, I get paid", hourly_wage, "per hour and work for", hours_worked, "hours a week. I get paid", gross_pay, "a week, but get", tax_to_take_out, "taken out. So I get left with", netPay)

            ### Listing 2: Example Output

r = int(input("Please enter a radius for a circle: "))
pi = 3.14
A = pi * (r)**2

#print(pi * (r)**2)
print("The radius of the circle is", A)
