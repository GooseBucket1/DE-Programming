# Even or Odd Checker
# You need to use a function

# Checks if the number is even and if it is not even then it will print "This is an odd number."
def evenOdd(num):
    if num % 2 == 0:
        print ("This is an even number.")
    else:
        print ("This is an odd number.")

# gets the user to imput a number than moves to the function evenOdd
def main():
    num = int(input("Enter an integer: "))
    evenOdd(num)


############# Main Code ##########################################
print ("Even or Odd Checker")
print()
if __name__ == "__main__":
    main()











































