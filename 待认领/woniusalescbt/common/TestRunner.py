#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@time    : 2020/4/15 15:59
#@Author  : 小米

import os


class GetMethods:
    def __init__(self):
        pass

    def FromClassName(self,module):
        case_list = dir(module)
        name = module()
        self.startup(module,name)
        for case in case_list:
            if case.startswith("test"):
                print("%s正在执行" % case)
                getattr(name,case)()
                self.teardonw(module,name)

    def FromMethodsName(self,module,methods):
        case_list = dir(module)
        name = module()
        self.startup(module, name)
        for case in case_list:
            for method in methods:
                if method == case:
                    print("%s正在执行" % case)
                    getattr(name,case)()
        self.teardonw(module, name)

    def startup(self,module,name):
        if hasattr(module,"prepare"):
            getattr(name,"prepare")()

    def teardonw(self,module,name):
        if hasattr(module,"finish"):
            getattr(name,"finish")()

    def AddTests(self,module):
        pass

    def AddTest(self, methods):
        pass

    def discover(self,path):
        filelist = []
        case_list = []
        for root, folders, filenames in os.walk(path):  # 通过给定路径获取该目录下的所有文件夹名和文件名(只有一层)
            for folder in folders:  # 遍历文件夹名的每一个，并且将期拼接成完整路径，准备递归查找
                filelist.append(os.path.join(root, folder))
            for filename in filenames:
                if filename.endswith("test") and filename.endswith(".py"):  # 如果要查找的文件名在遍历的文件中，将其添加到用例的列表中
                    case_list.append(filename)
        return case_list


