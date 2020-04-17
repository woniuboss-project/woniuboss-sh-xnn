#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@time    : 2020/4/10 21:41
#@Author  : 小米
import time,os
from selenium import webdriver
from common.mydb import Mydb
from selenium.webdriver.support.wait import WebDriverWait


class Web:
    driver = None

    @classmethod
    def get_driver(cls,browser="chrome"):
        if cls.driver is None:
            if browser == "chrome" or browser =="gc":
                cls.driver = webdriver.Chrome()
            elif browser == "firefox" or browser == "ff":
                cls.driver = webdriver.Firefox()
            else:
                cls.driver = webdriver.Ie()
        cls.driver.maximize_window()
        return cls.driver

    # 关闭浏览器
    @classmethod
    def colse_browser(cls):
        cls.driver.close()

    #打开首页
    @classmethod
    def open_page(cls):
        cls.driver.get("http://localhost:8080/woniusales")

    #页面刷新
    @classmethod
    def refresh(cls):
        cls.driver.refresh()



    #退出浏览器
    @classmethod
    def quit_browser(cls):
        cls.driver.quit()
        cls.driver = None

    #查找元素
    @classmethod
    def show_wait(cls,by,value,timeout=5):
        try:
            element = WebDriverWait(cls.driver,timeout).until(lambda driver:driver.find_element(by,value))
            return element
        except Exception as e:
            return  str(e)

    #判断元素是否存在
    @classmethod
    def element_exists(cls,by,value,timeout=15):
        try:
            WebDriverWait(cls.driver, timeout).until(lambda driver:driver.find_element((by, value)))
            return True
        except:
            return False


    #截图
    @classmethod
    def screencap(cls,version):
        now_time = int(time.time())
        now_path = os.path.split(os.path.dirname(__file__))[0] + r"/report/"
        image= "bug_image/%s_%s.png" % (version,now_time)
        cap_path = now_path + image
        cls.driver.get_screenshot_as_file(cap_path)
        return image


    #将测试结果写入数据库
    @classmethod
    def write_result(cls, version,module,type,case_id,case_title,result,error="无"):
        if result == "成功":
            screenshot = "无"
        else:
            screenshot = cls.screencap(version)
        test_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        Mydb().write_test_result(version,module,type,case_id,case_title,result,test_time,error,screenshot)

    # 相等断言
    @classmethod
    def assert_equa(cls, actual, expect):
        if actual == expect:
            return True
        else:
            return False



