#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@time    : 2020/4/10 21:40
#@Author  : 小米
import os
import time
from common.mydb import Mydb

class WriteReport:
    def __init__(self):
        self.pdpc = Mydb()

    def get_test_data(self,version):
        pdpc = self.pdpc
        title = (pdpc.query_one("select count(*) from report where version='%s';" % version))["count(*)"]
        success = (pdpc.query_one("select count(*) from report where version='%s' and result='成功';"% version))["count(*)"]
        fail = (pdpc.query_one("select count(*) from report where version='%s' and result='失败';"% version))["count(*)"]
        error = (pdpc.query_one("select count(*) from report where version='%s' and result='错误';"% version))["count(*)"]
        time_sql = "select time from report where version='%s' order by time desc limit 1;" % version
        last_time = pdpc.query_one(time_sql)["time"]
        test_result = (pdpc.query_all("select * from report where version='%s';"% version))
        return title,success,fail,error,last_time,test_result

    # 将测试结果写入html报告
    def write_html(self,version):
        title,success,fail,error,last_time,test_result = self.get_test_data(version)
        test_time = time.strftime("%Y-%m-%d")
        content = ""
        for result in test_result:
            content += "<tr>\n"
            content += "<td width=6%% align=center>%s</td>\n" % (result['id'])
            content += "<td width=7%% align=center>%s</td>\n" % (result['module'])
            content += "<td width=8%% align=center>%s</td>\n" % (result['type'])
            content += "<td width=10%%>%s</td>\n" % (result['case_id'])
            content += "<td width=21%%>%s</td>\n" % (result['case_title'])
            test_result = result['result']
            if test_result == "成功":
                content += "<td width=6%% bgcolor=#C1FFE4 align=center>%s</td>\n" % test_result
            elif test_result == "错误":
                content += "<td width=6%% bgcolor=#FFF4C1 align=center>%s</td>\n" % test_result
            else:
                content += "<td width=6%% bgcolor=#FFD9EC align=center>%s</td>\n" % test_result
            content += "<td width=14%% align=center>%s</td>\n" % (result['time'])
            content += "<td width=20%% align=center>%s</td>\n" % (result["error"])
            screen = result["screenshot"]
            if screen == "无":
                content += "<td width=8%% align=center>%s</td>\n" % (result["screenshot"])
            else:
                content += "<td width=8%% align=center><a href='%s'>查看图片</a></td>\n" % (result["screenshot"])
            content += "</tr>\n"
        html_result = self.write_table(test_time,version,title, success, fail, error, last_time, content)
        html_path = os.path.split(os.path.dirname(__file__))[0]
        with open((html_path +"\\report\\%s_%s测试报告.html")% (version,test_time), mode="w+", encoding="utf-8") as file:
            file.write(html_result)

    def write_table(self,test_time, version, title,success, fail, error, last_time, content):
        project = version.split("_")[0]
        table = f'''
                         <!DOCTYPE html>
                         <html>
                         <head>
                             <meta charset="UTF-8">
                             <title>测试报告</title>
                         </head>
                         <body style="margin-top: 20px; font-family: '微软雅黑';">
                         <table border="1" cellspacing="0" cellpadding="5" width="95%" align="center">
                             <tr bgcolor="#CAFFFF" style="font-size: 30px;">
                                 <td height="60" colspan="6" align="center"> {project}-自动化测试报告: {test_time} </td>
                             </tr>
                             <tr style="font-size: 20px;">
                                 <td width="20%">被测版本：{version} </td>
                                 <td width="15%">总用例： {title} 个</td>
                                 <td width="10%">成功： {success} 个</td>
                                 <td width="10%">失败： {fail} 个</td>
                                 <td width="10%">错误： {error} 个</td>
                                 <td width="35%">最后时间： {last_time} </td>
                             </tr>
                         </table>
                         <p/>
                         <table border="1" cellspacing="0" cellpadding="5" width="95%" align="center">
                             <tr height="40" bgcolor="#CAFFFF">
                                 <td width="6%" align="center">记录编号</td>
                                 <td width="7%" align="center">所属模块</td>
                                 <td width="8%" align="center">测试类型</td>
                                 <td width="10%" align="center">用例编号</td>
                                 <td width="21%" align="center">用例描述</td>
                                 <td width="6%" align="center">测试结果</td>
                                 <td width="14%" align="center">运行时间</td>
                                 <td width="20%" align="center">错误消息</td>
                                 <td width="8%" align="center">现场截图</td>
                             </tr>
                             <!-- 此处只需要定义一个变量，用于循环代替即可 -->
                             {content}
                         </table>
                         </body>
                         </html>
                         '''
        return table


# if __name__ == '__main__':
#   w = WriteReport()
  # w.get_test_data("WoniuBoss_2.5")

  # w.write_html("WoniuBoss_2.5")