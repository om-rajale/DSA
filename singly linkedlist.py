class Node:
    def __init__(self,data):     
        self.data = data
        self.ref = None
class Linkedlist:
    def __init__(self): 
        self.head = None 
         
    def print_LL(self):
        if self.head == None:
            print('linkedlist is empty')
        else:
            n = self.head
            print('linkedlist is not empty')
            while n is not None:
                print(n.data)
                n = n.ref

LL1 = Linkedlist()
LL1.print_LL()
