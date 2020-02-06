

from queue import Queue
class Stack:
    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()
        self.curr_size=0


    def push(self,item):
        self.curr_size += 1
        self.q2.put(item)
        while not self.q1.empty():
            self.q2.put(self.q1.queue[0])
            self.q1.get()
        # q1 is empty

        self.q1,self.q2=self.q2,self.q1  
        # Now w2 is empty

    def pop(self):


        if (self.q1.empty()):
            return
        self.q1.get()
        self.curr_size -= 1

    def top(self):
        if (self.q1.empty()):
            return -1
        return self.q1.queue[0]

    def size(self):
        return self.curr_size

s = Stack()
s.push(1)
s.push(2)
s.push(3)

print("current size: ", s.size())
print(s.top())
s.pop()
print(s.top())
s.pop()
print(s.top())

print("current size: ", s.size())
