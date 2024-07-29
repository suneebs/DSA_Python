stack=[]
# print(len(stack))
def push():
    if len(stack)==n:
        print("Stack is full")
    else:
        el=int(input("Enter the element: "))
        stack.append(el)
        print(stack)

def pop():
    if len(stack)==0:
        print("stack is empty")
    else:
        x=stack.pop()
        print("removed: ",x)
        print(stack)

n=int(input("Enter the length of stack: "))
while True:
    choice=int(input("Enter the choice\n 1.push 2.pop 3.exit\n"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("Enter correct choice")

# --------------------------------------------------------------------------------------------------
# using dequeue class

import collections
stack=collections.deque()
print(stack)
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)


#using queue module

import queue
stack=queue.LifoQueue()
stack.put(10)
stack.put(20)
stack.put(30)
print("size: ",stack.qsize())
print(stack.queue)
print(stack.get())
print(stack.get())
print(stack.get())
print(stack.get(timeout=1))