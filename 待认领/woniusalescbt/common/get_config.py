#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@time    : 2020/4/14 16:36
#@Author  : 小米
import os
from configparser import ConfigParser

class Get:

    #使用configparser方法获取配置文件的内容
    @classmethod
    def get_config_value(cls,section,key):
        from configparser import ConfigParser
        config = ConfigParser()
        config_path = os.path.split(os.path.dirname(__file__))[0] +"/config/woniusales.conf"
        # config.read(config_path)
        config.read('../data/woniusales.conf')
        return config.get(section,key)


# if __name__ == '__main__':
#     Get.get_config_value("")