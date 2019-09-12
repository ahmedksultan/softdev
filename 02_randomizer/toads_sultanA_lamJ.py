import random

#   KREWES data
KREWES = {
	'orpheus': ['Emily', 'Kevin', 'Vishwaa', 'Eric', 'ray', 'Jesse', 'Tiffany', 'Amanda', 'Junhee', 'Jackie ', 'Tyler', 'Emory', 'Ivan', 'Elizabeth', 'Pratham', 'Shaw', 'Eric', 'Yaru', 'Kelvin', 'Hong Wei', 'Michael', 'Kiran', 'Amanda', 'Joseph', 'Tanzim', 'David', 'Yevgeniy'],
	'rex': ['William', 'Joseph', 'Calvin', 'Ethan', 'Moody', 'Mo', 'Big Mo', 'Peihua', 'Saad', 'Benjamin', 'Justin', 'Alice', 'Hilary', 'Ayham', 'Michael', 'Matthew', 'Jionghao', 'Devin ', 'David', 'Jacob', 'Will', 'Hannah', 'Alex'],
	'endymion': ['Grace', 'Nahi', 'Derek', 'Jun Tao', 'Connor', 'Jason', 'Tammy', 'Albert', 'Kazi', 'Derek', 'Brandon', 'Kenneth', 'Lauren', 'Biraj', 'Jeff', 'Jackson', 'Taejoon', 'Kevin', 'Jude', 'Sophie', 'Henry', 'Coby', 'Manfred', 'Leia', 'Ahmed', 'Winston']
}

#   randomizer, providing krew from KREWES
def studentPicker(krew):
    x = random.randint(0, (len(KREWES[krew])))
    return(KREWES[krew][x])

#   randomizer (totally random)
def studentPicker2():
    x = random.randint(0, (len(KREWES)))
    if (x == 0):
        name = 'orpheus'
    elif (x == 1):
        name = 'rex'
    else:
        name = 'endymion'
    y = random.randrange(0, (len(KREWES[name])))
    return(KREWES[name][y])

print('Totally random student: ' + studentPicker2())
print('Totally random student: ' + studentPicker2())
print('Totally random student: ' + studentPicker2())

print('Random student from ORPHEUS: ' + studentPicker('orpheus'))
print('Random student from REX: ' + studentPicker('rex'))
print('Random student from ENDYMION: ' + studentPicker('endymion'))




