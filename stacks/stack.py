# A stack is structured, as an ordered collection of items where items are added to and removed from the end called the "top". Stacks are ordered LIFO. 

class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

""" s = Stack()
print(s.isEmpty())
s.push(1)
print(s.isEmpty())
s.push('two')
print(s.peek())
print(s.size())
s.pop()
s.peek()
s.pop()
print(s.isEmpty())
 """