#6 C235357 전채운
# Defining parent class 1
class Parent1 :
    def __init__(self,a):
        super().__init__()
        self.p1 = a
        
    # Parent's show method
    def show(self):
        print("Inside Parent1",self.p1)
    def display(self) :
        print("Inside Parent1",self.p1)
        
# Defining Parent class 2
class Parent2 :
    def __init__(self,a,b):
        super().__init__(a)
        self.p2 = b
    # Parent's show method
    def display(self):
        print("Inside Parent2",self.p2)
        
# Defining child class
class Child(Parent2, Parent1):
    def __init__(self,a,b,c) :
        super().__init__(a,b)
        self.c = c
        
    # Child's show method
    def show(self):
        print("Inside Child",self.c)
        
# Driver's code
obj = Child(1,2,3)

obj.show()
obj.display()
