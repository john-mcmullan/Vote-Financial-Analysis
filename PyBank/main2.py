#import proper readers
import os
import csv

#Reading file
Bcsv = os.path.join("Resources", "budget_data.csv")

#Creating new file
outputfile = os.path.join("budget_analysis.txt")

#Variables
months = 0
total = 0
change = [] 
date = []

# Open the file
with open(Bcsv) as file:
    
    #Reads the file
    reader = csv.reader(file)
    
    #finds the header
    head = next(reader)
    
    #labels the first row with data
    first = next(reader)
    
    months += 1

    total += float(first[1])

    previous = float(first[1])
    
    #loops through the rows
    for row in reader:
        
        #Counting total months of data
         months += 1

         total += float(row[1])

        #find the change between each month
         netchange = float(row[1]) - previous

        #Stores the changes
         change.append(netchange)

        #Stores the dates
         date.append(row[0])

        #Resets the previous
         previous = float(row[1])

#Variables for increase and decrease and their dates
Gincrease = [date[0], change[0]]
Gdecrease = [date[0], change[0]]

# Loop to find greatest increase and decrease
for x in range(len(change)):

    #Find the Greatest increase by comparing each line of change
    if(change[x] > Gincrease[1]):
        Gincrease[1] = change[x]

        Gincrease[0] = date[x]
    
    #Find the Greatest decrease by comparing each line of change
    if(change[x] < Gdecrease[1]):
        Gdecrease[1] = change[x]

        Gdecrease[0] = date[x]


# Sum of the change divided by the total months of change gives average
average = sum(change) / len(change)

# Title screen
output = (
    f"\nFinancial Analysis\n"
    f"--------------------\n"
    f"Total Months: {months}\n"
    f"Total Revenue: ${total:,.2f}\n"
    f"Average Change: ${average:,.2f}\n"
    f"Greatest Increase: {Gincrease[0]} Amount ${Gincrease[1]:,.2f}\n"
    f"Greatest Decrease: {Gdecrease[0]} Amount ${Gdecrease[1]:,.2f}"
)

print(output)

#puts new information into new text file
with open(outputfile, 'w') as textFile:

    textFile.write(output)
