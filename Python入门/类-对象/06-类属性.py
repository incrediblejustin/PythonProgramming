class Tool(object):
    # -------1. 类属性， 属于类-----
    count = 0

    #方法
    def __init__(self, new_name):
        # 实例属性
        self.name = new_name
        # ------2. 类属性的使用-----
        Tool.count += 1
        print(self.name, ": ", Tool.count)


tool1 = Tool("first")  # 1
tool2 = Tool("second") # 2
tool3 = Tool("third")  # 3

print("外部访问类属性： ", Tool.count)