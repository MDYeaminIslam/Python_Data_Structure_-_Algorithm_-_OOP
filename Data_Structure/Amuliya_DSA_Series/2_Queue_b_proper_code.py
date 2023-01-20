queue = []
def enqueue():
    element = int(input("\nEnter the element: "))
    queue.append(element)
    print(element," is added to the queue")
    
def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        value_removed = queue.pop(0)
        print(value_removed," is removed from the queue")

def display():  
    print(queue) 

while True:
    choice = int(input("\nEnter your choice 1.enqueue 2.dequeue 3.display 4.exit: ")) 
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Enter the correct operation")
        