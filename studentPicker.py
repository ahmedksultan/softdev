import random

#   ATTEMPT I — choosing random character from defined 'krew'

KREWES = {
    'alpha': ['ness', 'mario', 'luigi', 'mewtwo', 'banjo', 'roy', 'falco'],
    'beta': ['donkey kong', 'pikachu', 'yoshi', 'captain falcon', 'lucas', 'link', 'kirby'],
    'gamma': ['sonic', 'cloud', 'king dedede', 'snake', 'jigglypuff', 'fox', 'zelda']
}

#   function to pick random character from dictionary of lists, given specific list
def studentPicker(krew):
    x = random.randrange(0, (len(KREWES[krew])))
    print(KREWES[krew][x])


print("--- semi random ---")
studentPicker('alpha')
studentPicker('alpha')
studentPicker('alpha')
studentPicker('alpha')
studentPicker('alpha')
studentPicker('beta')
studentPicker('beta')
studentPicker('beta')
studentPicker('beta')
studentPicker('beta')
studentPicker('gamma')
studentPicker('gamma')
studentPicker('gamma')
studentPicker('gamma')
studentPicker('gamma')

#   ATTEMPT II — choosing random character from random 'krew'

def studentPicker2():
    x = random.randrange(0, (len(KREWES)))
    if (x == 0):
        name = 'alpha'
    elif (x == 1):
        name = 'beta'
    else:
        name = 'gamma'
    y = random.randrange(0, (len(KREWES[name])))
    print(KREWES[name][y])

print("--- completely random ---")
studentPicker2()
studentPicker2()
studentPicker2()
studentPicker2()
studentPicker2()
studentPicker2()
    

