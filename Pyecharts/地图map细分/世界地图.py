from pyecharts.charts import Map  # 注意这里与老版本pyecharts调用的区别
from pyecharts import options as opts
import random
country = ['China', 'Canada', 'France', 'Japan', 'Russia', 'USA']
data_world = [(i, random.randint(100, 200)) for i in country]
world = (
    Map()
    .add('', # 此处没取名，所以空着
    	data_world, # 数据
    	'world') # 地图类型
    .set_global_opts(
        title_opts=opts.TitleOpts(title='World Map'),
        visualmap_opts=opts.VisualMapOpts(
            max_=200,
            min_=100,
            is_piecewise=True)  # 定义图例为分段型，默认为连续的图例
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .render(path='世界地图.html')
)