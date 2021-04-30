import numpy as np
import random
#3种方法
# a = np.array([1,2,3,4])
# b = np.array(range(1,5))
# c = np.arange(1,5)
# print(a,b,c,"\n")

# print(type(a))
# print(a.dtype)#np里面的数据类型
# d = a.astype("int64")#起修改作用
# print(d.dtype)
# x = np.array([random.random() for i in range(10)])#random里面不能有参数ok  学编程，一定要将对象深刻人心
# y = np.round(x,2)
# print(y)
# x = [random.random() for i in range(10)].round(random.random(),2)   #AttributeError: 'list' object has no attribute 'round'
# a = np.array([[1,2,3,4],[5,6,2,4]])
# # a = a.shape
# # print(a)    #输出(2, 4)  行*列 如果是三维，就是 块，行，列  块*行*列=对应的元素个数
# a = a.reshape((8,)) #试着驶入1,8  8,1  4,2  8,
# print(a)

#   a.shape[0]代表行    a.shape[1]代表列    shape[0]*shape[1]
#a.flatten()     #将二维直接展开为一维，与上面对比
# np.arange(0,10).reshape(m,n) m*n=10       axis  m表示0轴  n表示1轴
#numpy读取数据

#loadtxt(文件文件,delimiter="",dtype="")
#取多行，多列，一行，一列  取多个不相邻的点  代码省略 也就是索引和切片
#修改 例如：a[a>4] = n
# np.where(a<10,0,10)#三元运算符
#a.clip(10,18)#裁剪
#数组拼接
# np.vstack((m,n))#竖直拼接
# np.hstack((m,n))#水平拼接
#行列交换





