#proper stack implementation using list
stack = []

def push():
    if len(stack) == stack_size:
        print("Stack is full")
    else:
        element = int(input("Enter the element: "))
        stack.append(element)
        print(stack)
        
def pop():
    if not stack:
        print("Stack is empty")
    else:
        pop_value = stack.pop()
        print(f"Removed value is {pop_value}")
        print(stack)
        
stack_size = int(input("Enter the size of stack: "))
while True:
    print("Enter the operation you want to perform: 1.push 2.pop 3.display 4.exit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        print(stack)
    elif choice == 4:
        break
    else:
        print("Enter the valid choice")

    