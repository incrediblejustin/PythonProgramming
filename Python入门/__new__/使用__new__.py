class Dog(object):
    """a class of dog"""

    def __init__(self):
        print("this is __init__")

    def __new__(cls):
        """__new__ function"""
        print("this is __new__")
        return super().__new__(cls)

    def __del__(self):
        print("this is delete") 

if __name__ == '__main__':
    dog = Dog()
# 1. 首先调用Dog.__new__
# 2. 根据父类object，调用它的__new__，并返回这个对象的引用
# 3. 根据这个对象的引用调用它的__init__方法，最后返回这个引用给dog
# 4. 最后在进程结束的时候调用Dog.__del__


