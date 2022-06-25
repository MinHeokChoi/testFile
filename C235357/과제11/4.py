#4 C235357 전채운
class CPoint:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    
    def move(self, a, b):
        self.__x += a
        self.__y += b
        return self
        
    def __str__(self):
        return f'pos({self.__x},{self.__y})'
    
class Shape(CPoint):
    def __init__(self, color="yellow", filled=True, x=0, y=0):
        super().__init__(x,y)
        self.__color = color
        self.__filled = filled
    
    def __str__(self):
        return f'{super().__str__()}({self.__color},{self.__filled})'

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.__radius = radius
    
    def __str__(self):
        return f'{super().__str__()}(radius = {self.__radius})'
    
class Rectangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.__width = width
        self.__height = height
    
    def __str__(self):
        return f'{super().__str__()}({self.__width},{self.__height})'
    
    
def main():
    a = Shape()
    b = Shape("red")
    c = Shape("black",False,1,2)
    print(a)
    print(b)
    print(c)
    a.move(2,3)
    print(a)
    print(b.move(4,5))
    d = Circle("blue",False,10).move(3,4)
    print(d)
    e = Rectangle("blue",False,10,20)
    print(e.move(7,8))
    
main()