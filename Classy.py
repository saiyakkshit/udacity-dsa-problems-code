class Classy(object):
    def __init__(self):
        self.items = []
    items = []
    j = 0

    def addItem(a):
        global items
        items = items.append(a)

    def getClassiness(self):
        global j
        global items
        for item in items:
            if item == 'tophat':
                j = j + 2
            elif item == 'bowtie':
                j = j + 4
            elif item == 'monocle':
                j = j + 5
            else:
                return 0
        return j


        # Test cases
me = Classy()
me.addItem('tophat')
print(me.items)