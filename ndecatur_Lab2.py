# Little note... so I was looking back over the slides and noticed that you put the code of how you solve this weeks lab on the slides
# so I am going to try using a function (I know how to do them from learning them at robotics)


# This is a function that converts a number grade to a letter grade
def gradeConverter(numGrade):
    if numGrade >= 90 and numGrade <= 100:
        print ("Letter grade: A")
    elif numGrade >= 80 and numGrade <= 89:
        print ("Letter grade: B")
    elif numGrade >= 70 and numGrade <= 79:
        print ("Letter grade: C")
    elif numGrade >= 60 and numGrade <= 69:
        print ("Letter grade: D")
    elif numGrade < 60:
        print ("Letter grade: F")


########## Main Code ########################################\
print ("Letter Grade Converter")
print ()

# Once you input your number grade it will move to the function 
numGrade = int(input("Enter numerical grade: "))
# Calls the function 
gradeConverter(numGrade)





