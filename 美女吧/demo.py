import requests
from bs4 import BeautifulSoup
import pymysql
import time
result = []

for t in range(250):
    print('第{0}页'.format(t+1))
    url='https://tieba.baidu.com/f?kw=明星&ie=utf-8&pn={0}'.format(t*50)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
    }
    response = requests.get(url, header)
    soup = BeautifulSoup(response.text, 'html.parser')
    items_content = soup.find_all('a', class_='j_th_tit')  #内容
    items_user = soup.find_all('span', class_='tb_icon_author ')  #昵称
    items_comment = soup.find_all(class_='threadlist_rep_num center_text')  #跟帖数量
    for i, j, k in zip(items_content, items_user, items_comment):
        result.append([i.get('title'), j.get('title')[5:], k.text])
    time.sleep(1)
conn=pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='',
    db='test1',
    charset='utf8mb4'
)
cur = conn.cursor()
#如果存在TIEBA表，则删除
cur.execute("DROP TABLE IF EXISTS STAR")
#创建TIEBA表
sql = """
    create table STAR(
    title char(255),
    author char(100),
    num char(20))
"""
cur.execute(sql)
for i in result:
    cur.execute("INSERT INTO STAR(title,author,num) VALUES ('{0}', '{1}','{2}')".
                format(i[0].replace('\'','').replace('\"','').replace('\\',''), i[1], i[2]))
conn.commit()