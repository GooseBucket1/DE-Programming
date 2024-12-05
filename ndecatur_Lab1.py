# Travel Time Calculator

import math


########### Mine Code ###################
print ("Travel Time Calculator")
print ()
distence = int(input("Enter miles: "))
milesPerHour = int(input("Enter miles per hour: " ))
timeTraveled = distence // milesPerHour
#to get the remainder can use this for the time travil calculator
min = distence % milesPerHour

print()
print (f"Estimated travel time \n Hours: {timeTraveled} \n Minutes: {min}")



