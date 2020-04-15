#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author:吴米珠

# 由于被测应用一般都比较固定,所以暂定写死
# self.package = os.popen(f"aapt dump badging {app_path} | findstr pack").read().split("'")[1]
# self.Activity = os.popen(f"aapt dump badging {app_path} | findstr launch").read().split("'")[1]


import os,socket
class AppiumServer:
    def get_devices_info(self):
        # 定义初始端口号
        port,bp_port = 5000,8000
        # 获取所有的设备信息
        info = os.popen("adb devices").read().strip().split("\n")
        devices_info = []
        #遍历每个设备名称,通过设备名称来获取版本号,调用查找可用端口的方法,将这些信息添加到列表中,以便后期的调用
        for i in range(1, len(info)):
            if info[i] != "":
                deviceName = info[i].split("\t")[0]
                platformVesion = os.popen(f"adb -s {deviceName} shell getprop ro.build.version.release").read().strip()
                port = self.find_port(port)
                bp_port = self.find_port(bp_port)
                devices_info.append((deviceName, platformVesion, port, bp_port))
        return devices_info

    # 定义可以查找设备可用端口的方法
    def find_port(self, port):
        while self.check_port(port):
            port += 1
            return port

    # 检查端口号是否被占用
    def check_port(self, port):
        con = socket.socket()
        result = con.connect_ex(("127.0.0.1", port))
        if result == "0":
            con.shutdown(socket.SHUT_RDWR)
            return False
        else:
            return True

    # 启动appium服务器
    def start_appium_server(self, deviceName, platformVesion, port, bp_port):
        log_path = os.path.join(os.getcwd(), f"D:\\woniu_project\\homework\\report\\{deviceName}_appium.log")
        if self.check_port(port):
            cmd = f'appium -p {port} -bp {bp_port} --device-name {deviceName} --platform-version {platformVesion} --log {log_path} --log-level info --log-timestamp'
            os.popen(cmd)


# if __name__ == '__main__':
# #     servier = AppiumServer()
# #     result = servier.get_devices_info()
# #     servier.start_appium_server(*result[0])