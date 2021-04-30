from pyecharts.charts import Map  # 注意这里与老版本pyecharts调用的区别
from pyecharts import options as opts
import random
province = ['广东', '湖北', '湖南', '四川', '重庆', '黑龙江', '浙江', '山西']
data_province = [(i, random.randint(100, 200)) for i in province]
# print(data)
china_province = (
    Map()
    .add('', data_province, 'china')
    .set_global_opts(
        title_opts=opts.TitleOpts(title='Provinces of China'),
        visualmap_opts=opts.VisualMapOpts(
            min_=100,
            max_=200,
            is_piecewise=True)
    )
    .render(path='中国省级地图.html')
)