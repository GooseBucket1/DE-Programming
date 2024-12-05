# this function displays the menu
def menu():
    print ("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()

# this displayes the list and the number assigned to it
def show(inventory):
    for i, items in enumerate (inventory, start = 1):
        print (f"{i}. {items}")
    print ()

# this adds to the list however you can only have 4 items in your inventory
# and if you try to add another item then it will print that you need to drop somthing
def grab(inventory):
    if len(inventory) < 4:
        item = input("Name: ")
        inventory.append(item)
        print (f"{item} item was added.")
        print ()
    else:
        print ("You can't carry any more items. Drop something first.")
        print ()

# in the case you need to fix an item on the list this function will ask you what word
# you want to change by asking for its number than allows you to change that name
def edit(inventory):
    num = int(input("Number: "))
    if 1 <= num <= len(inventory):
        startAtOne = num - 1
        editedName = input("Name: ")
        inventory[startAtOne] = editedName
        print (f"Item number {num} was updated")
        print ()

# this function gets rid of a word when you type in the number that corisponds with
# the word
def drop(inventory):
    num = int(input("Number: "))
    if num < 1 or num > len (inventory):
        print ("Invalid invintory number.")
        print ()
    else:
        item = inventory.pop(num-1)
        print (f"{item} was dropped.")
        print ()

# this function will display the menu then whatever the cammand you imput in it will 
# go to that function
def main():
    print ("The Wizard Inventory program")
    menu()
    inventory = ["wooden staff", "wizard hat", "cloth shoes"]
    while True:
        command = input("Command: ")
        if command == "show":
            show(inventory)
        elif command == "grab":
            grab(inventory)
        elif command == "edit":
            edit(inventory)
        elif command == "drop":
            drop(inventory)
        elif command == "exit":
            print ("Bye!")
            break
        else:
            print ("Invaled command please try again")
            print ()

if __name__ == "__main__":
    main()































