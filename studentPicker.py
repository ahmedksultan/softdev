import random

KREWES = {
    'one': ['ahmed', 'joseph', 'max', 'alma', 'julian', 'mykolyk'],
    'two': ['tejas', 'leon', 'jason', 'tommy', 'manfred', 'fahim'],
    'three': ['bruh', 'moment', 'qbert', 'john', 'nora', 'lydia']
}

#function
def studentPicker(name):
    x = random.randrange(0, (len(KREWES[name])))
    print(KREWES[name][x])


studentPicker('one')
studentPicker('one')
studentPicker('one')
studentPicker('one')
studentPicker('two')
studentPicker('two')
studentPicker('two')
studentPicker('two')
studentPicker('three')
studentPicker('three')
studentPicker('three')
studentPicker('three')
studentPicker('three')
