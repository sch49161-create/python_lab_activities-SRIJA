#Method Overriding Example

class Parent:
    def showinfo(self):
        print("This is parent class method")
class Child(Parent):
    def showinfo(self):
      super().showinfo()         #here super keyword refers parent class data
      print("This is child class method")

c1=Child()
c1.showinfo() #Here interpreter takes a limited time


#Method Overloading Example

class Text:
    def display(self, name=None, age=None):
        if name is not None and age is not None:
            print("Name:", name, "Age:", age)
        elif name is not None:
            print("Name:", name)
        else:
            print("No parameters passed")
t2 = Text()
t2.display()  
t2.display("Alice")
t2.display("Bob", 30)