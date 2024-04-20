class Node:
    def _init_(self, data):
        self.data = data
        self.next = None
        self.prev = None


def printLeftToRightManner(head):
    curr = head 
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.next 
    print()

def printRightToLeftManner(tail):
    tail = head 
    while tail.next != None:
        tail = tail.next 
 
    curr = tail
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.prev 
    print()
    
def addNodeAtTailOfLinkedList(head, val):
    newBlock = Node(val)
 
    if head == None:
        return newBlock
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = newBlock 
    newBlock.prev = tail 
    return head
    
def addNodeAtHeadOfLinkedList(head, val):
    newBlock = Node(val)
    if head == None:
        return newBlock
   
    newBlock.next = head 
    head.prev = newBlock 
    return newBlock

def deleteTailNodeInDoublyLinkedList(head):
    if head == None or head.next == None:
        return None 
    
    curr, previous = head, None
    while curr.next != None:
        previous = curr 
        curr = curr.next 
   
    previous.next = None 
    curr.prev = None 
    return head 

n = int(input())
values = list(map(int, input().split()))


head = None
for value in values:
    head = addNodeAtTailOfLinkedList(head, value)

    
printLeftToRightManner(head)
printRightToLeftManner(head)



head = deleteTailNodeInDoublyLinkedList(head)

printLeftToRightManner(head)



tail = head 
while tail.next != None:
    tail = tail.next 
printRightToLeftManner(tail)
