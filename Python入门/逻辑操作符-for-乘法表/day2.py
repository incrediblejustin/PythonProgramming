# #------------1. logical operators---------
# age = int(input("please input ur age >> "))
#
# if age > 50:
#     print("your are an adult, and elder")
# elif age >= 18 and age <= 50:
#     print("your are an adult, and young")
# elif not (age >= 18):
#     print("your are not an adult")
# # and&  or|  not!

# #------------2. while structure-----------
# i = 1
# while i <= 5:
#
#     j = 1
#     while j <= i:
#         print("*", end = "")   #end = "", let print don't print \n
#         j += 1
#
#     print("")                  #print nothing, but print \n default
#     i += 1
# # print something like down here
# # *
# # **
# # ***
# # ****
# # *****

# #-------------3. print 99 乘法表-------------------

# i = 1
#
# while i <= 9:
#     j = 1
#     while j <= i:
#         print("%d * %d = %d\t"%(j, i, j * i), end = "")
#         j += 1
#     print("")
#     i += 1

# # print something like this
# # 1 * 1 = 1
# # 1 * 2 = 2	2 * 2 = 4
# # 1 * 3 = 3	2 * 3 = 6	3 * 3 = 9
# # 1 * 4 = 4	2 * 4 = 8	3 * 4 = 12	4 * 4 = 16
# # 1 * 5 = 5	2 * 5 = 10	3 * 5 = 15	4 * 5 = 20	5 * 5 = 25
# # 1 * 6 = 6	2 * 6 = 12	3 * 6 = 18	4 * 6 = 24	5 * 6 = 30	6 * 6 = 36
# # 1 * 7 = 7	2 * 7 = 14	3 * 7 = 21	4 * 7 = 28	5 * 7 = 35	6 * 7 = 42	7 * 7 = 49
# # 1 * 8 = 8	2 * 8 = 16	3 * 8 = 24	4 * 8 = 32	5 * 8 = 40	6 * 8 = 48	7 * 8 = 56	8 * 8 = 64
# # 1 * 9 = 9	2 * 9 = 18	3 * 9 = 27	4 * 9 = 36	5 * 9 = 45	6 * 9 = 54	7 * 9 = 63	8 * 9 = 72	9 * 9 = 81