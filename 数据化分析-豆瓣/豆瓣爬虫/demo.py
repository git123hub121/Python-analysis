# #豆瓣电影top250-国家/地区电影数top10
# #不会数据分析，好烦

# bd = ["导演: 弗兰克·德拉邦特 Frank Darabont   主演: 蒂姆·罗宾斯 Tim Robbins /...1994 / 美国 / 犯罪 剧情","1"]
# info = bd[0].split("/")
# i = info[1].strip(".")
# j = info[2].strip()
# data = info[3].strip().split(" ")
# for i in data:
#     print(i)
# # print(data)
# # print(info)
# # print(i,j,z)
#-*- codeing = utf-8 -*-
#需求分析：爬取豆瓣电影Top250的基本信息，包括电影的名称、豆瓣评分、评价数、电影概况、电影链接等
import urllib.request
from bs4 import BeautifulSoup
import re
import xlwt
import sqlite3

def main():
    #1.爬取网页
    #2.解析数据
    #3.保存数据
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    #savepath = ".\\豆瓣电影TOP250.xls"
    #dbpath = "movie.db"
    #saveData(savepath,datalist)
    #saveData2DB(datalist,dbpath)
    #askURL("https://movie.douban.com/top250?start=0")

findLink = re.compile(r'<a href="(.*?)">')#创建正则表达式对象，表示规则
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S) #re.S让换行符包含在字符中
findTitle = re.compile(r'<span class="title">(.*?)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

#1.爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,1):#10次
        url =  baseurl + str(i*25)
        html = askURL(url)#保存获取到的网页源码
    #2.解析数据
        soup =BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):#查找符合要求的字符串
            #print(item)#测试，查看电影item全部信息
            data = []#保存一部电影的所有信息
            item = str(item)
            link = re.findall(findLink,item)[0]#通过正则表达式来查找指定的字符串
            data.append(link)
            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)
            titles = re.findall(findTitle,item)
            if(len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)#添加中文名
                otitle = titles[1].replace("/","")#去掉无关符号
                data.append(otitle)#添加外国名
            else:
                data.append(titles[0])
                data.append(' ')#外国名字留空，防止串位
            rating = re.findall(findRating,item)[0]
            data.append(rating)
            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)
            inq = re.findall(findInq,item)#存在可能不存在的情况
            if len(inq) != 0:
                inq = inq[0].replace("。","")#去掉句号
                data.append(inq)
            else:
                data.append(" ")
            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)#去掉br
            bd = re.sub('/'," ",bd)
            bd = re.findall(r"\d{4}",bd)[0]
            # print(bd)
            # datadb = []
            # datadb.append(bd.strip())
            # print(datadb)
            # info = datadb[0].split("/")
            # # print(info)
            # print(info[1].strip("."))
            
            data.append(bd)#去除前后的空格
            print(data)
            datalist.append(data)#处理好的一部电影信息放入datalist
    #print(datalist)
    return datalist
#得到一个指定的url的网页内容
def askURL(url):
    head = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43"
    }#用户代理，表示我们是什么浏览器
    request =  urllib.request.Request(url,headers=head)
    html =""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html
#3.保存数据
def saveData(savepath,datalist):
#1.excel保存
    print("save......")
    workbook = xlwt.Workbook(encoding="utf-8",style_compression=0)
    worksheet = workbook.add_sheet('豆瓣电影TOP250',cell_overwrite_ok=True)
    col = ("电影链接","图片链接","影片中文名","影片外国名","评分","评价数","概况","年份")
    for i in range(0,8):
        worksheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条" %(i+1))
        data = datalist[i]
        for j in range(0,8):
            worksheet.write(i+1,j,data[j])
    workbook.save(savepath)
#2.数据库保存
#用pycharm好一点！
def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur  = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
            insert into movie250(
            info_link,pic_link,cname,ename,score,rated,instroduction,info)
            values(%s)'''%",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()

def init_db(dbpath):
    #print("successfully")
    sql = '''
        create table movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        instroduction text,
        info text
        )
    '''
    conn = sqlite3.connect(dbpath)#创建数据库文件
    cursor = conn.cursor()#获取游标
    cursor.execute(sql)#执行数据库操作
    conn.commit()#提交数据库操作
    cursor.close()
    conn.close()

if __name__ == "__main__":#当程序执行时
#调用函数
    main()
    print("爬取完毕")



