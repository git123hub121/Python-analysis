import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker

c = (
    Line()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values(), is_smooth=True)
    .add_yaxis("商家B", Faker.values(), is_smooth=True)
    .set_global_opts(title_opts=opts.TitleOpts(title="Line-smooth"))

)
c.render()