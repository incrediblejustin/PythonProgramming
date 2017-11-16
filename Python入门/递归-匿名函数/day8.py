# #------------1. 递归 -------------
# # n!
# def factorial(num):
#     if num == 1:
#         return num
#     return num * factorial(num-1)
# num = 4
# print("%d! = %d"%(num, factorial(num)))


# #-----------2. 匿名函数----------
# # lambda 参数:式子
#
# func = lambda x,y:x+y
# print("res = ", func(1,2)) # res = 3
#
# def test(x, y):
#     x+y
# print("res = ", test(1,2)) # res = None
#
# # 匿名函数的应用场景     1
# # 一般list排序
# nums = [11,12,9,8]
# nums.sort(reverse=True)
# print("sorted nums : ", nums)
#
# # 复杂list排序，其中有dict，dict之间无法直接比较
# info = [{"name":"zhao", "age":18},{"name":"qian", "age":19},{"name":"sun", "age":20}]
# print("info : ", info)
# # info.sort() #没有dict < dict, 无法直接比较
# info.sort(key = lambda x:x["name"]) #按名字顺序排序
# print("sorted with name, info : ", info)
#
# info.sort(key = lambda x:x["age"]) #按名字顺序排序
# print("sorted with age, info : ", info)
#
# # 匿名函数的应用场景     2
# def print_result(a, b, func):
#     result = func(a, b)
#     print("result : ", result)
#
# print_result(10, 20, lambda x,y:x+y) # result : 30
# print_result(20, 10, lambda x,y:x-y) # result : 10
# func_new = input("please input func:")# lambda x,y:x+y+100
# func_new = eval(func_new) # func_new = lambda x,y:x+y+100
# print_result(10, 20, func_new) # result : 130