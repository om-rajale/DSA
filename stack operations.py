stack=[]
def push():
    elements=input("add elements:")
    stack.append(elements)
    print(stack)
def pop(): 
    if not stack:
        print("stack is empty")
    else:
        d = stack.pop()
        print("remove elements:",d)
        print(stack)
while True:
    choice = int(input("enter choice 1.push,2.pop.3.quit"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("enter correct choice")
        
    
