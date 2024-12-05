# Change Calculator

print ("Change Calculator")
print()


while True:
# sets the cents to zero until how much of each cents there are
    quarters = 0
    dimes = 0
    nickels = 0 
    pennies = 0
# asks user to imput the amout of change they have up to 99    
    change = int(input("Enter number of cents (0-99): "))

# I used if statments because using an elif statement would have not output the right values
    if  change >= 25:
        quarters = change // 25 # divides change by 25 (than for the other statments it does the same thing but by 10 and 5)
        change = change % 25 # this updates the remander 
    
    if change >= 10:
        dimes = change // 10
        change = change % 10

    if change >= 5:
        nickels = change // 5
        change = change % 5

    if change >= 1: 
        pennies = change

# prints how many of each there is 
    print()
    print(f"Quarters: {quarters}")
    print(f"Dimes:    {dimes}")
    print(f"Nickels:  {nickels}")
    print(f"Pennies:  {pennies}")
    print()

# asks if you want to continue if you put yes than it starts back at the top of the while loop but if you put "n" than it says bye and breaks
    keepGoing = input("Continue? (y/n): ")
    if keepGoing.lower() == "y":
        print()
        continue
    else:
        print()
        print("Bye!")
        break

 




















































