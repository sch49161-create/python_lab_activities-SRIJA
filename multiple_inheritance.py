#Multiple Inheritance Example in Python

class Father:
    def show(self):
        print("This is Father class method")
class Mother:
    def display(self):
        print("This is Mother class method")
class Child(Mother, Father):
    def info(self):
        print("This is Child class method")

c1=Child() 
c1.show()  
c1.display()
c1.info()