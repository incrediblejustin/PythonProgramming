#-----------1. 字符串操作--------
mystr = "hello  and world  and bitch"

#find("str"), 从左向右找 能找到返回下标，否则返回-1
#rfind("str")，从右向左找 能找到返回下标，否则返回-1
#index("str")，从左向右找 能找到返回下标，否则发生错误
#rindex("str")，从右向左找 能找到返回下标，否则发生错误
#count("str")，统计字符串中含有str的个数
#replace("source", "destination"[, count])，返回字符被替换后的新的字符串，替换count个
#split(sep=None, maxsplit=-1)，把字符串根据sep切割返回一个list，maxsplit小于0全部分割，大于0分割maxsplit次，剩余的是一个元素，
#capitalize()，返回新的字符串，把字符串首字母大写
#title()，返回新的字符串，把字符串中所有单词首字母大写
#startswith("str")，判断字符串是否以str开头
#endswith("str")，判断字符串是否以str结尾
#upper()，把字符串的所有字符都改为大写，返回成新的字符串
#lower(), 把字符串的所有字符都改为小写，返回成新的字符串
#center(50)，把字符串居中在五十个字符中间
#ljust(50)，把字符串左对齐在五十个字符左边
#rjust(50)，把字符串右对齐在五十个字符右边
#strip()，默认字符串左右两边的空格全部去掉，作为新字符串返回，如果传入"str"，会在左右两边把str中有的字符都删除
#lstrip(), rstrip()，分别删除左右两边的
#partition("str")，把元字符串按照str分为 left，str，right作为tuple返回，某人从左向右找 str
#rpartition("str"), lpartition("str")，分别是从左右两边开始找到str再进行分割
#splitlines()，把字符串按换行切，作为一个新的list返回
#isalpha()，判断字符串是否是纯字母
#isdigit()，判断字符串是否是纯数字
#isalnum()，判断是否是字母数字组合
#isspace()，判断是否是纯空格
#a.join(list)，把list中的元素按照a的值连接起来，list = [a,b,c] a = "_"   ->  a_b_c