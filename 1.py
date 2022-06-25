#1번 C235418 최민혁

#1. 2차원 도형을 나타내는 Shape 클래스를 완성하기.
#2. Shape를 상속받아서 Circle 클래스를 정의하기.

#*Shape 클래스는 color와 fillded 속성을 가짐.
#*Circle 클래스는 반지름을 나타내는 radius 변수를 추가로 정의함.


class Shape:
    def __init__(self, color = 'yellow', filled = True ):
        self.__color = color
        self.__filled = filled
        
    def __str__(self):
        return f'({self.__color},{self.__filled})'

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color,filled)
        self.radius = radius
    def __str__(self): 
        return super().__str__()+ f'(radius = {self.radius})'
    def area(self):
        return f'{self.radius*self.radius*3.14}'
def main():
    a = Shape()
    b = Shape("red")
    print(a,b)
    c = Circle("blue", False, 10)
    print(c)
    print(c.area())

main()
