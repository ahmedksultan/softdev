# Dimension Q -- Ahmed Sultan
# SoftDev pd9
# K10 -- Import/Export Bank
# 2020-03-15

'''
name of dataset: Pokedex
description: contains the original 151 Pokemon from Generation 1, along with a few of their stats
hyperlink: https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json
brief summary of import:
     1) open the .json file
     2) read the .json file
     3) insert pokemon entries into the database
'''

from pymongo import MongoClient
import json
import pprint

client = MongoClient('localhost', 27017)

# setting up database stuff
db = client.dimensionq
pkmndb = db['pokemon']
pkmndb.delete_many({})

# opening, reading, and processing the json
f = open('pokedex.json', 'r')
file = f.read()
f.close()
data = json.loads(file)
pokemon = data['pokemon']
# inserting info into database
pkmndb.insert_many(pokemon)

### ----- METHODS ----- ###

# finding a pokemon in the database by its json number (id)
def findPKMNByID(id):
     for pkmn in pkmndb.find({'id': id}):
          print(pkmn['num'] + ' ' + pkmn['name'])

# finding a pokemon in the database by its pokedex number (num)
def findPKMNByNUM(num):
     for pkmn in pkmndb.find({'num': num}):
          print(pkmn['num'] + ' ' + pkmn['name'])

# find all pokemon in the database by type (type)
def findPKMNType(pktype):
     print("Finding PKMN with type " + pktype.upper())
     for pkmn in pkmndb.find({'type': pktype}):
          print(pkmn['num'] + ' ' + pkmn['name'])

# find type weaknesses for a pokemon when provided id, num, or name    
def findPKMNTypeWeakness(para):
     for pkmn in pkmndb.find({'id': para}):    
          print(pkmn['num'] + ' ' + pkmn['name'] + "'s weaknesses: " + weaknessListToString(pkmn['weaknesses']))
     for pkmn in pkmndb.find({'num': para}):
          print(pkmn['num'] + ' ' + pkmn['name'] + "'s weaknesses: " + weaknessListToString(pkmn['weaknesses']))
     for pkmn in pkmndb.find({'name': para}):
          print(pkmn['num'] + ' ' + pkmn['name'] + "'s weaknesses: " + weaknessListToString(pkmn['weaknesses']))

# HELPER FUNCTION for findPKMNtypeWeakness
# converts list of type weaknesses to string for output
def weaknessListToString(wklist):
     result = ''
     for pktype in wklist:
          result += pktype + ", "
     result = result[:-2]
     return result

'''
findPKMNByID(9)
findPKMNByID(131)
findPKMNByNUM('012')
findPKMNByNUM('057')
findPKMNType('Poison')
findPKMNTypeWeakness(1)
findPKMNTypeWeakness('001')
findPKMNTypeWeakness('Bulbasaur')
'''

client.close()
