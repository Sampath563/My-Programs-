#2:
class Card:
    def __init__(self,imageUrl,deviceType,price,rating):
        self.imageUrl = imageUrl
        self.deviceType = deviceType
        self.price = price
        self.rating = rating

    def printalldetails(self):
        print("imageUrl:",self.imageUrl)
        print("deviceType:",self.deviceType)
        print("price:",self.price)
        print("rating:",self.rating)
                
product1=Card("Dummy-url 1","Mobile",56000,4.5)
print("Product - 1 :")
product1.printalldetails()
print()

product2=Card("Dummy-url 2","Laptop",94000,4.8)
print("Product - 2 :")
product2.printalldetails()
print()

product3=Card("Dummy-url 3","Smart-watch",18000,3.5)
print("Product - 3 :")
product3.printalldetails()
