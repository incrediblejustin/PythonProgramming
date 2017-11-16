#-------1. sunmsg是一个包---
# 包内必须有__init__.py

#-------2. __init__.py 的使用----
# from sunmsg import *
# recvmsg.recv_msg() #正确执行
# sendmsg.send_msg() #sendmsg未定义，因为__init__.py中的__all__没有sendmsg

# #-------3. import sunmsg 的使用-----
import sunmsg # python3, 必须在__init__.py 中加人 from . import module_name才能使用
sunmsg.recvmsg.recv_msg()
sunmsg.sendmsg.send_msg()
# #-------4. 包的查找顺序 --------
# 1. 现在当前目录中找，如果找不到 2
# 2. 在系统默认目录中找

# #-------5. 创建自己的模块，并且安装------
# 1. 创建模块外部创建setup.py文件，在其中导入from distutils.core import setup
# 2. 调用setup，其中主要的参数部分包括 py_modules=['包名.模块名']以及其他一些参数
    # Metadata-Version: 1.0
    # Name: iam5un
    # Version: 0.1
    # Summary: UNKNOWN
    # Home-page: UNKNOWN
    # Author: UNKNOWN
    # Author-email: UNKNOWN
    # License: UNKNOWN
    # Description: UNKNOWN
    # Platform: UNKNOWN
# 3. 调用 python3 setup.py build
# 4. 调用 python3 setup.py sdisk， 产生 ./dist/***.tar.gz, 里面包含了可以安装的包内容
# 5. 解压这个包，调用 python3 setup.py install, 管理员权限
# 6. 可以在任何位置调用import sunmsg