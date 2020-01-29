import random

#   ATTEMPT I — choosing random character from defined 'krew'

KREWES = {
	'orpheus': ['Emily', 'Kevin', 'Vishwaa', 'Eric', 'ray', 'Jesse', 'Tiffany', 'Amanda', 'Junhee', 'Jackie ', 'Tyler', 'Emory', 'Ivan', 'Elizabeth', 'Pratham', 'Shaw', 'Eric', 'Yaru', 'Kelvin', 'Hong Wei', 'Michael', 'Kiran', 'Amanda', 'Joseph', 'Tanzim', 'David', 'Yevgeniy'],
	'rex': ['William', 'Joseph', 'Calvin', 'Ethan', 'Moody', 'Mo', 'Big Mo', 'Peihua', 'Saad', 'Benjamin', 'Justin', 'Alice', 'Hilary', 'Ayham', 'Michael', 'Matthew', 'Jionghao', 'Devin ', 'David', 'Jacob', 'Will', 'Hannah', 'Alex'],
	'endymion': ['Grace', 'Nahi', 'Derek', 'Jun Tao', 'Connor', 'Jason', 'Tammy', 'Albert', 'Kazi', 'Derek', 'Brandon', 'Kenneth', 'Lauren', 'Biraj', 'Jeff', 'Jackson', 'Taejoon', 'Kevin', 'Jude', 'Sophie', 'Henry', 'Coby', 'Manfred', 'Leia', 'Ahmed', 'Winston']
}
#   function to pick random character from dictionary of lists, given specific list
def studentPicker(krew):
    x = random.randrange(0, (len(KREWES[krew])))
    print(KREWES[krew][x])


print("\n--- semi random ---")
studentPicker('orpheus')
studentPicker('orpheus')
studentPicker('orpheus')
studentPicker('orpheus')
studentPicker('orpheus')
studentPicker('rex')
studentPicker('rex')
studentPicker('rex')
studentPicker('rex')
studentPicker('rex')
studentPicker('endymion')
studentPicker('endymion')
studentPicker('endymion')
studentPicker('endymion')
studentPicker('endymion')

#   ATTEMPT II — choosing random character from random 'krew'

def studentPicker2():
    x = random.randint(0, (len(KREWES)))
    if (x == 0):
        name = 'orpheus'
    elif (x == 1):
        name = 'rex'
    else:
        name = 'endymion'
    y = random.randrange(0, (len(KREWES[name])))
    print(KREWES[name][y])

print("\n--- completely random ---")
studentPicker2()
studentPicker2()
studentPicker2()
studentPicker2()
studentPicker2()
studentPicker2()
    

