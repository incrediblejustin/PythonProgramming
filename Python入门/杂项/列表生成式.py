#生成a = [1,2,3,4,5....,99]
# # --------1. 普通---------
# a = []
# i = 1
# while i != 100:
#     a.append(i)
#     i += 1
#
# print(a)

# # -----2. range()-------
# # range(start = 0, stop = 100, step = 1)
# a = [i for i in range(1, 100)]
# # a = [要插入到list中的变量 for 同名变量用来接受range() in range(start, stop, step)]
# print(a)

# #-----3. 如果只要其中的偶数-----
# a = [i for i in range(1, 100) if i%2==0]
# print(a)

#-----4. 多个for循环-----
a = [i for i in range(3) for j in range(2)] #每个i打印第二个循环的次数
print(a) # [0, 0, 1, 1, 2, 2]

b = [(i,j) for i in range(3) for j in range(2)]
print(b) # [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]