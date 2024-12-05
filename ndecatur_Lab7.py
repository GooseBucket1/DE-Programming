def lowHigh(quarterList): 
    lowest = min(quarterList) # gets the lowest number in the list
    highest = max(quarterList) # gets the highest number in the list

# prints the lowist and highest quarters
    print (f"Lowest Quarter:     {lowest}")
    print (f"Highest Quarter:    {highest}")



def main():
    print ("The Quarterly Sales program")
    print ()

# quarterList stores all the numbers inputend
    quarterList = []

# asks for the each quarterly sales 4 times than puts those numbers into the list quarterList
    for i in range(1, 5):
        quarter = float(input(f"Enter sales for Q{i}: "))
        quarterList.append(quarter)

# takes the list adds it up than divides by 4 than rounds to 2 decimal places
    total = sum(quarterList)
    newTotal = total / 4
    average = round(newTotal, 2)

# prints the total and average
    print()
    print(f"Total:              {total}")
    print(f"Average Quarter:    {average}")

# moves to the lowHigh function
    lowHigh(quarterList)

if __name__ == "__main__":
    main()
