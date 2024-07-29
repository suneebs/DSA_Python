queue=[]
def enqueue():
    if len(queue)==n :
        print("Queue is full")
    else:
        el=int(input("Enter the element: "))
        queue.append(el)

def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        print("removed: ",queue.pop())

def display():
    if not queue:
        print("Queue is empty")
    else:
        print(queue)

n=int(input("Enter the Queue size: "))

while True:
    choice=int(input("Enter the choice\n1.Enqueue\n2.Dequeue\n3.Display\n4.Exit \n"))
    if choice == 1:
        enqueue()
    elif choice ==2:
        dequeue()
    elif choice == 3:
        display()
    elif choice==4:
        break
    else:
        print("\nEnter correct choice!")

