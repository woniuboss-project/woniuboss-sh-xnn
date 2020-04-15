#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@time    : 2020/4/10 21:40
#@Author  : 小米
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os,time,smtplib



class SendEmail:
    def __init__(self):
        pass

    @classmethod
    def send_email(cls,project):
        senders = "2424076343@qq.com"
        receviers = ["2065967035@qq.com"]
        message = MIMEMultipart()
        test_time = time.strftime("%Y-%m-%d")
        message.attach(MIMEText("woniusales测试报告-%s" % test_time,"text","utf-8"))
        message["Subject"] = Header("第三次测试，请查收，谢谢!","utf-8")
        addr_path = os.path.split(os.path.dirname(__file__))[0] + r"\report\%s_report.zip" % project
        with open(addr_path,"rb") as f:
            attach = MIMEApplication(f.read())
        attach.add_header("Content-Disposition","addr_path",filename= os.path.basename(addr_path))
        message.attach(attach)
        try:
            smtp_obj = smtplib.SMTP()
            smtp_obj.connect("smtp.qq.com", 587)
            smtp_obj.login("2424076343@qq.com", "knlyeximgwuedhhf")
            smtp_obj.sendmail(senders, receviers, message.as_string())
            print("邮件发送成功")
        except Exception as e:
            print("邮件发送失败")


# if __name__ == '__main__':
#     SendEmail.send_email("woniusaes_v1")

