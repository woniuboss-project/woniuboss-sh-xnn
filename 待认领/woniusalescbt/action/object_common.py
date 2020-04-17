#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@time    : 2020/4/14 21:05
#@Author  : 小米
from common.web import Web
from selenium.webdriver.common.by import By

class ObjectCommon:
    def __init__(self):
        self.driver = Web.get_driver()

    def loginout_link(self):
        element = Web.show_wait(By.PARTIAL_LINK_TEXT, "注销")
        return element

