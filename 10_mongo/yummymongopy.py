from pymongo import MongoClient
from bson.json_util import loads
import pprint

client = MongoClient('localhost', 27017)

f = open('office.json', 'r')
dataset = f.read().split('\n')
f.close()

items = []
