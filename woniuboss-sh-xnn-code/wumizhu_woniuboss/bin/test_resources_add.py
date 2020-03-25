import time,unittest
from selenium import webdriver
from woniuboss.tools.util import Util
from parameterized import parameterized
from woniuboss.tools.server import Server
from woniuboss.lib.resources_add import Resources_Add


path ="..\\data\\demo.xlsx"
sheetname="resources"
add_data = Util.excel_tup(path,sheetname,"add")
query_data = Util.excel_tup(path,sheetname,"query")

class Test_Resources_Add(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver = getattr(webdriver,"Firefox")()
        driver.maximize_window()
        driver.get("http://192.168.1.8:8080/WoniuBoss2.5/")
        driver.implicitly_wait(3)
        Server.login(driver)
        cls.driver = driver

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.close()


    @parameterized.expand(add_data)
    def test_add(self,tel,name,status,email,qq,school,major,intent,salary,applposition,age,eduexp,experience,last_tracking_remark,expect):
        add = Resources_Add(self.driver)
        time.sleep(0.5)
        add.add_source(tel,name,status,email,qq,school,major,intent,salary,applposition,age,eduexp,experience,last_tracking_remark)
        print(expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)