class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def __str__(self):
        return "x = %d, y = %d"%(self.x, self.y)

#--------只有对象对应的最后一个引用被删除后，自动调用该方法--------
    def __del__(self):
        print("this object has been release")

    def setx(self, new_x):
        self.x = new_x

    def sety(self, new_y):
        self.y = new_y


a = Point(5, 10)
b = a  # a --> mem <-- b
print("a : ", a,"\n", "b : ", b)
#------------测试引用计数---------
import sys
print("引用计数 = %d"%(sys.getrefcount(a)-1))

del a   # a -x-> mem <-- b
print("delete a\n")

print("引用计数 = %d"%(sys.getrefcount(b)-1))
del b   # a -x-> mem <-x- b
print("delete b\n")

