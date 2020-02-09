# A queue is an ordered collection of items where the addition of new items happens at one end, called the "rear", and the removal of existing items occurs at the other en commonly called the "front". FIFO principle

class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

q = Queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue('A')
q.dequeue()
print(q.isEmpty())
print(q.size())
print(q.peek())