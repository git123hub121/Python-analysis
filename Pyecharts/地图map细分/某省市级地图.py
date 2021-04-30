from pyecharts.charts import Map  # 注意这里与老版本pyecharts调用的区别
from pyecharts import options as opts
import random

prov_city = ['长沙市', '株洲市', '湘潭市', '衡阳市']
data_prov_city = [(i, random.randint(100, 200)) for i in prov_city]
province_city = (
    Map()
    .add("",
         data_prov_city,
         "湖南")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="某省地级市地图"),
        visualmap_opts=opts.VisualMapOpts(
            min_=100,
            max_=200,
            is_piecewise=True
        )
    )
    .render(path="某省地级市地图.html")
)