import PyPDF2
import pdfplumber

# with pdfplumber.open("chapter.pdf") as p:
#     page = p.pages[2]
#     print(page.extract_text())
#只能适合单一的文字排版

# from openpyxl import Workbook
#
# with pdfplumber.open("chapter.pdf") as p:
#     page = p.pages[13]
#     table = page.extract_table()
# print(table)
#
# workbook = Workbook()
# sheet = workbook.active
# for row in table:
#     sheet.append(row)
# workbook.save(filename = "pdf.xlsx")
#只能适合符合excel模式的表

