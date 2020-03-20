import random,time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



class Server:

    #向指定无素输入内容
    @classmethod
    def send_input(cls,driver,by,element,value):
        '''
        :param driver:
        :param by:通过什么方式定位,例如,通过id定位
        :param element:定位的值 ,这里需要写id的值
        :param value:输入框需要输入的内容
        :return:无返回值
        '''
        ele = driver.find_element(by,element)
        ele.click()
        ele.clear()
        ele.send_keys(value)

    #单击指定元素
    @classmethod
    def click_element(cls,driver,by,element):
        driver.find_element(by,element).click()

    #随机下拉框的选择
    @classmethod
    def select_random(cls,driver,by,value,selector=None):
        '''
        :param driver:
        :param by:通过什么方式定位,例如,通过id定位
        :param value:定位的值 ,这里需要写id的值
        :param selector:,默认为None,代表着是随机选择,如果想指定,可以直接传入选择框内的值
        :return:无返回值
        '''

        ele = driver.find_element(by,value)                         #定位到指定的下拉框
        ele_length = len(Select(ele).options)                       #获取下拉框的长度
        if selector != None:
            selector = Select(ele).select_by_visible_text(selector)
        else:
            random_index = random.randrange(1,ele_length)                 #将下拉框的长度作为随机下标的范围
            selector = Select(ele).select_by_index(random_index)        #选择随机下标的元素


    #去附只读功能
    @classmethod
    def remove_readonly(cls, driver, ele_id):
        driver.execute_script('document.getElementById("%s").readOnly=false' % (ele_id))


    #随机选中一个选择框
    @classmethod
    def random_one(cls,driver):
        table = driver.find_element_by_xpath("//*[@id='personal-table']/tbody")
        tr = table.find_elements_by_tag_name("tr")


    # 解密
    @classmethod
    def decryption(self,driver):
        Server.click_element(driver,By.ID, "btn-decrypt")
        Server.send_input(driver,By.CSS_SELECTOR, "div.modal-body:nth-child(2) > input:nth-child(1)", "woniu123")
        Server.click_element(driver,By.CSS_SELECTOR,"#secondPass-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)")

    #登录
    @classmethod
    def login(cls,driver):
        cls.send_input(driver,By.NAME,"userName","WNCD000")
        cls.send_input(driver,By.NAME,"userPass","woniu123")
        cls.click_element(driver,By.CSS_SELECTOR,".btn")
        time.sleep(0.5)
        Server.decryption(driver)





# if __name__ == '__main__':
#     driver.get("http://xiaomi:8080/WoniuBoss2.5/")
#     Server.send_input(By.CSS_SELECTOR,"div.row:nth-child(1) > input:nth-child(1)","WNCD000")
#     Server.send_input(By.CSS_SELECTOR,"div.row:nth-child(2) > input:nth-child(1)","woniu123")
#     driver.find_element(By.CSS_SELECTOR,".modal-footer").click()
#     time.sleep(2)
#     Server.select_random(By.ID,"poolSelect")
#     Server.random_one()
