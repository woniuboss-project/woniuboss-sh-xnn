#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author:吴米珠


#以下是装饰器在类中的使用
def Myddt(filename):                                #外层用来传递装饰器本身的参数
    def wapper(func):                               #中间层用来传参函数
        def inner(self):                            #当装饰器装饰的是类方法时，必须传递self实例参数，否则，不能传递
            with open(filename) as file:
                lines_list = file.readlines()
            for line in lines_list:                 #写在在with open 平行的位置,意味着withopen结束了,关闭了
               list = line.strip().split(",")
               func(self,*list)   #在实参处对序列化(如列表,元组)表示将该序列化数据展开后对应的形参的位置上参数,也就相当于有几个参数就传几个参数

        return inner
    return wapper

