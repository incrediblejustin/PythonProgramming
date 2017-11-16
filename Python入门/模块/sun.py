def say1():
    print("this is a module, sun.say1()")

def say2():
    print("this is a module, sun.say2()")

def say3():
    print("this is a module, sun.say3()")

# print(__name__) # __main__
if __name__ == '__main__':
    say1()