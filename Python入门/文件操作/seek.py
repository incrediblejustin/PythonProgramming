#----------1. tell --------
f = open("seek.txt", "w")
f.write("hello")

pos = f.tell() # 5
print("position when i write \"hello\" ", pos)  # 5

f.seek(0, 0) # 把文件指针移到距离文件开头0个字符的位置
pos = f.tell()
print("position when i seek(0,0)  ", pos)  # 0
# f.seek(offset, from)
# offset是距离from的偏移
# from:0 文件开头 1 文件当前位置 2 文件末尾