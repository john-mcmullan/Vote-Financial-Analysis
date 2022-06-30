#import proper readers
import os
import csv

#Find the file to Read
Bcsv = os.path.join("Resources", "election_data.csv")

#New text file creation
outputfile = os.path.join("election_results.txt")

#Variables
votes = 0
candidates = []
canvotes = {}
winner = 0
victor = ""

with open(Bcsv) as file:
    
    #Reads the file
    reader = csv.reader(file)
    
    #finds the header
    head = next(reader)

    #Loop through data
    for row in reader:
        
        #Count the total amount of votes
        votes += 1

        #checks the 3rd column (index 2) for new names
        if row[2] not in candidates:
            
            #add to list
            candidates.append(row[2])

            #counts the first time you see the new name
            canvotes[row[2]] = 1
        
        else:
            # if the name is already there add to the total
            canvotes[row[2]] += 1

#Variable for dictionary list
voterout = ""

#loop to find a winner and counts
for x in canvotes:
    
    #get function to grab the numbers of each candidate
    y = canvotes.get(x)
    
    # (candidate votes / total voates) * 100 gives percentage
    percent = (float(y) / float(votes)) * 100

    # How it will look when printed
    voterout += f"\n{x}: {percent:.2f}% ({y})\n"

    # If statement to find winner
    if y > winner:

        winner = y

        victor = x
    
#how the output will look
output = (
    f"\nElection Results\n"
    f"\n---------------------------\n"
    f"\nTotal Votes: {votes:,}\n"
    f"\n---------------------------"
    f"\n{voterout}\n"
    f"---------------------------\n"
    f"\nWinner: {victor}\n"
    f"\n---------------------------"

)
print(output)

# Printing results into a new text file
with open(outputfile, 'w') as textFile:

    textFile.write(output)
