class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.previous = None 
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

 
def printLeftToRightManner(head):
    
    curr = head 
    while curr != None:
        print(curr.data, end =" ")
        curr = curr.next 
    print()
 
def printRightToLeftManner(tail):
    
    curr = tail
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.previous 
    print()

    
def addNodeAtTailOfLinkedList(head, val):
    Block = Node(val)
 
    if head == None:
        head = Block
        return head
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
 
    tail.next = Block 
    Block.previous = tail 
    return head
 
 
n=int(input())
values = list(map(int, input().split()))

dll = DoublyLinkedList()
for value in values:
    dll.head = addNodeAtTailOfLinkedList(dll.head, value)
    if dll.tail is None:
        dll.tail = dll.head
    else:
        dll.tail = dll.tail.next
 
printLeftToRightManner(dll.head)
printRightToLeftManner(dll.tail)
