from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

map = (
    Map()
    .add("中国地图", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
    .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"))
)
map.render()

