import json
import sqlite3
import xlrd
import xlsxwriter
from classmates_zscg import Addclassmate

def readExcel():
    try:
        in_wb = xlrd.open_workbook('classmates.xlsx')
    except:
        print("文件读取错误")
    ws = in_wb.sheet_by_index(0)
    ls = []
    for i in range(ws.nrows):
        ls.append(ws.row_values(i))
    print("读取Excel成功")
    return ls

def writeSqlite(ls):
    try:
        conn = sqlite3.connect('cm.db')
        cur = conn.cursor()
    except:
        print("数据库连接错误")
        droptable_sql = 'drop table if exists cmtable'
        cur.execute(droptable_sql)
    cur.execute('''create table cmtable(
        '学号' text primary key not null,
        '姓名' text not null,
        '电话' text not null,
        '邮箱' text not null,
        '地址' text not null
        );''')
    for i in range(len(ls)-1):
        sqlstr = 'insert into cmtable(学号,姓名,电话,邮箱,地址)values(?,?,?,?,?)'
        cur.execute(sqlstr,(ls[i+1][0], ls[i+1][1], ls[i+1][2], ls[i+1][3], ls[i+1][4]))
        conn.commit()
        cur.close()
        conn.close()
        print('创建数据库成功')

def main():
    ls = readExcel()
    writeSqlite(ls)
    ls1 = ['006','刘泽名','18875375938','1123459978@qq.com','贵州']
    ls2 = '007'
    ls3 = '姓名'
    ls4 = '刘志森'
    ls5 = '007'

    Addclassmate.selectInfo()

    Addclassmate.insertInfo(ls1)
    Addclassmate.selectInfo()
    Addclassmate.deteleInfo(ls2)
    Addclassmate.selectInfo()
    Addclassmate.updateInfo(ls3,ls4,ls5)
    Addclassmate.selectInfo()

if __name__ == '__main__':
    main()
#感觉这个CSDN的作者没有写完，靠！