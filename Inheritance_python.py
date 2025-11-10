#Inheritance in Python

class Parent:   # Parent class or super or base class
    def displayinfo(self):
        print("This is Parent class method")
        a=10
        b=20
        if a<b:
            print("a is less than b")
        else:
            print("a is greater than b")
    def displaydata(self):
        print("This is another Parent class method")
class Child(Parent):   # Child class or sub class derived from Parent class
    def showinfo(self):
        print("This is Child class method")

c1=Child()  # Creating object of Child class
c1.displayinfo()  # Calling Parent class method through Child class object
c1.showinfo()  # Calling Child class method through Child class object
c1.displaydata()  # Calling another Parent class method through Child class object
