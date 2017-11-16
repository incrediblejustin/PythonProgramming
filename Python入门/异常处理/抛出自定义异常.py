class FuckException(Exception):
    def __init__(self, pos):
        self.pos = pos

    def __str__(self):
        return "fuck positon: %d"%self.pos

if __name__ ==  '__main__':
    try:
        s = input("输入：")
        pos = s.find("fuck")
        if pos != -1:
            raise FuckException(pos)
    except FuckException as fexcept:
        print(fexcept)

#------异常处理中抛出异常------
#直接使用 raise