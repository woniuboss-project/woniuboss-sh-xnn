#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@time    : 2020/4/15 15:59
#@Author  : 小米

class GetMethods:
    def __init__(self):
        pass

    def FromClassName(self,module):
        case_list = dir(module)
        name = module()
        for case in case_list:
            if case.startswith("test"):
                print("%s正在执行" % case)
                getattr(name,case)()


    def FromMethodsName(self,module,methods):
        case_list = dir(module)
        name = module()
        for case in case_list:
            for method in methods:
                if method == case:
                    print("%s正在执行" % case)
                    getattr(name,case)()

