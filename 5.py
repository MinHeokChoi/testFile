#5번 C235418 최민혁

class Shape:
    def __init__(self, color = 'yellow', filled = True, cpoint = None):
        if cpoint == None:
            self.cpoint = CPoint()
        else:
            self.cpoint = cpoint #cpoint에 좌표를 나타내는 객체를 할당받았을 때
        self.color = color
        self.filled = filled
    def __str__(self):
        return f'pos{self.cpoint}({self.color},{self.filled})'
    def move(self,a,b):
        CPoint.move(self.cpoint,a,b)
        return self

class CPoint:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return f'pos({self.x},{self.y})'
    def move(self,a,b):
        self.x += a
        self.y += b
        return self
    
class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color,filled)
        self.radius = radius
    def __str__(self): 
        return super().__str__()+ f'(radius = {self.radius})'
    def area(self):
        return f'{self.radius*self.radius*3.14}'

class Rectangle(Shape):
    def __init__(self,color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height
    def __str__(self):
        return super().__str__() + f'({self.width},{self.height})'
    def area(self):
        return f'{self.width*self.height}'
    
def main() :
    a = Shape()
    b = Shape("red")
    cpoint = CPoint(4,7)
    c = Shape("black",False,cpoint)
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
