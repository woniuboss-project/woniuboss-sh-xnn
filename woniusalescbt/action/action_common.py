#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@time    : 2020/4/14 21:09
#@Author  : 小米

from action.object_common import ObjectCommon

class Common:
    def __init__(self):
        self.common = ObjectCommon()


    def do_loginout(self):
        self.common.loginout_link().click()