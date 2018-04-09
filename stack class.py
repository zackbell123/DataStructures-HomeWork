class listitem:
    def __init__(self, item, index):
        self.item = item
        self.index = index
        self.next = None
        self.prev = None
class myqueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def add(self, val):
        x = listitem(val, self.length)
        if self.length == 0:
            self.head = x
        else:
            x.prev = self.tail
            self.tail.next = x
        self.tail = x
        self.length+=1
    def remove(self):
        if (self.length != 0):
            self.head = self.head.next
            self.length = self.length - 1
        else:
            pass
                
                
    def __str__(self):
        op = str(self.head.item)
        y = self.head
        for i in range(self.length-1):
            y = y.next
            op = op  + " " + str(y.item)
        return op
class stack:
    def __init_(self):
        self.top = None
        self.length = 0
    def add(self, value):
        newItem = listitem(value, self.length)
        if (self.length == 0):
            self.top = newItem
        else:
            newItem.next = self.top
        self.top = NewItem
        self.length += 1
    def pop(self):
        if (self.length != 0):
            self.top = self.top.next
            self.length = self.length - 1
    def __str__(self):
        op = str(self.head.item)
        y = self.head
        for i in range(self.length-1):
            y = y.next
            op = op  + " " + str(y.item)
        return op
mylist = myqueue()
mylist.add(7)
mylist.add(3)
mylist.add(14)
mylist.add(1)
mylist.add(21)
mylist.add(0)
mylist.add(0)
mylist.add(56)
anlist = stack()
anlist.add(7)
anlist.add(3)
anlist.add(14)
anlist.add(1)
anlist.add(21)
anlist.add(0)
anlist.add(0)
anlist.add(56)

print(mylist)
print(anlist)
        
