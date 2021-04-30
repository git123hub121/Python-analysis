from matplotlib import pyplot as plt
import random
from matplotlib import font_manager
myfont = font_manager.FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc")
plt.figure(figsize=(15,6),dpi=80)
# 折线图
# x = range(120)
# y = [random.randint(20,35) for i in range(120)]
# plt.figure(figsize=(15,6),dpi=80)
# plt.plot(x,y)
# x_tick = ["10点{}".format(i) for i in range(60)]
# x_tick += ["11:{}".format(i) for i in range(60)]
# plt.xticks(list(x[::3]),x_tick[::3],rotation=45,fontproperties=myfont)
# plt.title("10点到12点每分钟的气温变化情况",fontproperties=myfont)
# plt.xlabel("时间",fontproperties=myfont)
# plt.ylabel("温度 单位(c)",fontproperties=myfont)


# x = range(20,32)
# y = [1,0,2,1,4,2,3,6,1,1,1,1]
# y1 = [1,2,1,5,4,1,0,3,1,2,0,1]
# plt.figure(figsize=(15,6),dpi=80)

# plt.plot(x,y,label="wo",linestyle="--",color="orange")
# plt.plot(x,y1,label="ta")

# x_tick = ["{}岁".format(i) for i in x]
# plt.xticks(x,x_tick,fontproperties=myfont)

# # plt.title("",fontproperties=myfont)
# # plt.xlabel("",fontproperties=myfont)
# # plt.ylabel("",fontproperties=myfont)
# plt.grid(alpha=0.4)
# plt.legend(prop=myfont,loc="upper left")

#以后记得加代理去下载模块 pip install 模块名 -i https://pypi.tuna.tsinghua.edu.cn/simple

#散点图
#折线图与散点图的唯一区别是：方法： 
#plt.scatter(x,y)

# #条形图     列表中的字符串也能能作为参数传入，
# a = ["速度与激情8","羞羞的铁拳","前任3：再见前任","功夫瑜伽","西游伏妖篇","变形金刚5：最后的骑士","芳华","摔跤吧！爸爸","寻梦环游记","加勒比海盗5：死无对证","金刚：骷髅岛","极限特工：终极回归","生化危机6：终章","乘风破浪","神偷奶爸3"]
# b = [56,26,21,19,17,16,15,14,13,12,12,11,11,11,10]
# # plt.bar(range(len(a)))#这样写的目的是为了自己设置x轴时更方便理解，例如：xticks()方法 第一个参数为可遍历对象，第二个参数实现对x轴的更改，在这里就可以改成字符串
# plt.barh(a,b,height=0.3,color="orange",label="票房电影")
# # x_tick = [i for i in a]
# plt.yticks(range(len(a)),a,fontproperties=myfont)
# plt.legend(prop=myfont,loc="upper right")

#刻度平移
# bar_width = 0.2
# x_1 = list(range(len(a)))
# x_2 = [i+bar_width for i in x_1]
# x_3 = [i+bar_width*2 for i in x_2]

plt.plot([1, 2, 3, 4], [1, 4, 9, 16],"ro")
plt.show()

# xticks()中有3个参数：
# xticks(locs, [labels], **kwargs)
# locs参数是一个数组，用于设置X轴刻度间隔
# [labels]参数也是一个数组，用于设置每个间隔的显示标签
# **kwargs可用于设置标签字体倾斜度和颜色等
# 例如下图，X轴间隔2显示一个刻度，由locs参数设置
# X轴上的数字2、4、6等就称为标签，具体显示内容由labels参数决定