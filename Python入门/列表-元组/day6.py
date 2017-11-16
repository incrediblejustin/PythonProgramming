# #-------1. traverse a list---------
# nums = [11, 22, 33, 44, 55]
# # while
# len = len(nums)
# i = 0
# while i < len:
#     print(nums[i], end = " ")
#     i += 1
# print("")
#
# # for
# for num in nums:
#     print(num, end = " ")
# print("")

# #---------2. for - else---------
# nums = [11, 22, 33]
# #nums = []
# for num in nums:
#     print(num)
#     break
# else:
#     print('--')
#
# #else will be excuted only if [for loop didn't touch break] || [for loop didn't run at all]

# #--------3. Tuple ------------
# #tuple object does not support item assignment
# rdnums = (11, 22, 33)
# print("rdnums: ", rdnums)
#
# #access
# print("rdnums[0]): ", rdnums[0])
# print("rdnums[0:2]): ", rdnums[0:2])
# #rdnums[0] = 100, illegal, tuple's element can not be changed
# rdnums1 = (3.14,)
# print("rdnums1: ", rdnums1)
# print("rdnums + rdnums1 = ", rdnums + rdnums1)
#
# #delete
# del rdnums1
#
# #split
# a,b,c = rdnums
# print("a,b,c = rdnums : ", a, b, c)
#
# #single element
# snum = (11)
# print("type of snum = (11): ", type(snum)) # snum's type is int, use () as a operator
#
# snum = (11,)
# print("type of snum = (11,): ", type(snum)) # snum's type is typle


