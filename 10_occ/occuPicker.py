import csv
import random

#   STEP 1 - generate a dictionary, using the CSV as input
def dictGenerate(filename):
    myDict = {}  #  initializing empty dictionary
    
    #   reading through CSV file
    with open('occupations.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line = 0
        for row in csv_reader:
            if line > 0 and row[0] != 'Total':
                myDict[row[0]] = float(row[1])
            line = line + 1
    
    #   FOR TESTING PURPOSES --> print(myDict)
    return myDict

#   STEP 2 - generate a random number, and pick a specific field from the dictionary using said number
def occuPick(dict):
    pickedNum = float(random.randrange(0, 998)) / 10    #   picking a random number between 0 and 99.8, to be picked from the dictionary
    total = 0.0 #   Note: var total is updated as we move through the dictionary keys
    
    for entry in dict:
        total = total + dict[entry]     #   update total to represent the range currently occupied
        if pickedNum < total:   #   if random number chosen is in the range between the previous entry and the current entry, output
            print(pickedNum, '\t', entry)   #   print entry
            return entry    #   output entry
            break

#   Note: main() goes here; this is what is output to the Flask app

def main():
    q = dictGenerate('occupations.csv')
    return occuPick(q)

#   Calling on main()

main()
