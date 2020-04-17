#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@time    : 2020/4/11 10:14
#@Author  : 小米
#以下有两种数据格式的方法，推荐使用json格式，列表加元组格式的代码也是OK的，装饰器中调用的方法改一下就行。
import xlrd


#对测试数据的内容进行单独处理
def date_deal(st):
    case_data = {}
    temp = (st.strip().split("\n"))
    for i in range(len(temp)):
        data = temp[i].split("=")
        case_data[data[0]] = data[1]
    return case_data


#将excel中的所有数据处理为json格式[{},{},{}]
def get_dict(file_name,sheetname,modulename):
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_name(sheetname)
    rows, cols = sheet.nrows, sheet.ncols
    data_list = []
    for i in range(1,rows):
        dict = {}
        if modulename in sheet.cell_value(i, 3):
            for j in range(cols):
                key = sheet.cell_value(0,j)
                content = sheet.cell_value(i, j)
                if j == 5:
                    content = date_deal(content)
                dict[key]= content
            data_list.append(dict)
    return data_list



def myddt(filename,sheetname,modulename):
    def warapper(func):
        def innter(self):
            result = get_dict(filename,sheetname,modulename)
            for item in result:
                func(self,**item)
        return innter
    return warapper







# if __name__ == '__main__':
#     import os
#     result = get_dict(r"../data/boss_data.xlsx" ,"train", "login")
#     print(result)


''' 
以下是列表加元组格式代码：
#将excel中的所有数据处理为列表加元组的格式[(),(),()]
def get_tup(file_name,sheetname,modulename):
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_name(sheetname)
    rows, cols = sheet.nrows, sheet.ncols
    data_list = []
    for i in range(1, rows):
        li = []
        if modulename in sheet.cell_value(i, 3):
            for j in range(cols):
                content = sheet.cell_value(i, j)
                if j == 5:
                    temp = content.strip().split("\n")
                    data = [temp[i].split("=")[1] for i in range(len(temp))]
                    content = tuple(data)
                li.append(content)
            data_list.append(tuple(li))
    return data_list
'''