# #--------1. list --------
# names = ["zhao", "qian", "sun", "li", 100] # different types can put in one list
# print("names: ", names)
# print("type of names: ", type(names))
# print("type of name[0]: ", type(names[0]))
# print("type of name[-1]: ", type(names[-1]))
#
# #insert
# print('-------------------insert--------------------')
# names.insert(-1, "zhou") # insert something before name[i]
# print("names, insert(0, zhoug): ", names)
#
# #append
# names.append(3.14) # append something(as one element) after names[-1], same value can insert into one list
# print("names, append(3.14): ", names)
# # if names.append(other list), other list will be one element in the list[#,#,[other list]]
#
# #"+" , extend
# names1 = ["c++", "python", "go"]
# print("names1: ", names1)
# print("names + names1: ", names + names1) # use '+' to build a new list names + names1
# names.extend(names1) # add names1 to names' tail, names become a new list
# print("names.extend(names1): ", names)
# # append every element from other list to list, it's different between names.append(other list)
#
#
# #pop
# print('-------------------delete--------------------')
# names1.pop()
# print("names1.pop(): ", names1)
#
# #remove
# names1.remove("python")  # names1.remove(names1[1]), multi values, remove first merge value
# print("names1.remove(python): ", names1)
#
# #del
# del names1[0]
# print("del names1[0]: ")
#
# #modify
# print('-------------------modify--------------------')
# names[0] = 'ruby'
# print("names[0] = 'ruby': ", names)
#
# #search
# print('-------------------search--------------------')
# print("names: ", names)
# if 'ruby' in names:
#     print("ruby in names")
# else:
#     print("ruby not in names")
#
# if 999 not in names:
#     names.append(999)
#     print("append 999 in names")
#     print("new names: ", names)
# else:
#    print("999 in names")

# # -----------2. 集合 set-------
# # 集合不重复，相同添加到集合中只会出现一个
# a = [1,1,2,2,3,3]
# b = set(a)
# print(b)
# b.add(1)
# print(b)


# #-----------3. students name management--------
# names = []
# while True:
#
#     # # interface
#     print('-'*20)
#     print('1. add new name')
#     print('2. delete name')
#     print('3. modify name')
#     print('4. search name')
#     print('5. show names')
#     print('6. out of system')
#     print('-'*20)
#
#
#
#     # #operators
#     choice = int(input('please input your choice: '))
#
#     if choice == 1: # add
#         new_name = input('please input the name you want to add: ')
#         if new_name in names:
#             print('add %s error, %s already exist!'%(new_name, new_name))
#         else:
#             names.append(new_name)
#             print('add %s success!')
#
#     elif choice == 2: # del
#         new_name = input('please input the name you want to delete: ')
#         if new_name in names:
#             names.remove(new_name)
#         print('delete %s success'%new_name)
#
#     elif choice == 3: # mod
#         old_name = input('please input the name you want to modify: ')
#         if old_name in names:
#             id = names.index(old_name)
#             new_name = input('please input the new name: ')
#             names[id] = new_name
#             print('modify name "%s" to new name "%s" '%(old_name, new_name))
#         else:
#             print('name "%s" not exists!'%old_name)
#     elif choice == 4: # search
#         new_name = input('please input the name you want to search: ')
#         if new_name in names:
#             print('%s already exist!'%new_name)
#         else:
#             print('%s doesn\'t exist!'%new_name)
#     elif choice == 5: # show
#         i = 0
#         print('there are %d students'%len(names))
#         for name in names:
#             print('name[%d]: %s'%(i, name))
#             i += 1
#     elif choice == 6: # break
#         break
#     else:
#         print('input error')

