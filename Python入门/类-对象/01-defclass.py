class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def __str__(self):
        return "x = %d, y = %d"%(self.x, self.y)

    def setx(self, new_x):
        self.x = new_x

    def sety(self, new_y):
        self.y = new_y

a = Point(5, 10)
print("point a: ", a)
b = Point(2, 3)
print("point b: ", b)

a.setx(100)
print("point a after setx: ", a)

b.sety(1000)
print("point b after sety: ", b)


