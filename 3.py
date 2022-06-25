#3번 C235418 최민혁



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
def main():
    p = CPoint()
    q = CPoint(3,4)
    print(p,q)
    print(q.move(-4,5))
    print(p.move(5,6).move(2,3))
main()
