#Public properties
class sample:
    def __init__(self):
        name = "Sneha" #Here name is a public properties or attributed
        age=22
        print(name, age)
s1=sample()


#Calling through objects

class simple:
    def showinfo(self):
        print(self.name, self.age)
s1=simple()
s1.name="Pranavi"
s1.age=22
s1.showinfo()



#Accessing private properties through 

class person:
     
    def __init__(self, name):
        self.__name=name
#getter method to access private properties   
    def get_name(self):
        return self.__name
#setter method to modify private properties
    def set_name(self, name):
        self.__name=name
p1=person("Yatala Sneha")
print(p1.get_name())
p1.set_name("Ellendula Pranavi")
print(p1.get_name())