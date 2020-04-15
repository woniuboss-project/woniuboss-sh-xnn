#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@time    : 2020/4/14 21:32
#@Author  : 小米

from common.send_email import SendEmail
from common.myzip import Myzip
from common.write_report import WriteReport
from test.testlogin import loginCase
from test.TestRunner import GetMethods



class Suite:
    def __init__(self):
        pass
        self.version = "woniusaes_v1"
        self.htmlreport = WriteReport()

    def start_test(self):
        suite = GetMethods()
        suite.FromClassName(loginCase)
        self.htmlreport.write_html(self.version)
        Myzip.compress_file(self.version)
        SendEmail.send_email(self.version)

if __name__ == '__main__':
    Suite().start_test()