#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@time    : 2020/4/14 21:10
#@Author  : 小米
import time,os
from common.web import Web
from common.myddt import myddt
from action.action_login import Login
from action.action_common import Common
from selenium.webdriver.common.by import By



class loginCase:
    def __init__(self):
        self.login = Login()
        self.common = Common()

    def main_test(self):
        self.prepare()
        self.test_login()
        self.finish()

    def prepare(self):
        try:
            Web.show_wait(By.ID,"username",timeout=15)
        except:
            Web.open_page()

    def finish(self):
        time.sleep(2)
        Web.colse_browser()


    data_path = os.path.split(os.path.dirname(__file__))[0] + "/data/woniusales_data.xlsx"
    @myddt(data_path,"woniusales","login")
    def test_login(self,version, module, type, case_id, case_title, case_data, expect):
        try:
            time.sleep(1)
            self.login.do_login(case_data["username"],case_data["password"],case_data["verifycode"])
            if expect == "注销":
                time.sleep(1)
                self.common.do_loginout()
                Web.write_result(version,module,type,case_id,case_title,"成功")
            elif expect == "fail":
                time.sleep(1)
                self.login.do_fail()
                Web.write_result(version, module, type, case_id, case_title, "成功")
            else:
                Web.write_result(version, module, type, case_id, case_title, "失败",error="断言失败")
        except Exception as e:
            massage = str(e)
            Web.write_result(version, module, type, case_id, case_title, "失败",error=massage)

