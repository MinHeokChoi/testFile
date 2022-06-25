#2번 C235418 최민혁


class Shape:
    def __init__(self, color = 'yellow', filled = True ):
        self.__color = color
        self.__filled = filled
        
    def __str__(self):
        return f'({self.__color},{self.__filled})'
    
class Rectangle(Shape):
    def __init__(self,color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height
    def __str__(self):
        return super().__str__() + f'({self.width},{self.height})'
    def area(self):
        return f'{self.width*self.height}'
def main():
    c = Rectangle("blue",False,10,20)
    print(c)
    print(c.area())

main()