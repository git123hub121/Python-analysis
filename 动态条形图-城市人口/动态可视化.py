# %%
import os
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML

# %%

df = pd.read_csv(
    'https://gist.githubusercontent.com/johnburnmurdoch/4199dbe55095c3e13de8d5b2e5e5307a/raw/fa018b25c24b7b5f47fd0568937ff6c04e384786/city_populations',
    usecols=['name', 'group', 'year', 'value'])
df.head(5)

# %%

current_year = 2018
dff = (df[df['year'].eq(current_year)]
       .sort_values(by='value', ascending=True)
       .head(10))
dff

# %%

fig, ax = plt.subplots(figsize=(15, 8))
ax.barh(dff['name'], dff['value'])

# %%

colors = dict(zip(
    ['India', 'Europe', 'Asia', 'Latin America',
     'Middle East', 'North America', 'Africa'],
    ['#adb0ff', '#ffb3ff', '#90d595', '#e48381',
     '#aafbff', '#f7bb5f', '#eafb50']
))
group_lk = df.set_index('name')['group'].to_dict()

# %%

fig, ax = plt.subplots(figsize=(15, 8))
dff = dff[::-1]  # 从上到下翻转值
# 将颜色值传递给`color=`
ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']])
# 遍历这些值来绘制标签和值(Tokyo, Asia, 38194.2)
for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
    ax.text(value, i, name, ha='right')  # Tokyo: 名字
    ax.text(value, i - .25, group_lk[name], ha='right')  # Asia: 组名
    ax.text(value, i, value, ha='left')  # 38194.2: 值
# 在画布右方添加年份
ax.text(1, 0.4, current_year, transform=ax.transAxes, size=46, ha='right')

# %%

fig, ax = plt.subplots(figsize=(15, 8))


def draw_barchart(year):
    dff = df[df['year'].eq(year)].sort_values(by='value', ascending=True).tail(10)
    ax.clear()
    ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']])
    dx = dff['value'].max() / 200
    for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
        ax.text(value - dx, i, name, size=14, weight=600, ha='right', va='bottom')
        ax.text(value - dx, i - .25, group_lk[name], size=10, color='#444444', ha='right', va='baseline')
        ax.text(value + dx, i, f'{value:,.0f}', size=14, ha='left', va='center')
    # ... polished styles
    ax.text(1, 0.4, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(0, 1.06, 'Population (thousands)', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 1.12, 'The most populous cities in the world from 1500 to 2018',
            transform=ax.transAxes, size=24, weight=600, ha='left')
    #     ax.text(1, 0, 'by QIML', transform=ax.transAxes, ha='right',
    #             color='#777777', bbox=dict(facecolor='white', alpha=0.8, edgecolor='white'))
    plt.box(False)


draw_barchart(2018)

# %%
import subprocess as sp

fig, ax = plt.subplots(figsize=(15, 8))
plt.rcParams['animation.ffmpeg_path']=r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"
animator = animation.FuncAnimation(fig, draw_barchart, frames=range(1968, 2019))
HTML(animator.to_jshtml())

# animator.to_html5_video()

Writer = animation.writers['ffmpeg']  # 需安装ffmpeg
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
animator.save('city.mp4',writer = writer)

# animator.save('city.gif',writer='imagemagick')