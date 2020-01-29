# Free Solo -- Ahmed Sultan
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

def computeAverage():
    for student in gradesDict:
        entry = gradesDict[student]
        gcount = 0
        gsum = 0.0
        gall = entry[1]
        for grade in gall:
            gcount = gcount + 1
            gsum = gsum + grade[1]
        entry.append(gsum / gcount)

def printAverage():
    for student in gradesDict:
        print(gradesDict[student][0], ":", gradesDict[student][2])

def createTable():
    q = "CREATE TABLE stu_avg (ID INTEGER PRIMARY KEY, AVERAGE REAL);"
    c.execute(q)
    for key in gradesDict:
        q = "INSERT INTO stu_avg VALUES ({}, {});".format(key, gradesDict[key][2])
        c.execute(q)

def addCourses(id, code, mark):
    q = "INSERT INTO courses VALUES({}, '{}', {});".format(id, code, mark)
    print(q)
    c.execute(q)


addCourses(3, 'harddev', 300)
studentsGrades()
computeAverage()
printAverage()
createTable()

# saving and exiting
db.commit()
db.close()
