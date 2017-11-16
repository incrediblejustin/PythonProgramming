try:
    print("----0----")
    #print(num) #num not defined, NameError
    print("----1----")
    #open("xxx.txt")
    print("----2----")
    11/0


#-----------1. 单个错误捕获-------
except NameError:
    print("num未定义, NameError")


#-----------2. 多个一直错误捕获--------
except (NameError, FileNotFoundError):
    print("用元组捕获多个异常")

#-----------3. 任意错误捕获-------------
# except Exception:
#     print("使用Exception捕获所有异常")

except Exception as ret:
    print("捕获到异常，执行except")
    print(ret)
else:
    print("没有异常的时候，执行else")
finally:
    print("不管怎样, 都执行finally")

print("----end----")