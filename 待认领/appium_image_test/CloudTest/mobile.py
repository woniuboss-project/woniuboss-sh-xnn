import os, time, subprocess, socket, threading

from CloudTest.one_stroke import OnestrokeTest


class MobileCloud:
    def get_device_info(self):
        port = 5000
        bp_port = 8000
        device_list = []
        #获取当前设备列表
        devices = subprocess.check_output('adb devices').decode().strip().split('\r\n')
        devices.pop(0)#剔除首行无用表头
        for item in devices:
            if item != '':#避免没有设备连接时代码报错
                device_name = item.strip().split('\t')[0]
                print(device_name)
                platformVersion = subprocess.check_output(
                    f'adb -s {device_name} shell getprop ro.build.version.release').decode().strip()
                print(platformVersion)

                port = self.find_port(port)
                bp_port = self.find_port(bp_port)
                #将准备好的设备信息添加到设备列表
                device_list.append((device_name,platformVersion,port,bp_port))
                port += 1
                bp_port += 1
        return device_list

    def find_port(self,port):
        while self.check_port(port):
            port +=1
        return port

    def check_port(self,port):
        con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            con.connect(('127.0.0.1',port))
            con.shutdown(socket.SHUT_RDWR)
            return True
        except socket.error:
            return False

    #定义一个启动APPium server的方法(appium -p5000 -bp8000 --device-name 127.0.0.1:21503
    # --platform-version 5.1.1 --log filepath --log-level info --log-timestamp)
    def start_appium_server(self,device_name,platform_version,port,bp_port):
        log_path = os.path.join(os.getcwd(),f'report/{device_name}_appium.log')
        cmd = f'appium -p {port} -bp {bp_port} --device-name {device_name} --platform-version {platform_version} --log {log_path} --log-level info --log-timestamp'
        os.system(cmd)

    def start_test(self):
        devices = self.get_device_info()
        threads = []
        for i in range(len(devices)):
            # ost = OnestrokeTest(devices[i][0],devices[i][1],devices[i][2])
            ost = OnestrokeTest(*devices[i][0: 3])
            server_thread = threading.Thread(target=self.start_appium_server,args=(*devices[i],), name=f'server-{i}')
            client_thread = threading.Thread(target=ost.start_test, name=f'client-{i}')
            threads.append(server_thread)
            threads.append(client_thread)

        threads.sort(key=lambda thread: thread.getName()[0: 1], reverse=True)
        for thread in threads:
            if thread.getName() == 'client-0':
                time.sleep(10)
            #设置守护线程,代表这个线程不重要,只要主线程结束,这个线程就可以结束了
            thread.setDaemon(True)
            thread.start()
        for thread in threads:
            if thread.getName().startswith('client'):
                thread.join()
        os.system('taskkill /f /im node.exe')
        print('全部测试工作完成')


if __name__ == '__main__':
    MobileCloud().start_test()
    # print(devices)