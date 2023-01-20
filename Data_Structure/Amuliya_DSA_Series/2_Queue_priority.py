#Queue is linear data structure which follow the FIFO(FIrst In First Out) principle.

#value will be removed form the Queue according their priority.

#here we set lowest value highest priority.
#priority queue 


#here we set lowest value highest priority.
#priority queue 
import queue
Queue = queue.PriorityQueue() #this method give lowest value highest priority.
#for entering value in the Queue we use put method and for removing value from the Queue we use get method.
Queue.put(10)
Queue.put(60)
Queue.put(20)
Queue.put(40)
Queue.put(40)
print(Queue.get())
print(Queue.get())
print(Queue.get())
print(Queue.get())
print(Queue.get())


#if we want to give item with their priority then we use tuple.

"""
    q = []
q.append((9, 80))
q.append((7, 34))
q.append((2, 10))
q.append((8, 58))
q.append((3, 23))
q.sort(reverse=True)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))
    
"""
