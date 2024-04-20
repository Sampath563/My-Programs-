class Box:
   def __init__(self, data):
       self.data = data
       self.previous = None
       self.next = None


      
def findTail(head):
   if head == None:
       return None
   tail = head
   while tail.next != None:
       tail = tail.next
   return tail


def insertAtEnd(head,item):
   newNode = Box(item)
   if head == None:
       return newNode
   tail = findTail(head)
   tail.next = newNode
   newNode.previous = tail
   return head


def printLeftToRight(head):
   curr = head
   while curr != None:
       print(curr.data, end = " ")
       curr = curr.next
   print()
  
def printRightToLeft(head):
   tail = findTail(head)
   while tail != None:
       print(tail.data, end = " ")
       tail = tail.previous
   print()
      
def deleteHeadNode(head):
   if head == None or head.next == None:
       return None
  
   head = head.next
   head.previous = None
   return head
  
n = int(input())
a = list(map(int, input().split()))


head = None
for item in a:
   head = insertAtEnd(head, item)
  
printLeftToRight(head)
printRightToLeft(head)


head = deleteHeadNode(head)


printLeftToRight(head)
printRightToLeft(head)
