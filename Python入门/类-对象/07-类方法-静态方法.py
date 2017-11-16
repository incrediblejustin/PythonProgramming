class Tool(object):
    # -------1. 类属性， 属于类-----
    count = 0

    #实例方法
    def __init__(self, new_name):
        print("--这是一个实例方法--")
        self.name = new_name
        Tool.count += 1
        # print(self.name, ": ", Tool.count)

    #类方法
    @classmethod
    def add_count(cls):
        print("--这是一个类方法--")
        cls.count += 2

    #静态方法
    @staticmethod
    def print_menu():
        print("--这是一个静态方法--")
        print("1. shit")
        print("2. bitch")
        print("3. fuck")

#-------1. 类方法的使用-------
Tool.add_count()
print("外部访问类属性： ", Tool.count)

#--------2. 静态方法的使用-----
Tool.print_menu()

tool = Tool("a")
tool.print_menu()