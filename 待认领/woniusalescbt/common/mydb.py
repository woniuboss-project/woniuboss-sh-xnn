#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@time    : 2020/4/10 21:39
#@Author  : 小米
import pymysql

class Mydb:
    def __init__(self,):
        self.con = pymysql.connect(user="root", password="123456", host="localhost", db="woniucbt", charset="utf8")
        self.cur = self.con.cursor(pymysql.cursors.DictCursor)

    def query_one(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

    def query_all(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def update(self,sql):
        try:
            self.cur.execute(sql)
            self.con.commit()
        except Exception as e :
            return "数据更新异常：%s " % str(e)

    def write_test_result(self,version,module, type, case_id, case_title, result, test_time, error, screenshot):
            sql = "insert into report(version,module,type,case_id,case_title,result,time,error,screenshot) values('%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (version,module, type, case_id, case_title, result, test_time, error, screenshot)
            self.cur.execute(sql)
            self.con.commit()

    def read_test_result(self,value):
        sql = "select * from report where version='%s'" % (value)
        test_data = ''
        return test_data


    def __del__(self):
        self.cur.close()
        self.con.close()


# if __name__ == '__main__':
    # import os
    # cap_path = os.path.split(os.path.dirname(__file__))[0]+ "/screenshot/aa.png"
    # print(cap_path)
    # Mydb().update("insert into test values('%s');"%cap_path)
