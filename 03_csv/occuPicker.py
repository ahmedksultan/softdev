import csv
import random

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

for x in range(0, 10):
    pickedNum = random.randint(0, 997)
    for entry in dictionary:
        if pickedNum < dictionary[entry]:
            print(pickedNum, '\t', entry)
            break
