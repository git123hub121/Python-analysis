# def printinfo():
#     print("="*10)
#     print("我是你爸爸！")
#     print("="*10)
# printinfo()

# def add2Num(a,b):
#     c = a + b
#     print(c)
# add2Num(11,12)
# go

# #文件打开关闭写入读取
# f = open("test.txt","w")#打开 必须是w 写入状态才行


# #f.close() 关闭文件
# f.readlines()

# #异常 必会代码
# import time

# with open("123.txt","w") as f:
#     f.write("我是你爸爸\nhhhhhaaa\nyou are so good!")
#     f.close()
# try:
#     with open("123.txt","r") as f:
#         try:
#             while True:
#                 # f.write("我是你爸爸\nok1111\nyou are so good!")
#                 # f.close()
#                 # with open("123.txt","r") as f:
#                 content = f.readline()
#                 if len(content) == 0:
#                     break
#                 time.sleep(2)
#                 print(content)
#         finally:
#             f.close()
#             print("文件关闭")
# except Exception as result:
#     print("发生异常")
#     print(result)

# #yes,异常完成！

import os
# import time
with open("gushi.txt","w") as f:
    whitegushi = f.write("床前明月光\n疑是地上霜\n举头望明月\n低头思故乡")
    f.close()

def readcopy():
    with open("gushi.txt","r") as f:
        content = f.read()
        # time.sleep(2)
        print(content)
        with open("copy.txt","w") as p:
            p.write(content)
readcopy()

#作业已完成！





























