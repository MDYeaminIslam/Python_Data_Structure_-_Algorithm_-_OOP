#impliment stack using deque module. dequeue is double ended queue.
#applying deque module.
import collections
stack = collections.deque()
print(stack)
stack.append(10)#this append is used to add the elements in the deque
stack.append(30)
stack.append(50)
print(stack)

#removing value using pop()
stack.pop()
stack.pop()
print(stack)
print(not stack)

#now we are going to implement stack using Queue module 

import queue
stack1 = queue.LifoQueue() #LifoQueue is used to implement stack using queue module 

#for adding the elements in the stack using put() module 
stack1.put(12)
stack1.put(14)
stack1.put(16)
print(stack1)