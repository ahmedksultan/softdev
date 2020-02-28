from pymongo import MongoClient
from bson.json_util import loads
import pprint

client = MongoClient('localhost', 27017)

f = open('primer-dataset.json', 'r')
dataset = f.read().split('\n')
f.close()

items = []

for item in dataset:
    items.append(loads(item))

db = client.primer

restaurants = db.restaurants

result = restaurants.insert_many(items)

def findBorough(borough):
    for restaurant in db.restaurants.find({"borough": borough}):
        pprint.pprint(restaurant)

def findZipcode(zipcode):
    for restaurant in db.restaurants.find({"address.zipcode": zipcode}):
        pprint.pprint(restaurant)

def findZipcodeGrade(zipcode, grade):
     for restaurant in db.restaurants.find({'address.zipcode': zipcode, 'grades': {'$elemMatch': {'grade': grade}}}):
          pprint.pprint(restaurant)

def findZipcodeScoreBelow(zipcode, score):
     for restaurant in db.restaurants.find({'address.zipcode': zipcode, 'grades': {'$elemMatch': {'score': {'$lt': score}}}}):
          pprint.pprint(restaurant)

findZipcodeScoreBelow("10026", "4")
