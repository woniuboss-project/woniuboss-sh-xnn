#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author:吴米珠

class RecordLog:
    def __init__(self):
        pass

    @classmethod
    def write(cls,x,y,action,content=""):
        with open(r"D:\woniu_project\woniuboss\report\log.txt",mode="a+") as file:
            cont = "在位置[%d,%d]处%s:%s\n" % (x, y,action,content)
            file.write(cont)
