# #----------1. define a simple function---------
# # 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
# # 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
# # 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
# # 函数内容以冒号起始，并且缩进。
# # return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
# # def 函数名（参数列表）:
# #     函数体
#
# def show(stuff):
#     print("show stuff: ", stuff)
#     stuff = 100
#     return type(stuff)
#
#
# List = [99,"99",(99, 100),[99, 100],{99, 100},{"first":99, "second":100}]
#
# for item in List:
#     print("----before show----")
#     Type = show(item)
#     print("----after show(stuff has been changed)----")
#     print(item)
#     #print("type of stuff: ", Type)
#     print("")

#---------------2. mutable & immutable------------
#----2.1 imutable----
def change_int(a):
    a = 100

Int = 2
print("before change_int:", Int)
change_int(Int)
print("after change_int:", Int)

def change_str(a):
    a = "100"

Str = "2"
print("before change_str:", Str)
change_str(Str)
print("after change_str:", Str)

def change_tuple(a):
    a = (3,4)

Tuple = (2,3)
print("before change_tuple:", Tuple)
change_str(Tuple)
print("after change_tuple:", Tuple)

print("-"*50)
#----2.2 mutable----
def change_list(a):
    a.append(4)
def change_set(a):
    a.add(4)
def change_dict(a):
    a["4"] = 4

List = [2,3]
print("before change: ", List)
change_list(List)
print("after change: ", List)
Set = {2,3}
print("before change: ", Set)
change_set(Set)
print("after change: ", Set)
Dict = {"2":2, "3":3}
print("before change: ", Dict)
change_dict(Dict)
print("after change: ", Dict)

# #-----------arguments------------
# #命名参数
# def func1(name, age):
#     print("name: ", name)
#     print("age:  ", age)
#
#  #func1(name = 'sun', age = 23)
# func1(age = 23, name='sun')
#
# #缺省参数
# def func2(name, age = 23):
#     print("name: ", name)
#     print("age:  ", age)
#
# func2('sun')
# func2('sun', 23)
# func2(name = 'sun', age = 23)
# func2(age = 23, name = 'sun')
#
# #可变长参数
# def sum(*args, **kwargs):
#     print('-'*6)
#     sum = 0
#     for item in args:
#         sum += item
#
#     print("args: ", args)
#     print("sum = ", sum)
#     print("kwargs: ", kwargs)
#     print('-'*6)
#
# sum()                # args = () , sum = 0
# sum(1,2,3)           # sum = 6
# sum(11,22,33,44, name='sun', age = 18)     # sum = 110
#
# #拆包
# Tuple = (11,22,33,44)
# Dict = {"name":"sun", "age":23}
#
# def Print(*args, **kwargs):
#     print("args: ", args)
#     print("kwargs: ", kwargs)
#
# Print(Tuple, Dict) # args(Tuple, Dict) , kwargs{}
# Print(*Tuple, **Dict) # args(Tuple[0], Tuple[1]...)  kwargs{Dict[0], Dict[1]...}
# Print(*Dict) # args(dict[0].key, dict[1].key....), kwargs{}
# #Print(**Tuple) #wrong

