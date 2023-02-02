""" Some of the methods of the Queue class.
1.enqueue() - This function is used to insert an element into the queue. The time complexity of this operation is O(1).
2.dequeue() - This function is used to remove an element from the queue. The time complexity of this operation is O(1).
3.isFull() - This function checks whether the queue is full or not. The time complexity of this operation is O(1).
4.isEmpty() - This function checks whether the queue is empty or not. The time complexity of this operation is O(1).

"""
#creating a queue using List
#Queue is FIFO -> First In First Out
"""
queue = []
queue.append(5) #adding elements to the queue using append() method
queue.append(6)
queue.append(7)
print(queue)
queue.pop(0) #removing elements from the queue using pop() method
queue.pop(0)
print(queue)
queue.pop(0)
print(queue) #at the end of the queue is empty and it will give an empty list.
    
"""



#impliment queue using insert() and pop() method
queue1 = []
queue1.insert(0,5) #adding elements to the queue using insert() method
queue1.insert(0,6)
queue1.insert(0,7)
print(queue1) 
queue1.pop() #removing elements form the queue using pop() method
queue1.pop()
queue1.pop()
print(queue1) #at the end of the queue is empty 
print(not queue1)
