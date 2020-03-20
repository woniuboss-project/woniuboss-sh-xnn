from selenium.webdriver.common.by import By
from woniuboss.tools.server import Server


class Resources_Query:
    def __init__(self,driver):
        self.driver = driver

    #选择资源库
    def select_pool(self,selector=None):
        Server.select_random(self.driver,By.ID,"poolSelect",selector=selector)

    #选择咨询师
    def select_empname(self,selector=None):
        Server.select_random(self.driver, By.ID, "empNameSelect", selector=selector)

    # 选择状态
    def select_status(self, selector=None):
        Server.select_random(self.driver, By.ID, "Select", selector=selector)

    #选择来源
    def select_source(self, selector=None):
        Server.select_random(self.driver, By.ID, "sourceSelect", selector=selector)


    #输入查询时间
    def input_time(self,start_date,end_date):
        driver = self.driver
        Server.remove_readonly(driver,"date1")
        Server.send_input(driver,By.ID,"date1",start_date)
        Server.remove_readonly(driver,"date2")
        Server.send_input(driver, By.ID, "date2", end_date)

    #向搜索框输入内容
    def input_query(self,content):
        Server.send_input(self.driver,By.CSS_SELECTOR,"div.col-lg-12:nth-child(4) > input:nth-child(3)",content)

    #点击搜索
    def click_search(self):
        Server.click_element(self.driver,By.CSS_SELECTOR,"div.col-lg-12:nth-child(4) > button:nth-child(4)")


