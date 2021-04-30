#1.先将同学的数据从xsxl中保存到csv中，然后进行读取，制作map地图

import xlrd
import pandas as pd

list = []  # 定义一个空的列表，用于存放读出来的数据
def read_data(sheetname):  # 传入一个参数sheetname
    data = xlrd.open_workbook('sjxx.xlsx')  # 打开文件，指定路径
    table = data.sheet_by_name(sheetname)  # 获取表名
    rows = table.nrows  # 获取表的所有行

    '''
    循环读取表的所有行，并将读取到的数据添加到list列表中
    '''
    for row in range(1, rows):
        list.append(table.row_values(row))
    print(list)

read_data('sheet')  # 调用方法，并传入表名
#
#import os
# with open("sjxx.xlsx","rb",encoding="gbk") as f:
#     t = f.read()
import csv
with open("sjxx.csv","w") as f:
    writer = csv.writer(f)
    for row in list:
        writer.writerow(row)

df = pd.read_csv("sjxx.csv", encoding='gbk')

from pyecharts.charts import Map
from collections import Counter
from pyecharts.options.global_options import ThemeType
from pyecharts import options as opts
import random

provinces = Counter(df.地区分布)
print(provinces)
area = [(i[0],i[1]) for i in provinces.items()]
maps = (
        Map(init_opts=opts.InitOpts(
        theme=ThemeType.ROMANTIC
        ))
        .add("居住地", area, "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="电商一班同学地区分布"),
            legend_opts=opts.LegendOpts(is_show=False),
            visualmap_opts=opts.VisualMapOpts(max_=5, is_piecewise=True),
        )
    )

maps.render("中国地图.html")