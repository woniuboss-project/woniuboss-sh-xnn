#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author:吴米珠
from find_image.Imageauto import ImageAuto
from myddt.myddt import Myddt
import time


class Login:
    def __init__(self):
        self.find = ImageAuto(wait=1)
        time.sleep(1)
        self.find.start_web(r"D:\Web\Firefox\firefox.exe","http://boss:8080/WoniuBoss2.5/")
        time.sleep(1)

    @Myddt(r"D:\woniu_project\woniuboss\test_data\login.csv")
    def do_login(self,test_number,username,password,verifycode):
        time.sleep(1)
        self.find.input(r"..\login_image\uname.png",username)
        self.find.input(r"..\login_image\upass.png",password)
        self.find.input(r"..\login_image\verifycode.png",verifycode)
        self.find.click(r"..\login_image\login.png")
        time.sleep(1)
        if self.find.exists(r"..\login_image\loginout.png"):
            print("%s:pass" % test_number)
            self.find.click(r"..\login_image\loginout.png")
        else:
            if self.find.exists(r"..\login_image\uname_error.png") or \
                self.find.exists(r"..\login_image\uapss_error.png") or \
                    self.find.exists(r"..\login_image\code_error.png"):
                print("%s:pass" % test_number)
                time.sleep(1)
                self.find.click(r"..\login_image\refresh.png")
                self.find.key_enter()
            else:
                print("%s:fail" % test_number)


if __name__ == '__main__':
    l = Login()
    l.do_login()
