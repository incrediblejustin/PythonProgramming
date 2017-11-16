class Point:
    def __init__(self, _x, _y):
        self.__x = _x    # 属性前加__， 变为私有属性，类内可修改， 类外不可修改
        self.__y = _y

    def __str__(self):
        return "__x = %d, __y = %d"%(self.__x, self.__y)

    def setx(self, new_x):
        self.__x = new_x

    def sety(self, new_y):
        self.__y = new_y
        # self.__print(), 私有方法可以再类内调用

#------------1. 私有方法的定义------------
    def __print(self):
        print("__x = %d, __y = %d"%(self.__x, self.__y))

a = Point(5, 10)
print("point a: ", a)

# a.__print()  无法使用，函数名前加 __ 表示该方法属于私有，不能再类外调用

#-------------2. 引用计数--------------------
b = a
print("point b: ", b)

a.setx(100)  # a --> mem <-- b,  mem.x = 100 , a和b都被执行了
print("point a after a.setx: ", a)
print("point b after a.setx: ", b)

#------------3. 私有属性-------------
# a.__x = 999  #不会被修改
# print(a)