class Box:
    def __init__(self,name,rollnum,dbmsmarks,pythonmarks,osmarks,cnmarks,cmarks):
        self.name = name
        self.rollnum = rollnum
        self.dbmsmarks = dbmsmarks
        self.pythonmarks = pythonmarks
        self.osmarks = osmarks
        self.cnmarks = cnmarks
        self.cmarks = cmarks

# object creation
student1 = Box("Harika","5A1",78,67,77,89,46)
print(student1.name,end=" ")
print(student1.rollnum,end=" ")
print(student1.dbmsmarks,end=" ")
print(student1.pythonmarks,end=" ")
print(student1.osmarks,end=" ")
print(student1.cnmarks,end=" ")
print(student1.cmarks)


student2 = Box("Swapna","5A2",38,65,97,59,41)
print(student2.name,end=" ")
print(student2.rollnum,end=" ")
print(student2.dbmsmarks,end=" ")
print(student2.pythonmarks,end=" ")
print(student2.osmarks,end=" ")
print(student2.cnmarks,end=" ")
print(student2.cmarks)


student3 = Box("Sushma","5A3",88,95,47,89,31)
print(student3.name,end=" ")
print(student3.rollnum,end=" ")
print(student3.dbmsmarks,end=" ")
print(student3.pythonmarks,end=" ")
print(student3.osmarks,end=" ")
print(student3.cnmarks,end=" ")
print(student3.cmarks)
