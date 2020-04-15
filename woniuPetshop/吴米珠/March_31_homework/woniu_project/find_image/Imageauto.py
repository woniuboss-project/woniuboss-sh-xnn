#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author:吴米珠

import time,os
import cv2 as cv
from PIL import ImageGrab
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from find_image.record_log import RecordLog

class ImageAuto:
    def __init__(self,wait=1):
        self.mouse = PyMouse()
        self.keyboard = PyKeyboard()
        self.wait = wait

    #图像匹配:参数为:模版图片的(由于模版图片每次不一样,所以要做为参数传参)
    def find_image(self,filename):
        ImageGrab.grab().save("./screen.png")  # 通过ImageGrab的方法对当前屏幕截图
        source = cv.imread("./screen.png")  # 打开屏幕截图,也就是大图
        template = cv.imread(filename)  # 打开模版图片,也就是小图
        result = cv.matchTemplate(source,template,cv.TM_CCOEFF_NORMED)  #参数为、把大图、小图、算法
        location = cv.minMaxLoc(result)
        pos_start = location[3]  # 获取匹配度最高所对应的坐标,也就是小图的左顶点在大图中的位置
        x = int(pos_start[0]) + int(template.shape[1] / 2)
        y = int(pos_start[1]) + int(template.shape[0] / 2)
        similarity = location[1]  # 拿到匹配度最高的那个值来做判断
        if similarity >= 0.85:
            return (x, y)
        else:
            return -1, -1

    #单击,参数为模版图片,因为要利用模版图片来进行匹配，匹配成功后对得到的坐标进行单击
    def click(self,filename):
        x,y = self.find_image(filename)
        self.mouse.click(x,y)
        time.sleep(self.wait)
        RecordLog.write(x,y,"单击")
        time.sleep(self.wait)

    # 双击,参数为模版图片,因为要利用模版图片来进行匹配，匹配成功后对得到的坐标进行单击
    def double_click(self, filename):
        x, y = self.find_image(filename)
        self.mouse.click(x, y,n=2)
        time.sleep(self.wait)
        RecordLog.write(x, y, "双击")
        time.sleep(self.wait)

    #输入,参数为模版图片及输入的内容
    def input(self,filename,content):
        x,y = self.find_image(filename)
        self.mouse.click(x,y,n=2)        #双击选中文本框
        self.keyboard.press_key(self.keyboard.backspace_key)  #清空内容
        self.keyboard.release_key(self.keyboard.backspace_key) #松开
        time.sleep(self.wait)
        self.keyboard.type_string(content)
        time.sleep(self.wait)
        RecordLog.write(x, y, "输入",content=content)
        time.sleep(self.wait)

    #回退键
    def key_backspace(self):
        self.keyboard.press_key(self.keyboard.backspace_key)
        self.keyboard.release_key(self.keyboard.backspace_key)
        time.sleep(self.wait)

    #回车键
    def key_enter(self):
        self.keyboard.press_key(self.keyboard.enter_key)
        self.keyboard.release_key(self.keyboard.enter_key)
        time.sleep(self.wait)

    #上键--参数n为次数
    def key_up(self,n=1):
        for i in range(n):
            self.keyboard.press_key(self.keyboard.up_key)
            self.keyboard.release_key(self.keyboard.up_key)
            time.sleep(self.wait)

    #下键--参数n为次数
    def key_down(self,n=1):
        for i in range(n):
            self.keyboard.press_key(self.keyboard.down_key)
            self.keyboard.release_key(self.keyboard.down_key)
            time.sleep(self.wait)

    #F5刷新
    def key_F5(self):
        self.keyboard.press_key(self.keyboard.function_keys[5])
        self.keyboard.release_key(self.keyboard.function_keys[5])
        time.sleep(self.wait)

    #移动
    def move(self,filename):
        x,y = self.find_image(filename)
        self.mouse.move(x,y)
        self.mouse.click(x,y)
        RecordLog.write(x, y, "移动并单击")


    #下拉框的操作
    def select(self,filename,n=1):
        x,y = self.find_image(filename)
        self.mouse.click(x,y)
        self.key_down(n=n)
        self.key_enter()

    #启动应用程序
    def start_app(self,cmd):
        os.system("start /b " + cmd)
        time.sleep(self.wait*3)


    def start_web(self,type,url):
        os.system("start /b %s %s" % (type,url))
        time.sleep(self.wait)

    #断言
    def exists(self,filename):
        time.sleep(self.wait)
        x,y = self.find_image(filename)
        if (x,y) == (-1,-1):
            return False
        else:
            return True




