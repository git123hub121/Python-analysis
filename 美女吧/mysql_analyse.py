
import pandas as pd
from sqlalchemy import create_engine
from pyecharts import Bar
# 初始化数据库连接，使用create_engine模块
engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/test1')
# 查询语句，选出TIEBA表中的所有数据
sql = ''' select * from STAR; '''
# read_sql_query的两个参数: sql语句， 数据库连接
df = pd.read_sql_query(sql, engine)
# 输出TIEBA表的查询结果
df['num']=[int(i) for i in list(df['num'])]
df=df.drop_duplicates(subset=['title','author','num'], keep='first')

'''#发帖数量排名
rank_num={}
for i in list(set(list(df['author']))):
    rank_num[i.replace(' ', '')] = list(df['author']).count(i)
rank_num = sorted(rank_num.items(), key=lambda x: x[1], reverse=True)
bar = Bar("柱状图", "发帖数量-昵称")
bar.add("发帖数量-昵称", [i[0] for i in rank_num[:20]], [i[1] for i in rank_num[:20]],
        xaxis_rotate=45, mark_line=["average"], mark_point=["max", "min"])
bar.render('发帖数量-昵称.html')'''

#跟帖数量排名
dff=df.sort_values(by='num', ascending=False).head(20)
bar = Bar('跟帖数量排名',width=1000,height=1000)
bar.use_theme('dark')
bar.add('' ,dff['title'][::-1], dff['num'][::-1], is_convert=True, is_yaxis_inverse=False, xaxis_rotate=45,is_label_show=True,label_pos='right')
bar.render("跟帖数量排名.html")
'''import matplotlib.pyplot as plt
import jieba
from wordcloud import wordcloud
text=''
for i in list(df['title']):
    text+=i
print(text)
cut_text = jieba.cut(text)
result=[]
for i in cut_text:
    result.append(i)
result = " ".join(result)
wc = wordcloud.WordCloud(
    font_path='C:\Windows\Fonts\FZBWKSJW.TTF',  # 字体路径
    background_color='white',  # 背景颜色
    width=1000,
    height=600,
    max_font_size=1000,  # 字体大小
    min_font_size=10,
    mask=plt.imread('水滴.jpg'),  # 背景图片
    max_words=100000)
wc.generate(result)
wc.to_file('result.png')  # 图片保存
'''


