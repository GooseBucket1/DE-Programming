import csv

# the two functions cleans the names and emails
def cleanName(name):
    return name.strip().title()

def cleanEmail(email):
    return email.strip().lower()

# file names
FILENAME = "Lab10_prospects.csv"
CLEANEDFILE = "Lab10_prospects_clean.csv"

# this reads, cleans, and writes the original file into the new one
try: 
    with open(FILENAME, mode='r', newline='') as orginalFile, open(CLEANEDFILE, mode='w', newline='') as newFile:
        reader = csv.reader(orginalFile)
        writer = csv.writer(newFile)

        header = next(reader)
        writer.writerow([h.strip().upper() for h in header])

        #cleans the first and last name as well as cleans the email
        for row in reader:
            cleanedRow  = [cleanName(row[0]), cleanName(row[1]), cleanEmail(row[2])]
            writer.writerow(cleanedRow)

# prints the welcome letter than tells you the original file than the new cleaned file
    print ("Welcome to the Email List Cleaner")
    print()
    print (f"Source list: {FILENAME}")
    print (f"Cleaned list: {CLEANEDFILE}")
    print ()
    print ("Congratulations! Your list has been cleaned!")
except:
    print (f"The file {FILENAME} does not exist.")














