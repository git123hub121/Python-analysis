import numpy as np
import pandas as pd

# import matplotlib
# from jedi.api.refactoring import inline



#   读取本地Excel数据
pd.read_excel("示例数据.xlsx")

#   生成指定格式/数量的数据   在Pandas中可以结合NumPy生成由指定随机数(均匀分布、正态分布等)生成的矩阵
pd.DataFrame(np.random.rand(10,2))

#   将表格中的数据存储至本地
#在Pandas中可以使用pd.to_excel("filename.xlsx")来将当前工作表格保存至当前目录下，当然也可以使用to_csv保存为csv等其他格式，也可以使用绝对路径来指定保存位置
#   pd.to_excel("filename.xlsx")
data = pd.DataFrame(np.random.rand(10,3))
data.to_excel("filename.xlsx")
data.to_csv("filename.csv")

#   按照指定要求筛选数据
#在Pandas中，可直接对数据框进行条件筛选，例如同样进行单个条件(薪资大于5000)的筛选可以使用df[df['薪资水平']>5000]
#如果使用多个条件的筛选只需要使用&(并)与|(或)操作符实现
# 先读取，再筛选
df = pd.read_excel("示例数据1.xlsx")
df[df['薪资水平']>5000]

#   在指定位置插入指定数据
#在Excel中我们可以将光标放在指定位置并右键增加一行/列，当然也可以在添加时对数据进行一些计算，
#比如我们就可以使用IF函数(=IF(G2>10000,"高","低"))，将薪资大于10000的设为高，低于10000的设为低，添加一列在最后
bins = [0,10000,max(df['薪资水平'])]
group_names = ['低','高']
df['new_col'] = pd.cut(df['薪资水平'], bins, labels=group_names)
df

#   删除指定行/列/单元格
#在Excel删除数据十分简单，找到需要删除的数据右键删除即可，比如删除刚刚生成的最后一列
#在pandas中删除数据也很简单，比如删除最后一列使用del df['new_col']即可
del df['new_col']   #这里是删除你所在列的标题头
df

#   按照指定要求对数据排序
#在pandas中可以使用sort_values进行排序，使用ascending来控制升降序，例如将示例数据按照薪资从高到低进行排序
#可以使用df.sort_values("薪资水平",ascending=False,inplace=True)
df.sort_values("薪资水平",ascending=False,inplace=True)
df

#   对缺失值(空值)按照指定要求处理
#Excel中可以按照查找—>定位条件—>空值来快速定位数据中的空值，接着可以自己定义缺失值的填充方式，比如将缺失值用上一个数据进行填充
#在pandas中可以使用data.isnull().sum()来检查缺失值，之后可以使用多种方法来填充或者删除缺失值，
#比如我们可以使用df = df.fillna(axis=0,method='ffill')来横向/纵向用缺失值前面的值替换缺失值
df.isnull().sum()
df = df.fillna(axis=0,method='ffill')
df

#   对重复值按照指定要求处理
#点击数据—>删除重复值按钮并选择需要去重的列即可
#在pandas中可以使用drop_duplicates来对数据进行去重，并且可以指定列以及保留顺序，
#例如对示例数据按照创建时间列进行去重df.drop_duplicates(['创建时间'],inplace=True)，可以发现和Excel处理的结果一致
df.drop_duplicates(['创建时间'],inplace=True)

#   修改指定数据的格式
#在Pandas中没有一个固定修改格式的方法，不同的数据格式有着不同的修改方法，
#比如类似Excel中将创建时间修改为年-月-日可以使用df['创建时间'] = df['创建时间'].dt.strftime('%Y-%m-%d')
df['创建时间'] = df['创建时间'].dt.strftime('%Y-%m-%d')
df

#   交换指定数据
#在Excel中交换数据是很常用的操作，以交换示例数据中地址与岗位两列为例，可以选中地址列，按住shift键并拖动边缘至下一列松开即可
#在pandas中交换两列也有很多方法，以交换示例数据中地址与岗位两列为例，可以通过修改列号来实现
cols = df.columns[[0,2,1,3,4,5,6]]
df = df[cols]
df

#   将两列或多列数据合并成一列
#在Excel中可以使用公式也可以使用Ctrl+E快捷键完成多列合并
#在Pandas中合并多列比较简单，类似于之前的数据插入操作，例如合并示例数据中的地址+岗位列使用df['合并列'] = df['地址'] + df['岗位']
df = df['合并列'] = df['地址'] + df['岗位']
df

