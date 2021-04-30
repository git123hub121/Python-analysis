from pyecharts import options as opts
from pyecharts.charts import Scatter
from pyecharts.faker import Faker
# c = (
#     Scatter()
#     .add_xaxis(Faker.choose())
#     .add_yaxis("商家A", Faker.values())
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="Scatter-VisualMap(Color)"),
#         visualmap_opts=opts.VisualMapOpts(max_=150),
#     )
#     .render("scatter_visualmap_color.html")
# )
sc = (
    Scatter()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Scatter-VisualMap(Size)"),
        visualmap_opts=opts.VisualMapOpts(type_="size", max_=150, min_=20),
    )
    .render("scatter_visualmap_size.html")
)
