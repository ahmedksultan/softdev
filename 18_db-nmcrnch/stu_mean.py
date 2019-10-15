# Ahmed Sultan
# SoftDev1 pd9
# K18 -- Average
# 2019-10-10

import sqlite3  # enable control of an sqlite database
import csv  # facilitate CSV I/O

# creating/accessing SQLite3 database file
DB_FILE = "discobandit.db"
db = sqlite3.connect(DB_FILE)
c = db.cursor()  # facilitate db ops

gradesDict = {}

def studentsGrades():
    # accessing data from database: (student name, id, code, mark)
    q = "SELECT name, students.id, code, mark FROM students, courses WHERE students.id = courses.id"
    foo = c.execute(q)
    for line in foo:
        # assigning values received from function to variables for ease of use
        name = line[0]
        idNo = line[1]
        course = line[2]
        mark = line[3]

        # creating a dictionary out of values, using idNo as keys
        # example: {1: ['name', [['course1', 75], ['course2', 88]]]} etc. etc.
        if idNo not in gradesDict.keys():
            gradesDict[idNo] = [name, [[course, mark]]]
        else:
            gradesDict[idNo][1].append([course, mark])

studentsGrades()

# saving and exiting
db.commit()
db.close()
