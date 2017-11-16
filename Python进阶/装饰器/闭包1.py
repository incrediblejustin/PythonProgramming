def func_100(val):
    passline = 60
    if val >= passline:
        print('pass')
    else:
        print('not pass')

def func_150(val):
    passline = 95 
    if val >= passline:
        print('pass')
    else:
        print('not pass')

func_100(90)
func_100(59)
func_150(100)
func_150(94)



print('-'*10,'Closure','-'*10)


# Closure: 内部函数中对enclosing作用域的变量进行引用
# 作用：1. 封装 2. 代码服用

def set_passline(passline):
    """Closure: 闭包，用来设置及格线的函数，返回比较器"""
    print('id of passline: %X'%id(passline))

    def cmp(val):
        """val表示成绩，val与passline比较，判断是否及格，输出结果"""
        if val >= passline:
            print('pass')
        else:
            print('not pass')

    # 返回比较器
    return cmp

fun_100 = set_passline(60)
print('id of fun_100: %X'%id(fun_100))
print(fun_100.__closure__)
fun_150 = set_passline(95)
print('id of fun_150: %X'%id(fun_150))
print(fun_150.__closure__)

fun_100(90)
fun_100(59)
fun_150(100)
fun_150(94)