#   将一列按照规则拆分为多列
#在Excel中可以通过点击数据—>分列并按照提示的选项设置相关参数完成分列，但是由于该列含有[]等特殊字符，所以需要先使用查找替换去掉
#在Pandas中可以使用.split来完成分列，但是在分列完毕后需要使用merge来将分列完的数据添加至原DataFrame，
#对于分列完的数据含有[]字符，我们可以使用正则或者字符串lstrip方法进行处理，但因不是pandas特性，此处不再展开
df['技能要求'].str.split(',',expand=True)

#   对数据进行分组计算
#在Excel中对数据进行分组计算需要先对需要分组的字段进行排序，之后可以通过点击分类汇总并设置相关参数完成，比如对示例数据的学历进行分组并求不同学历的平均薪资
#在Pandas中对数据进行分组计算可以使用groupby轻松搞定，
#比如使用df.groupby("学历").mean()一行代码即可对示例数据的学历进行分组并求不同学历的平均薪资，结果与Excel一致
df.groupby("学历").mean()

#   对数据进行一些计算
#在Excel中有很多计算相关的公式，比如可以使用COUNTIFS来统计薪资大于10000的岗位数量有518个
#在Pandas中可以直接使用类似数据筛选的方法来统计薪资大于10000的岗位数量len(df[df["薪资水平"]>10000])
len(df[df["薪资水平"]>10000])

#   对数据进行一些统计计算
#在Excel中有很多统计相关的公式，也有现成的分析工具，比如对薪资水平列进行描述性统计分析，可以通过添加工具库之后点击数据分析按钮并设置相关参数
#在pandas中也有现成的函数describe快速完成对数据的描述性统计，比如使用df["薪资水平"].describe()即可得到薪资列的描述性统计结果
df["薪资水平"].describe()

#   对数据进行可视化
#在Excel中可以通过点击插入并选择图表来快速完成对数据的可视化，比如制作薪资的直方图，并且有很多样式可以直接使用
#在Pandas中也支持直接对数据绘制不同可视化图表，例如直方图，可以使用plot或者直接使用hist来制作df["薪资水平"].hist()
# %matplotlib inline  这菊花不适用pycharm
from matplotlib import pyplot as plt
df["薪资水平"].hist()
plt.show()
#   对数据按要求采样
#在Excel中抽样可以使用公式也可以使用分析工具库中的抽样，但是仅支持对数值型的列抽样，比如随机抽20个示例数据中薪资的样本
#在pandas中有抽样函数sample可以直接抽样，并且支持任意格式的数据抽样，可以按照数量/比例抽样，比如随机抽20个示例数据中的样本
df.sample(20)

#   制作数据透视表
#数据透视表是一个非常强大的工具，在Excel中有现成的工具，只需要选中数据—>点击插入—>数据透视表即可生成，
#并且支持字段的拖取实现不同的透视表，非常方便，比如制作地址、学历、薪资的透视表
#在Pandas中制作数据透视表可以使用pivot_table函数，例如制作地址、学历、薪资的透视表
#pd.pivot_table(df,index=["地址","学历"],values=["薪资水平"])，虽然结果一样，但是并没有Excel一样方便调整与多样
pd.pivot_table(df,index=["地址","学历"],values=["薪资水平"])

#   利用VLOOKUP查找数据
#VLOOKUP算是EXCEL中最核心的功能之一了，我们用一个简单的数据来进行示例
#在Pandas中没有现成的vlookup函数，所以实现匹配查找需要一些步骤，首先我们读取该表格

#   这个较为复杂！


#   用Pycharm编写项目的时候是不能写magic函数的

#   本文链接    https://www.baidu.com/baidu?tn=monline_7_dg&ie=utf-8&wd=%25matplotlib+inline

#1. 数据读取
#2. 数据生成
#3. 数据存储
#4. 数据筛选
#5. 数据插入
#6. 数据删除
#7. 数据排序
#8. 缺失值处理
#9. 数据去重
#10.格式修改
#11.数据交换
#12.数据合并
#13.数据拆分
#14.数据分组
#15.数据计算
#16.数据统计
#17.数据可视化
#18.数据抽样
#19.数据透视表
#20.vlookup