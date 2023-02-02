#impliment queue using dequeue module which is double ended queue.

import collections
queue =collections.deque()

#here we will add value using appanedleft method which will add value at the left side of the queue.
queue.appendleft(20)
queue.appendleft(30)
queue.appendleft(40)
print(queue)

#removing value form the queue using pop method which will remove the value from the right side of the queue.
queue.pop()
queue.pop()
print(queue)
queue.pop()
print(queue)

#now we do the same task but in vice versa formate

queue1 = collections.deque()
queue1.append(15)
queue1.append(25)
queue1.append(35)
print(queue1)

#now we will remove the value from the left side of the queue.
queue1.popleft()
queue1.popleft()
print(queue1)
queue1.popleft()
print(not queue1)

#here we talk about class name queue and model name is Queue.
#queue.Queue(maxsize) here maxsize is optional parameters which is used to set the max size of the queue other wise it will be infinite.
#put(item,block,timeout) here item is the value which we want to add in the queue, block is optional parameter which is used to set the block time of the queue, timeout is optional parameter which is used to set the timeout of the queue.
#put_nowait(item) here item is the value which we want to add in the queue.

#get(block,timeout) here block is optional parameter which is used to set the block time of the queue, timeout is optional parameter which is used to set the timeout of the queue.

#get_nowait() here we will get the value from the queue without any block time and timeout.


import queue
Q = queue.Queue() #here we don't give any parameter so it will be infinite.

Q.put(10)
Q.put(20)
print(Q.get())

