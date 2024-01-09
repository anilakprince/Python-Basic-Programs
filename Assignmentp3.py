#Create a Person class with attributes like name, age, and address. Include methods to update and display the person's information.


class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def update(self):
        name=input("Enter new name: ")
        age=input("Enter new age: ")
        address=input("Enter new Address: ")
        self.name=name
        self.age=age
        self.address=address
    def display(self):
        print("the name is ",self.name)
        print("the age is ",self.age)
        print("the address is ",self.address)
        
p=Person("Sijo","22","Houseno.237")
p.display()
p.update()
p.display()
