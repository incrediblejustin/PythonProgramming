class Base(object):

    def __init__(self):
        self.__a = 10
        self.b = 100

    def __test(self):
        print("Base::__test")

    def test(self):
        print("Base::test")


class Derive(Base):

    def show(self):
        print("Derive::show")

    def test(self):
        print("Derive::test")
        # Base.test(self)   可以再派生类中，根据基类的名字调用相应函数，传入self

d = Derive()

d.b = 9999
print("Derive.b: ", d.b) # d.b修改成了9999
d.test()                 # 成功调用，如果test被重写，就调用Derive::test 否则 调用Base::test

d.__a = 999
# print("Derive.a: ", d.__a) # d.__a没有被修改
# d.__test()               # 错误
