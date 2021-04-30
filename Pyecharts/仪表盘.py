from pyecharts import options as opts
from pyecharts.charts import Gauge

g = (
    Gauge()
    .add("", [("完成率", 80)])
    .set_global_opts(title_opts=opts.TitleOpts(title="Gauge-基本示例"))

)
g.render()

