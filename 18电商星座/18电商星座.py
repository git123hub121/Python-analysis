import pandas as pd
from pandas.core.frame import DataFrame
#读取xlsx表
df = pd.read_excel('sfz.xlsx',header=0,names=['xuehao','name','sfz','sex','nation','number'])#
df.head(5)
#读取需要的列
dom = df['sfz']
dom = df['sfz'].str
#字符串分词处理
sfz_list = []
for i in list(dom):
    # i = i[6:14]
    # print(i)
    h = i[6:10]
    j = i[10:12]
    k = i[12:14]
    sfz = h+'-'+j+'-'+k
    sfz_list.append(sfz)
# sfz_list[:5]
#星座判断
sdate=[20,19,21,20,21,22,23,23,23,24,23,22]     # 星座判断列表
conts =['摩羯座','水瓶座','双鱼座','白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座','摩羯座']
signs=['♑','♒','♓','♈','♉','♊','♋','♌','♍','♎','♏','♐','♑']
#构建新的数据列表
xm = list(df['name'])
xz = []
tx = []
for birth in sfz_list:
    cbir=birth.split('-')    # 分割年月日到列表
    cmonth=str(cbir[1])      # 提取月数据
    cdate=str(cbir[2])       # 提取日数据
    def sign(cmonth,cdate):  #  判断星座函数
        if int(cdate)<sdate[int(cmonth)-1]:   # 如果日数据早于对应月列表中对应的日期
            xz.append(conts[int(cmonth)-1])       # 直接输出星座列表对应月对应的星座
            tx.append(signs[int(cmonth)-1])       # 直接输出星座列表对应月对应的星座
        else:
            xz.append(conts[int(cmonth)])         # 否则输出星座列表下一月对应的星座
            tx.append(signs[int(cmonth)])         # 否则输出星座列表下一月对应的星座        
    sign(cmonth,cdate) 
# xm[:10],xz[:10],tx[:10]
#构建字典，将列表作为values
getlist = {
    '姓名' : xm,
    '星座' : xz,
    '图标' : tx,
    '出生日期' : sfz_list
}
dom = DataFrame(getlist)
dom.head(10)
# #保存为xlsx
# dom.to_excel('18电商星座表.xlsx')
#取出星座列，进行分组
dom1 = dom['星座'].value_counts().reset_index()
dom1.columns = ['星座统计','count']
# place_message = dom.groupby(['星座'])
# for index,i in place_message:
#     print(index,i)
#进行排序
dom2 = dom.sort_values(['星座'],ascending = False)
#进行表的数据列添加
dom['星座统计'] = dom1['星座统计']
dom['count'] = dom1['count']
dom['星座'] = dom2['星座']
#保存为xlsx
dom.to_excel('18电商星座表.xlsx')

#涉及知识：
'''
1.如何将列表作为数据列添加到dataframe-------------构建字典，key为列名，values为元素
2.如何对某一列进行排序，分组排序，分组统计等等-----------------dgroupby()
3.对行操作-------loc    如根据某一列的判断条件和    对列操作--------------iloc   下标
'''