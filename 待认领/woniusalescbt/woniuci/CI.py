#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@time    : 2020/4/14 21:42
#@Author  : 小米
import os,time
from common.get_config import Get
from module.suite import Suite


class WoniusalesCI:
    def __init__(self):
        self.tomcat = Get.get_config_value("ci","tomcat")
        self.svn_folder = Get.get_config_value("ci","svn_folder")
        self.svn_url = Get.get_config_value("ci","svn_url")
        self.svn_username = Get.get_config_value("ci","svn_username")
        self.svn_password = Get.get_config_value("ci","svn_password")

    #获取源代码
    def svn(self):
        is_exists_file = os.path.exists(r"%s\build.xml" % self.svn_folder)
        if is_exists_file:
            os.system(r"svn update %s --username %s --password %s" % (self.svn_folder,self.svn_username,self.svn_password))
            print("源代码更新完成")
        else:
            os.system(r"svn checkout %s %s --username %s --password %s" %(self.svn_url,self.svn_folder,self.svn_username,self.svn_password))
            print("源代码下载完成")

    #利用ANT编译和构建源代码并打包为：war包
    def ant(self):
        os.system(r"ant -f %s\build.xml" % self.svn_folder)
        if os.path.exists(r"%s\woniusales.war" % self.svn_folder):
            print("源代码已经成功构建")
        else:
            print("源代码构建失败")

    # 停止Tomcat
    def shutdown_Tomcat(self):
        os.system(r"%s\bin\shutdown.bat" % self.tomcat)
        print("Tomcat服务器已停止")

    # 启动Tomcat
    def startup_Tomcat(self):
        os.system(r"%s\bin\startup.bat" % self.tomcat)
        print("Tomcat服务器启动成功")

    #部置更新的项目到Tomcat服务器端
    def deploy(self):
        self.shutdown_Tomcat() #先将Tomcat停掉
        time.sleep(3)
        os.system(r"rmdir /s /Q %s\webapps\woniusales" % self.tomcat)  #删除woniusales文件夹，强制删除
        print("已删除woniusales文件夹")
        os.system(r"del /Q /F %s\webapps\woniusales.war" % self.tomcat)   #删除旧的war
        print("已删除woniusales.war包")
        os.system(r"copy %s\woniusales.war %s\webapps" % (self.svn_folder,self.tomcat)) #复制新的Tomcat到webapps目录下
        time.sleep(2)
        self.startup_Tomcat() #非阻塞的方式启动Tomcat，不会影响后续代码执行
        time.sleep(10)

    #更新配置文件
    def update_properites(self):
        content = "db_url=jdbc:mysql://localhost:3306/woniusales?useUnicode=true&characterEncoding=utf8\n"
        content += "db_username=root\n"
        content += "db_password=123456\n"
        content += "db_driver=com.mysql.jdbc.Driver\n"
        with open(r"%s\webapps\woniusales\WEB-INF\classes\db.properties" % self.tomcat,"w") as file:
            file.write(content)
        print("db.properties更新成功")
        time.sleep(2)

    def update_verifycode(self):
        os.system(r"del /Q /F %s\webapps\woniusales\WEB-INF\classes\com\woniucx\control\UserController.class" % self.tomcat)  #删除旧的验证码文件
        print("验证码文件已删除")
        os.system(r"copy %s\code\UserController.class %s\webapps\woniusales\WEB-INF\classes\com\woniucx\control" % (self.tomcat, self.tomcat))
        print("万能验证码文件已替换")

    def tomcat_restart(self):
        self.shutdown_Tomcat()
        time.sleep(1)
        self.startup_Tomcat()
        time.sleep(15)
        print("Tomcat重启成功")

    #进行测试
    def test(self):
        Suite().start_test()


    #整个运行的入口
    def run(self):
        self.svn()
        self.ant()
        self.deploy()
        self.update_properites()
        self.update_verifycode()
        self.tomcat_restart()
        self.test()


if __name__ == '__main__':
    ci = WoniusalesCI()
    ci.run()