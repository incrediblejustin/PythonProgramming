class Base(object):
    def show(self):
        print("-----base:show-----")

class A(Base):
    def show(self):
        print("-----A:show-----")

class B(Base):
    def show(self):
        print("-----B:show-----")


# ----------1. 多重继承----------
class C(A, B):
    def show(self):
        print("-----C:show-----")

    def test(self):
        B.show(self)  # 调用另一个类的同名函数，传入当前类的self

c = C()
c.show() #C:show

#C.__mro__将返回一个元组，按顺序表示当调用一个函数的时候搜索这个函数的类的顺序，如果当前没有将会在下一个类中查找
print(C.__mro__)
#(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>,
# <class '__main__.Base'>, <class 'object'>)