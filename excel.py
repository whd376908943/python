# coding:utf-8

import xlrd


book = xlrd.open_workbook(r"E:\tomcat.xlsx")
# 返回sheet的总数
print "Sheet数量:", book.nsheets
# 返回sheet的名称，列表
print "Sheet名称:", book.sheet_names()
# 获取第1个Sheet
sh = book.sheet_by_index(0)
# 返回该Sheet的名称
print sh.name
# 返回该Sheet的行
print sh.nrows
# 返回该Sheet的列
print sh.ncols
# 输出第二行第三列的值
print sh.cell_value(1, 2)
# 遍历所有表单
for s in book.sheets():
    for r in range(s.nrows):
        print s.row(r)
