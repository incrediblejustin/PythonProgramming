class SingleDog:
    # 类属性， 用来实现单例模式，即对象内存只创建一次
    __instance = None
    # 类属性，用来判断实例属性是否初始化过
    __init_flag = False
    def __new__(cls, name):
        if cls.__instance == None:
            print('第一次')
            cls.__instance = super().__new__(cls)
        else:
            print('其余的')
        return cls.__instance
    def __init__(self, name):
        if SingleDog.__init_flag == False:
            self.name = name
            SingleDog.__init_flag = True
        print("dog name: ", self.name)

if __name__ == "__main__":
    sdog = SingleDog("sdog")
    sdog2 = SingleDog("sdog2")
    sdog3 = SingleDog("sdog3")
    sdog4 = SingleDog("sdog4")
    print("id: ", id(sdog),id(sdog2),id(sdog3),id(sdog4))

# 第一次
# dog name:  sdog
# 其余的
# dog name:  sdog
# 其余的
# dog name:  sdog
# 其余的
# dog name:  sdog
# id:  4302284840 4302284840 4302284840 4302284840