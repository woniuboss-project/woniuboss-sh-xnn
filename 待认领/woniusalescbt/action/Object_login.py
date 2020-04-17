#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@time    : 2020/4/14 20:49
#@Author  : 小米
from common.web import Web
from selenium.webdriver.common.by import By


class ObjectLogin:
    def __init__(self):
        self.driver = Web.get_driver()

    def username_text(self):
        element = Web.show_wait(By.ID, "username")
        element.clear()
        return element

    def password_text(self):
        element = Web.show_wait(By.ID, "password")
        element.clear()
        return element

    def verifycode_text(self):
        element = Web.show_wait(By.ID, "verifycode")
        element.clear()
        return element

    def login_button(self):
        element = Web.show_wait(By.XPATH, "/html/body/div[4]/div/form/div[6]/button")
        return element

    def login_fail_button(self):
        element = Web.show_wait(By.XPATH, "/html/body/div[6]/div/div/div[3]/button")
        return element
