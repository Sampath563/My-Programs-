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


def insertAtEnd(head, ele):
   newNode = Box(ele)
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
      
def deleteAtSpecificPosition(head, position):
   currInd = 1
   curr = head
   prev = None
  
   while currInd != position:
       currInd += 1
       previous = curr
       curr = curr.next
      
   if previous == None:
       head = head.next
       head.previous = None
       return head
  
   previous.next = curr.next
   curr.next.previous = previous
   return head
  
n = int(input())
a = list(map(int, input().split()))
position = int(input())


head = None
for item in a:
   head = insertAtEnd(head, item)
  
printLeftToRight(head)
printRightToLeft(head)


head = deleteAtSpecificPosition(head, position)


printLeftToRight(head)
printRightToLeft(head)
