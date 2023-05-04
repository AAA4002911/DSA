class Classy(object):
    def __init__(self):
        self.items = []

    def addItem(self, str):
        self.items.append(str)

    def getClassiness(self):
        sum = 0
        for ele in self.items:
            if ele == 'tophat':
                sum += 2
            elif ele == 'bowtie':
                sum += 4
            elif ele == 'monocle':
                sum += 5
        return sum


# Test cases
me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
# Should be 2
print(me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print(me.getClassiness())

me.addItem("bowtie")
# Should be 15
print(me.getClassiness())
