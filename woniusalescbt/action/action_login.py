#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@time    : 2020/4/14 21:07
#@Author  : 小米
import time
from common.web import Web
from action.Object_login import ObjectLogin


class Login:
    def __init__(self):
        self.login = ObjectLogin()

    def do_login(self,username,password,verifycode):
        Web.open_page()
        self.login.username_text().send_keys(username)
        self.login.password_text().send_keys(password)
        self.login.verifycode_text().send_keys(verifycode)
        self.login.login_button().click()
        time.sleep(1)

    def do_fail(self):
        self.login.login_fail_button().click()