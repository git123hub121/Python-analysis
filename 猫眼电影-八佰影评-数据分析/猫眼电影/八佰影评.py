#-*- coding = uft-8 -*-
#@Time : 2020/8/30 1:24 下午
#@Author : 公众号 菜J学Python
#@File : 八佰影评.py

import requests
import json
import time
from fake_useragent import UserAgent
from datetime import datetime
from datetime import timedelta

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 获取数据，根据url获取
def get_page(url):
    headers = {'User-Agent':UserAgent(verify_ssl=False).random}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.text
    return None


# 处理数据
def parse_page(html):
    try:
        data = json.loads(html)['cmts']  # 将str转换为json
        #print(data)
        comments = []
        for item in data:
            comment = {
                'id': item['id'],
                'nickName': item['nickName'],
                'cityName': item['cityName'] if 'cityName' in item else '',  # 处理cityName不存在的情况
                'content': item['content'].replace('\n', ' ', 10),  # 处理评论内容换行的情况
                'score': item['score'],
                'startTime': item['startTime']
            }
            comments.append(comment)
        return comments
    except Exception as e:
        pass



# 存储数据，存储到文本文件
def save_data():
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取当前时间，从当前时间向前获取
    end_time = '2020-08-21 09:00:00'
    while start_time > end_time:
        url = 'http://m.maoyan.com/mmdb/comments/movie/346210.json?_v_=yes&offset=0&startTime=' + start_time.replace(' ', '%20')
        html = None
        try:
            html = get_page(url)
        except Exception as e:
            time.sleep(0.5)
            html = get_page(url)
        else:
            time.sleep(0.1)
        comments = parse_page(html)
        print(comments)
        try:
            start_time = comments[14]['startTime']  # 获得末尾评论的时间
            start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S') + timedelta(seconds=-1)  # 转换为datetime类型，减1秒，避免获取到重复数据
            start_time = datetime.strftime(start_time, '%Y-%m-%d %H:%M:%S')  # 转换为str
        except Exception as e:
            pass
        try:
            for item in comments:
                with open('comments.txt', 'a', encoding='utf-8') as f:
                    f.write(str(item['id']) + ',' + item['nickName'] + ',' + item['cityName'] + ',' + item['content'] + ',' + str(item['score']) + ',' + item['startTime'] + '\n')
        except Exception as e:
            pass

if __name__ == '__main__':
    save_data()