from pyecharts.charts import Map  # 注意这里与老版本pyecharts调用的区别
from pyecharts import options as opts
import random
city = ['北京', '天津', '上海', '广州', '阿拉善盟', '株洲']
data_city = [(i, random.randint(100, 200)) for i in city]
china_city = (
    Map()
    .add(
        "",
        data_city,
        "china-cities",
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国市级地图"),
        visualmap_opts=opts.VisualMapOpts(
            min_=100,
            max_=200,
            is_piecewise=True
        ),
    )
    .render("中国地级市地图.html")
)