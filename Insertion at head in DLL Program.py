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


def insertAtEnd(head, item):
   Node = Box(item)
   if head == None:
       return Node
   tail = findTail(head)
   tail.next = Node
   Node.previous = tail
   return head


def insertAtBeginning(head, item):
   Node = Box(item)
   if head == None:
       return Node
  
   Node.next = head
   head.previous = Node
   head = Node
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
      
n = int(input())
a = list(map(int, input().split()))
newElement = int(input())
head = None
for item in a:
   head = insertAtEnd(head, item)
  
printLeftToRight(head)
printRightToLeft(head)


head = insertAtBeginning(head, newElement)


printLeftToRight(head)
printRightToLeft(head)
