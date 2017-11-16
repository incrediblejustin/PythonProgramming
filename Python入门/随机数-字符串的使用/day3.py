# #--------1. multi input -------
# a, b = (int(x) for x in input("please input two numbers >> ").split())
# c, d = input("please input two numbers >> ").split() # not int, but str
#
# print(type(a), type(b))
# print(type(c), type(d))

# #--------2. random number -------
# import random
# number = random.randint(0,100) #number == between(0, 100)

# #--------3. simple for loop structure---------
# name = "hello, this is sun"
# for ch in name:
#     print(ch, end = "") #print name by single character

# #--------4. break --------
# i = 1
# count = 0
# while i <= 100:
#     if i % 2 == 0:
#         print(i)
#         count += 1
#     if count == 20:
#         break
#     i += 1
# # print 20 even numbers between 1 ~ 100

# #--------5. string add-----
# name = "sun"
# print("str: %s"%name)
# print("str len: %d"%len(name))
#
# say = "this is " + name
# print("say: %s"%say)
# 
# newsay = "---%s---"%say
# print("newsay: %s"%newsay)
#
# print("add str from name[:n]: ", name[:3] + "ny")
#


# #---------6. string index ---------
# name = "sun xiaoqiang"
# print("orignal string: ", name)
# print("[0]", name[0], "[1]", name[1], "[2]", name[2], "[-1]", name[-1]) #len(name) == 3, index < 3, if index >= 3, out of range
# print("last ch, by len: ", name[len(name) - 1]) # access last character of name
# print("last ch, by [-1]: ", name[-1]) # access last character of name
#
# # # name[begin:end:step]
# cut1 = name[1:-1] # cut [begin, end - 1) to a new string
# print("cut form 1 to end-1: ", cut1) #un xiaoqian
#
# cut2 = name[1:]  # cut [begin, end) to a new string
# print("cut from 1 to end: ", cut2) #un xiaoqiang
#
# cut3 = name[1::2]
# print("cut from 1 to end, 2ch one step: ", cut3) #u ioin
#
# # #reverse
# rev = name[-1::-1]
# print("reverse: ", rev) #cut [end - 1, begin -1) # name[-1::-1] == name[::-1]

