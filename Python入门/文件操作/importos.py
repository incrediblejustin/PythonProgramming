import os
# os.rename("source_name.txt", "destination_name.txt") 修改文件名
# os.remove("source_name.txt") 将文件名为source_name.txt的文件删除
# os.mkdir("dir_name") 创建一个名为dir_name的目录
# os.getcwd() 获取当前目录的路径，并返回成字符串
# os.chdir("path") 将当前的工作目录修改为path指定的路径
# os.listdir("path") 把path路径指定的目录下的所有文件包括目录的名字放在list中返回
# os.rmdir("path") 删除path指定的目录

#-------1. 创建一个目录--------
dirlist = os.listdir(".")
for item in dirlist:
    if "importos_file_dir" == item:
        break;
else:
    os.mkdir("importos_file_dir")

#-------2. 给这个目录中放入一些文件----
i = 0
while i != 10:
    os.system("touch ./importos_file_dir/file_%d.txt"%i)
    i += 1

#--------3. 批量修改这些文件的名字-------
os.chdir("./importos_file_dir")
filelist = os.listdir("./")
for item in filelist:
    os.rename(item, "new_" + item)