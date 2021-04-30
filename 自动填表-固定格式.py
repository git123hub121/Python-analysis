import xlwings as xw
app=xw.App(visible=True,add_book=False)
workbook=app.books.open(r'D:\数据分析\人员信息.xlsx')
sheet=workbook.sheets[0]    #选中第一个表格
info = sheet.used_range
#nrows = info.last_cell.row
#ncols = info.last_cell.column
list_cell=['B1','D1','F1','H1','B2','D2','F2','H2']
for i in info.raw_value[1:]:
    print(i)
    app=xw.App(visible=True,add_book=False)
    workbook=app.books.open(r'D:\数据分析\个人信息模板.xlsx')
    sheet=workbook.sheets[0]
    sheet['B1'].value=i[0]
    sheet['D1'].value=i[1]
    sheet['F1'].value=i[8]
    sheet['H1'].value=i[2]
    sheet['B2'].value=i[9]
    sheet['D2'].value=i[5]
    sheet['F2'].value=i[6]
    sheet['H2'].value=i[7]
    for j in list_cell:
        sheet[j].api.Font.Name='楷体'   #设置字体
        sheet[j].api.Font.Size=14      #设置字号
        #设置文本水平对齐方式为居中
        sheet[j].expand('table').api.HorizontalAlignment=xw.constants.HAlign.xlHAlignCenter
        #设置文本水平对齐方式为居中
        sheet[j].expand('table').api.VerticalAlignment=xw.constants.VAlign.xlVAlignCenter
    workbook.save(r'D:\数据分析\{}.xlsx'.format(i[0]))
    workbook.close()
    app.quit()

#https://mp.weixin.qq.com/s?__biz=Mzg3NjMzMjc5OQ==&mid=2247484338&idx=1&sn=f9332dd153bc715e97c90a2b0996e3bf&chksm=cf329022f845193478eef860f9ebd9b3761a464073e1cc07df69d4e106ad9356c466f8b9e0e3&scene=21#wechat_redirect
#不给数据，我玩个锤子