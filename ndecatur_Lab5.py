from ndecatur_conversions import feetMeters
from ndecatur_conversions import metersFeet

def intro():
    print ("Feet and Meters Converter")
    print()

def menu():
    print("Conversions Menu:")
    print("a. Feet to Meters")
    print("b. Meters to Feet")

def main():
    intro()

    while True:
        menu()
        choice = input("Select a conversion (a/b): ")
        print()
        if choice == "a":
            feet = int(input("Enter feet: "))
            feetMeters(feet)
        elif choice == "b":
            meters = int(input("Enter meters: "))
            metersFeet(meters)
        print()
        answer = input("Would you like to perform another conversion? (y/n): ")
        print()
        if answer.lower() != "y":
            print ("Thanks, bye!")
            break



############# Main Code ################################

if __name__ == "__main__":
    main()





 
