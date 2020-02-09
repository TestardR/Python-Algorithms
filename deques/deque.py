# A deque, also known as a double-ended queue, is an ordered collection of items similar to the queue
# New items can be added at either the front or the rear
# Likewise, existing items can be removed from eitheir end


class Deque(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)
    

d = Deque()
d.addFront('Hello')
d.addRear('World')
print(d.size())
print(d.removeFront() + ' ' + d.removeRear())