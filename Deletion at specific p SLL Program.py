#Delete a node at specific position in Singly-linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtEndOfTail(head, item):
    Block = Node(item)
    if head is None:
        return Block
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = Block
    return head

def printlist(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

def deleteNodeAtSpecificPosition(head, position):
    if position == 1:
        return deleteHeadNodeInLinkedList(head)
    curr = head 
    index = 1 
    while index != position - 1:
        curr = curr.next 
        index += 1 
   
    main = curr.next 
    nextNode = main.next 
    main.next = None 
    curr.next = None 
    curr.next = nextNode 
    return head

n = int(input())
a = list(map(int, input().split()))
position = int(input())
head = None
for item in a:
    head = insertAtEndOfTail(head, item)
printlist(head)
head = deleteNodeAtSpecificPosition(head, position)
printlist(head)
