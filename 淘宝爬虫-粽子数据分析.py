# 导包
import pandas as pd
import numpy as np
import re

#%%

# 导入爬取得到的数据
df = pd.read_csv("粽子.csv", engine='python', encoding='utf-8-sig', header=None)
df.columns = ["商品名", "价格", "付款人数", "店铺", "发货地址"]
df.head(10)

#%%

# 去除重复值
df.drop_duplicates(inplace=True)

#%%

# 处理购买人数为空的记录
df['付款人数']=df['付款人数'].replace(np.nan,'0人付款')

#%%

# 提取数值
df['num'] = [re.findall(r'(\d+\.{0,1}\d*)', i)[0] for i in df['付款人数']]  # 提取数值
df['num'] = df['num'].astype('float')  # 转化数值型
# 提取单位（万）
df['unit'] = [''.join(re.findall(r'(万)', i)) for i in df['付款人数']]  # 提取单位（万）
df['unit'] = df['unit'].apply(lambda x:10000 if x=='万' else 1)
# 计算销量
df['销量'] = df['num'] * df['unit']

#%%

# 删除无发货地址的商品，并提取省份
df = df[df['发货地址'].notna()]
df['省份'] = df['发货地址'].str.split(' ').apply(lambda x:x[0])

#%%

# 删除多余的列
df.drop(['付款人数', '发货地址', 'num', 'unit'], axis=1, inplace=True)

# 重置索引
df = df.reset_index(drop=True)
df.head(10)
#df.to_csv('清洗完成数据.csv')

#%%

df1 = df.sort_values(by="价格", axis=0, ascending=False)
df1.iloc[:5,:]

#%% md

## 数据可视化

#%% md

### 分词

#%%

import jieba
import jieba.analyse

txt = df['商品名'].str.cat(sep='。')

# 添加关键词
jieba.add_word('粽子', 999, '五芳斋')

# 读入停用词表
stop_words = []
with open('stop_words.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        stop_words.append(line.strip())

# 添加停用词
stop_words.extend(['logo', '10', '100', '200g', '100g', '140g', '130g'])

# 评论字段分词处理
word_num = jieba.analyse.extract_tags(txt,
                                      topK=100,
                                      withWeight=True,
                                      allowPOS=())

# 去停用词
word_num_selected = []

for i in word_num:
    if i[0] not in stop_words:
        word_num_selected.append(i)

key_words = pd.DataFrame(word_num_selected, columns=['words','num'])

#%% md

### 查询你的pyecharts版本

#%%

import pyecharts

print(pyecharts.__version__)

#%% md

### 商品销量排名top10 - 柱形图

#%%

# 导入包
from pyecharts.charts import Bar
from pyecharts import options as opts

# 计算top10店铺
shop_top10 = df.groupby('商品名')['销量'].sum().sort_values(ascending=False).head(10)

# 绘制柱形图
bar0 = Bar(init_opts=opts.InitOpts(width='1350px', height='750px'))
bar0.add_xaxis(shop_top10.index.tolist())
bar0.add_yaxis('sales_num', shop_top10.values.tolist())
bar0.set_global_opts(title_opts=opts.TitleOpts(title='粽子商品销量Top10'),
                     xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
                     visualmap_opts=opts.VisualMapOpts(max_=shop_top10.values.max()))
bar0.render("粽子商品销量Top10.html")

#%% md

### 店铺销量排名top10 - 柱形图

#%%

# 导入包
from pyecharts.charts import Bar
from pyecharts import options as opts

# 计算top10店铺
shop_top10 = df.groupby('店铺')['销量'].sum().sort_values(ascending=False).head(10)

# 绘制柱形图
bar1 = Bar(init_opts=opts.InitOpts(width='1350px', height='750px'))
bar1.add_xaxis(shop_top10.index.tolist())
bar1.add_yaxis('sales_num', shop_top10.values.tolist())
bar1.set_global_opts(title_opts=opts.TitleOpts(title='粽子店铺销量Top10'),
                     xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
                     visualmap_opts=opts.VisualMapOpts(max_=shop_top10.values.max()))
bar1.render("粽子店铺销量Top10.html")

#%% md

### 全国省份销量地区分布-地图

#%%

from pyecharts.charts import Map

# 计算销量
province_num = df.groupby('省份')['销量'].sum().sort_values(ascending=False)

# 绘制地图
map1 = Map(init_opts=opts.InitOpts(width='1350px', height='750px'))
map1.add("", [list(z) for z in zip(province_num.index.tolist(), province_num.values.tolist())],
         maptype='china'
        )
map1.set_global_opts(title_opts=opts.TitleOpts(title='各省份粽子销量分布'),
                     visualmap_opts=opts.VisualMapOpts(max_=300000),
                     toolbox_opts=opts.ToolboxOpts()
                    )
map1.render("各省份粽子销量分布.html")

#%% md

### 不同价格区间的销量占比

#%%

from pyecharts.charts import Pie

def price_range(x): #按照淘宝推荐划分价格区间
    if x <= 22:
        return '22元以下'
    elif x <= 115:
        return '22-115元'
    elif x <= 633:
        return '115-633元'
    else:
        return '633元以上'

df['price_range'] = df['价格'].apply(lambda x: price_range(x))
price_cut_num = df.groupby('price_range')['销量'].sum()
data_pair = [list(z) for z in zip(price_cut_num.index, price_cut_num.values)]
print(data_pair)


# 饼图
pie1 = Pie(init_opts=opts.InitOpts(width='1350px', height='750px'))
# 内置富文本
pie1.add(
        series_name="销量",
        radius=["35%", "55%"],
        data_pair=data_pair,
        label_opts=opts.LabelOpts(formatter='{{b}—占比{d}%}'),
)

pie1.set_global_opts(legend_opts=opts.LegendOpts(pos_left="left", pos_top='30%', orient="vertical"),
                     toolbox_opts=opts.ToolboxOpts(),
                     title_opts=opts.TitleOpts(title='不同价格区间的粽子销量占比'))

pie1.render("不同价格区间的粽子销量占比.html")

#%% md

### 商品标题文本分析 - 词云图

#%%

from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType

# 词云图
word1 = WordCloud(init_opts=opts.InitOpts(width='1350px', height='750px'))
word1.add("", [*zip(key_words.words, key_words.num)],
          word_size_range=[20, 200],
          shape=SymbolType.DIAMOND)
word1.set_global_opts(title_opts=opts.TitleOpts('粽子商品名称词云图'),
                      toolbox_opts=opts.ToolboxOpts())
word1.render("粽子商品名称词云图.html")

#%% md

## 关注公众号

#%%

img_src = 'http://note.youdao.com/yws/public/resource/8171065fb7d978eb589a16c6a64d70f4/xmlnote/WEBRESOURCEf000a60369f9467f8e4eff640b2159ff/3904'
from skimage import io
image = io.imread(img_src)
io.imshow(image)
io.show()

#%%


