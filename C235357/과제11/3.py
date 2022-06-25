#3 C235357 전채운
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

def main():
    p = CPoint()
    q = CPoint(3,4)
    print(p,q)
    print(q.move(-4,5))
    print(p.move(5,6).move(2,3))
    
main()