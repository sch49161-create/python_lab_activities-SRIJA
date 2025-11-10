#Multi level Inheritance Example in Python

class GrandParent:   
    def display(self):
        print("This is GrandParent class method")
class Parent(GrandParent):   
        def show(self):
            print("This is Parent class method")
class Child(Parent):
        def info(self):
            print("This is Child class method")

c1=Child()  # Creating object of Child class
c1.display()  # Calling GrandParent class method through Child class object
c1.show()  # Calling Parent class method through Child class object
c1.info()  # Calling Child class method through Child class object