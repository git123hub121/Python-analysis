#自行创建一个“Address.xlsx”班级通讯录表格文件，表格中包含学号、姓名、电话、邮箱、地址等信息，并在表格中输入至少5行数据记录。编写Python程序，完成将Excel表格文件的通讯录信息导入到sqlite3数据库中。
#编写一个AddressBook类，类中包含selectInfo,insertInfo,deleteInfo,updateInfo等四个函数用于实现对数据库中通讯录的增删查改操作。
#实例化AddressBook类的对象，使用本人信息测试完成对通讯录的数据处理操作
import json
import  sqlite3
import xlrd
import xlsxwriter

class Addclassmate():
    """该类有selectInfo,insertInfo,deleteInfo,updateInfo等
        四个函数用于实现对数据库中通讯录的增删查改操作"""
    def selectInfo(slef):
        try:
            conn = sqlite3.connect('cm.db')
            cur = conn.cursor()
        except:
            print("数据库连接错误")

        try:
            result = cur.execute('select * from cmtable')
            for row in result:
                print('{},{},{},{},{}'.format(*row))#应该是啥用法吧！
        except Exception as e:
            return False
        print("查询数据库完成")
        cur.close()
        conn.close()

    def insertInfo(ls1):
        try:
            conn = sqlite3.connect('cm.db')
            cur = conn.cursor()
        except:
            print("数据库连接错误")

        try:
            sqlstr = 'insert into cmtable(学号,姓名,电话,邮箱,地址)values(?,?,?,?,?)'
            cur.execute(sqlstr,(ls1[0],ls1[1],ls1[2],ls1[3],ls1[4]))
        except Exception as e:
            return False
        finally:
            conn.commit()
        cur.close()
        conn.close()
        print("增加数据库完成")

    def updateInfo(ls1,ls2,ls3):
        try:
            conn = sqlite3.connect('cm.db')
            cur = conn.cursor()
        except:
            print("数据库连接错误")
        try:
            if ls1 == '姓名':
                sqlstr ='''update cmtable set 姓名 = ? where 学号 = ?'''
            elif ls1 == '电话':
                sqlstr = '''update cmtable set 电话 = ? where 学号 = ?'''
            elif ls1 == '邮箱':
                sqlstr = '''update cmtable set 邮箱 = ? where 学号 = ?'''
            elif ls1 == '地址':
                sqlstr = '''update cmtable set 地址 = ? where 学号 = ?'''
            else:
                print('失败')
                return False
            cur.execute(sqlstr,(ls2,ls3))
        except Exception as e:
            return False
        finally:
            conn.commit()
        conn.commit()
        cur.close()
        conn.close()
        print("修改数据库完成")

    def deteleInfo(ls1):
        try:
            conn = sqlite3.connect('cm.db')
            cur = conn.cursor()
        except:
            print("数据库连接错误")
        try:
            sqlstr = '''detele from cmtable where 学号=？'''
            cur.execute(sqlstr,[(ls1)])
        except Exception as e:
            return False
        finally:
            conn.commit()
        cur.close()
        conn.close()
        print("删除数据库完成")
