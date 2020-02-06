class Queue:
    def __init__(self,capacity):
        self.Q=[None]*capacity
        self.front=self.size=0
        self.rear=capacity-1
        self.capacity=capacity


    def isempty(self):
        return self.size==0


    def isfull(self):
        return self.size==self.capacity
        

    def EnQueue(self,item):
        if self.isfull():
            print("overflow")
            return
        self.rear=(self.rear+1)%self.capacity
        self.Q[self.rear]=item
        self.size+=1
        print("Enqueued item is ",item)



    def DeQueue(self):
        if self.isempty():
            print("Underflow")
            return
        print("Dequeued element",self.Q[self.front])
        self.front=(self.front+1)%self.capacity
        self.size-=1


queue=Queue(30)

queue.EnQueue(10)
queue.EnQueue(20)
queue.EnQueue(30)
queue.EnQueue(40)

print("size of queue before Dequeue is :", queue.size)
queue.DeQueue()

print("now the size of queue is :", queue.size)
