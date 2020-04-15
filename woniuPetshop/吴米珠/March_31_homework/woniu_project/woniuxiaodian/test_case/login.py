#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author:吴米珠
import time
from myddt.myddt import Myddt
from find_image.Imageauto import ImageAuto


class Login:
    def __init__(self):
        self.find = ImageAuto(wait=1)
        time.sleep(1)
        self.find.start_web(r"D:\Web\Firefox\firefox.exe","https://snailpet.com/index")
        time.sleep(1)

    @Myddt(r"D:\woniu_project\woniuxiaodian\test_data\login.txt")
    def do_login(self,test_number,phone,password):
        find = self.find
        time.sleep(4)
        find.input(r"..\login_image\phone.png",phone)
        find.input(r"..\login_image\pass.png",password)
        find.click(r"..\login_image\login.png")
        time.sleep(1)
        if find.exists(r"..\login_image\loginout.png"):
            find.click(r"..\login_image\loginout.png")
            find.click(r"..\login_image\loginout_ok.png")
            time.sleep(5)
            find.key_F5()
            time.sleep(2)
            print("%s:pass" % test_number)
        else:
            if find.exists(r"..\login_image\login_error.png"):
                time.sleep(1)
                find.key_F5()
                print("%s:pass" % test_number)
            else:
                print("%s:fail" % test_number)
if __name__ == '__main__':
    l = Login()
    l.do_login()

