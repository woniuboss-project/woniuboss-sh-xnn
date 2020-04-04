#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author:吴米珠
import time
from appium import webdriver

class APPClient:
    # 启动客户端
    def __init__(self, deviceName, platformVesion, port):
        caps = {
            "platformName": "Android",
            "platformVersion": platformVesion,
            "automationName": "UiAutomator1",
            "deviceName": "appium",
            "udid": deviceName,
            "appPackage": "com.miui.calculator",
            "appActivity": ".cal.CalculatorActivity",
            "unicodeKeyboard": "true",  # 允许键盘输入中文
        }
        url = f"http://127.0.0.1:{port}/wd/hub"
        driver = webdriver.Remote(url,caps)
        driver.implicitly_wait(12)
        self.driver = driver

    def test_01(self, first_number, operator, second_number, expect):
        driver = self.driver
        time.sleep(2)
        try:
            driver.tap([(396,794)])   #根据坐标位置单击
            driver.find_element_by_id(f"com.miui.calculator:id/btn_{first_number}_s").click()
            driver.find_element_by_accessibility_id(operator).click()  # 识别content_desc的id
            driver.find_element_by_id(f"com.miui.calculator:id/btn_{second_number}_s").click()
            driver.find_element_by_accessibility_id("等于").click()
            time.sleep(5)
            result = driver.find_element_by_id("result").text
            actual = result.split(" ")[1]
            if actual == expect:
                print("测试成功")
            else:
                print("测试失败")
        except Exception as e:
            print(e)
        finally:
            time.sleep(2)
            driver.quit()



# if __name__ == '__main__':
#     from homework.report.Apri_04_server import AppiumServer
#     server = AppiumServer()
#     result = server.get_devices_info()
#     print(result)
#     time.sleep(10)
#     at = APPClient(*result[0][0:3])
#     at.test_01(5,"加",6,"11")
