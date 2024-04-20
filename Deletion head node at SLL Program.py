#Delete head node in Singly-linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
 
def insertAtEndOfTail(head,item):
    Block = Node(item)
    if head == None:
        return Block
    curr = head 
    while curr.next != None:
        curr = curr.next 
    curr.next = Block
    return head
 
def printlist(head):
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next
    print()
def deleteHeadNodeInLinkedList(head):
    if head == None:
        return None 
 
    secondNode = head.next 
    head.next = None 
    return secondNode
 

n=int(input())
a=list(map(int,input().split()))
head=None
for item in a:
    head=insertAtEndOfTail(head,item)
printlist(head)
head = deleteHeadNodeInLinkedList(head)
printlist(head)
