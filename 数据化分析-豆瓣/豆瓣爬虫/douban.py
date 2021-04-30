#豆瓣爬虫
import urllib.request
from bs4 import BeautifulSoup
import sqlite3
import re
import xlwt
#分析自己要获取数据的字段，在这里，分别是电影中文名称，电影英文名称，电影图片，评论，评价人数，电影链接，一句话概述，基本信息

Link = re.compile(r'<a href="(.*?)">')

def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    # urlAsk("")#首先是爬取一页,直接输入即可
    #保存数据
    #savepath = "豆瓣.xls"
    #saveData(datalist,savepath)
#爬虫请求 单页
def urlAsk(url):
    html = ""   #初始化
    # url = ""
    #用户代理请求 post
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.48"
    }
    req = urllib.request.Request(url,headers=header)    #这里可以测试状态码 200 正常 408？？？ 被检测为爬虫登录 防范网站反爬虫制
    response = urllib.request.urlopen(req)  #获取整个网页源码 
    html = response.read().decode("utf-8")  #这个编码是根据源码的编码格式来的，一般都是utf-8
    # print(html) #测试
    return html


#获取数据
def getData(baseurl):
    datalist = []
    #爬取循环
    for i in range(0,10):
        url = baseurl + str(i*25)   #这一步代表可以将url作为参数传到urlAsk()里面
        #urlAsk(url)
        html = urlAsk(url)
        #开始数据解析
        soup = BeautifulSoup(html,"html.parser")    #解析得到整个有格式化的网页，方便提取数据
        #print(soup)
        souplist = soup.find_all('div',class_="item")   #得到自己需要的数据
        #print(souplist)
        #细心分析，这得到的是25条数据，因此还可以细分
        for item in souplist:
            data = [] #最内层列表
            #print(item)
            item = str(item)
            #print(item)    #比较与上面的区别
            #re 正则表达式 观察该item,从中进行正则匹配
            link = re.findall(Link,item)[0]
            data.append(link)
            datalist.append(data)
    print(datalist)
    return datalist


#保存数据
def saveData(datalist,savepath):
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet("豆瓣电影")
    col = ("","","","","","","","")
    for i in range(0,8):
        worksheet.write(0,i,col[i])
    for i in range(0,250):
        data = datalist[i]
        for j in len(data):
            worksheet.write(i+1,j,data[j])
    workbook.save(savepath)





if __name__ == "__main__":

    main()
