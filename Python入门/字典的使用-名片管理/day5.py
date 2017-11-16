# #-----------1. dict--------------
# dict = {'name':'sun'}
# print('orignal business card: ', dict)
#
# #insert
# dict['age'] = 23
# dict['phone'] = '10086'
# dict['qq'] = '331773166'
# print('insert age phone qq: ', dict)
#
# #delete
# del dict['qq']
# print('delete qq: ', dict)
#
# #modify
# dict['phone'] = '10010'
#
# #search
# print('search name in the business card: ', dict.get('name'))
#
# #dict.keys(), dict.values(), dict.items()
# print(dict.keys()) # dict_keys([key, key, ...])
# print(dict.values()) #dict_values([value, value])
# print(dict.items()) #dict_items([(key:value), (key:value)])
# if 'name' in dict.keys(): # same as dict.get('name')
#     print('name in it')
# for key in dict.keys(): #print every key in the dicts
#     print(key)
#
# #  traverse dict.items, item is a tuple,
# for item in dict.items():
#     print('key = %s, value=%s'%(item[0], item[1]))
# #  a,b = tuple >> a = tuple[0] b = tuple[1]
# for A,B in dict.items():
#     print('key = %s, value=%s'%(A, B))



    # #---------2. business card management--------------
# cards = []
# find_flag = False
# while True:
#
#     # # interface
#     print('-'*40)
#     print('1. add new card')
#     print('2. delete card')
#     print('3. modify card')
#     print('4. search card')
#     print('5. show cards')
#     print('6. out of system')
#     print('-'*40)
#
#
#
#     # #operators
#     choice = int(input('please input your choice: '))
#
#     if choice == 1: # add
#         new_name = input('please input the name you want to add: ')
#         for card in cards:
#             if new_name == card['name']:
#                 print('add %s error, %s already exist!' % (new_name, new_name))
#                 break
#         else:
#             new_qq = input('please input the qq you want to add: ')
#             new_weixin = input('please input the weixin you want to add: ')
#             new_card = {'name':new_name, 'qq':new_qq, 'weixin':new_weixin}
#             cards.append(new_card)
#             print('add %s\'s card success!'%new_name)
#
#     elif choice == 2: # del
#         new_name = input('please input the name you want to delete: ')
#         for card in cards:
#             if new_name == card['name']:
#                 cards.remove(card)
#                 break
#         print('delete %s success'%new_name)
#
#     elif choice == 3: # mod
#         old_name = input('please input the name you want to modify: ')
#         for card in cards:
#             if old_name == card['name']:
#                 card['name'] = input('please input the new name: ')
#                 card['qq'] = input('please input the new qq: ')
#                 card['weixin'] = input('please input the new weixin: ')
#                 print('modify %s\'s card to new %s\'s card '%(old_name, card['name']))
#                 find_flag = True
#                 break
#         else:
#             print('%s\'s card not exists!'%old_name)
#
#
#     elif choice == 4: # search
#         new_name = input('please input the name you want to search: ')
#         for card in cards:
#             if new_name == card['name']:
#                 print('%s already exist!'%new_name)
#                 find_flag = True
#                 break
#         else:
#             print('%s\'s card doesn\'t exist!'%new_name)
#
#     elif choice == 5: # show
#
#         print('there are %d cards'%len(cards))
#         print("name\tqq\twexin\t")
#         for card in cards:
#             print("%s\t%s\t%s"%(card['name'], card['qq'], card['weixin']))
#
#     elif choice == 6: # break
#         break
#     else:
#         print('input error')