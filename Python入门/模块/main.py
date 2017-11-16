# #---------1. 全部导入------
# import sun
# sun.say1()
# sun.say2()

# #---------2. 只导入一部分----
# from sun import say1
# from sun import say2
# say1()
# say2()

# #----------3. import *--------
# from sun import *
# from suntest import *
# say1()
# say2()
# #如果还导入其他模块中有同名函数， 这个同名函数会被后面导入的函数覆盖

# #-------4. 重命名--------
# import sun as iam5un
# iam5un.say1()

# #-------5. 模块的测试, __name__ ------
# #调用模块时，会把模块执行一次
# import sun # print(__name__) 会打印模块名，sun
# #所以在模块内进行测试的时候，应该把测试内容放在 if __name__ == '__main_': 之下

# #-------6. __all__ -----
# from sunall import *
# say1() # 可以执行
# say2() # say2未定义, 因为__all__里面只有say1