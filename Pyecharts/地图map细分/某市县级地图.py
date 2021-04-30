from pyecharts.charts import Map  # 注意这里与老版本pyecharts调用的区别
from pyecharts import options as opts
import random

counties = (
    Map()
    .add(
        "",
        [['祁阳县', 1]],
        "永州",
        label_opts=opts.LabelOpts(is_show=False)
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国某市区县地图"),
        visualmap_opts=opts.VisualMapOpts(),
    )
    .render("某市的区县地图.html")
)