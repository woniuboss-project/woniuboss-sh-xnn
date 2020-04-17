#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author:吴米珠
from homework.report.Apri_04_server import AppiumServer
from homework.report.April_04_client import APPClient
import threading,time,os


class StartTest:
    def __init__(self):
        self.server = AppiumServer()

    def test01(self):
        devices = self.server.get_devices_info()
        threads = []
        for i in range(len(devices)):
            app = APPClient(*devices[i][0:3])  #通过解包的方法将设备名称、版本号及客户端的端口号给到app
            server = threading.Thread(target=self.server.start_appium_server,args=(*devices[i],),name=f"sever-{i}")
            client = threading.Thread(target=app.test_01,name=f"cliet_{i}")
            threads.append(server)
            threads.append(client)
        threads.sort(key = lambda t :t.getName()[0:1])
        for t in threads:
            if t.getName() == "client-0":
                time.sleep(30)
            t.setDaemon(True)
            t.start()
        for t in threads:
            if t.getName().startswith("client"):
                t.join()
        os.system('taskkill /f /im node.exe')

if __name__ == '__main__':
    st = StartTest()
    st.test01()
