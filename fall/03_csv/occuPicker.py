#   Ahmed Sultan 
#   SoftDev1 pd9
#   K06 -- StI/O: Divine your Destiny!
#   2019-09-17

import csv
import random

#   this code section goes through the csv file and creates ranges of percentages for each job field using the data
with open('occupations.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    dictionary = {}
    line = 0
    for row in csv_reader:
        if line == 0:
            dictionary[row[0]] = float(row[1]) * 10
            tempName = row[0]
            line = line + 1
        else:
            dictionary[row[0]] = (float(row[1]) * 10) + (dictionary[tempName])
            tempName = row[0]
            line = line + 1
    print(dictionary)

#   this code section uses the dictionary and prints a randomized selection (x10)
for x in range(0, 10):
    pickedNum = random.randint(0, 997)
    for entry in dictionary:
        if pickedNum < dictionary[entry]:
            print(pickedNum, '\t', entry)
            break
