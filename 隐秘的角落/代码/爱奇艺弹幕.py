# 导入包
import requests
import pandas as pd
import zlib
import re
import time


def get_aiqiyi_danmu(tvid):
    """
    功能：给定tvid，获取爱奇艺一集的弹幕评论信息
    """
    # 建立空df
    df_all = pd.DataFrame()

    # 初始page_num
    page_num = 1

    while True:
        # 打印进度
        print(f'正在获取第{page_num}页的弹幕数据')

        try:
            # 获取URL
            url = f'https://cmts.iqiyi.com/bullet/{str(tvid)[-4:-2]}/{str(tvid)[-2:]}/{str(tvid)}_300_{page_num}.z'

            # 添加headers
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
            }

            # 发起请求
            try:
                r = requests.get(url, headers=headers, timeout=3)
            except Exception as e:
                print(e)
                r = requests.get(url, headers=headers, timeout=3)

            # 转换为arrry
            zarray = bytearray(r.content)

            # 解压字符串
            xml = zlib.decompress(zarray, 15+32).decode('utf-8')

            # 用户名
            name = re.findall('<name>(.*?)</name>', xml)
            # 评论ID
            contentId = re.findall('<contentId>(.*?)</contentId>', xml)
            # 评论信息
            content = re.findall('<content>(.*?)</content>', xml)
            # 展示时间
            showTime = re.findall('<showTime>(.*?)</showTime>', xml)
            # 点赞次数
            likeCount = re.findall('<likeCount>(.*?)</likeCount>', xml)

            # 保存数据
            df_one = pd.DataFrame({
                'name': name,
                'contentId': contentId,
                'content': content,
                'showTime': showTime,
                'likeCount': likeCount
            })

            # 循环追加
            df_all = df_all.append(df_one, ignore_index=True)

            # 休眠一秒
            time.sleep(1)

            # 页数+1
            page_num += 1

        except Exception as e:
            print(e)
            break

    return df_all


# 抓包获取视频tvid
tvid_list = [9000000005439200, 9000000005442600, 9000000005447000, 9000000005448200, 9000000005450200,
             9000000005451900, 16954202800, 16954268600, 16954335100, 16954390400,
             16954467500, 16954519300]

episodes_list = ['第一集 ', '第二集', '第三集', '第四集', '第五集',
                 '第六集', '第七集', '第八集', '第九集', '第十集',
                 '第十一集', '第十二集'
                 ]

# 循环获取所有集数据
for tvid, episodes in zip(tvid_list, episodes_list):
    print(tvid, episodes)
    # 获取数据
    df = get_aiqiyi_danmu(tvid=tvid)
    # 插入列
    df.insert(0, 'episodes', episodes)
    # 导出数据
    df.to_csv(f'./data/df_{episodes}.csv')
