#coding=gbk
from tools.service import Service
from selenium import webdriver

class Login:
    #��ʼ��driver
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost:8080/WoniuBoss/login')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)


    # ���û����������������
    def input_uname(self, username):
        uname = self.driver.find_element_by_name('userName')
        uname.clear()
        uname.send_keys(username)

    # ���������������
    def input_upass(self, password):
        upass = self.driver.find_element_by_name('userPass')
        upass.clear()
        upass.send_keys(password)

    # ����֤���������֤��
    def input_vfcode(self, verifycode):
        vfcode = self.driver.find_element_by_name('checkcode')
        vfcode.clear()
        vfcode.send_keys(verifycode)

    # �����¼��ť
    def click_button(self):
        self.driver.find_element_by_css_selector('.btn').click()

    # �����ϵĶ���������֯���γ�����ĵ�¼����,����login_data���ֵ�
    def do_login(self):
        self.input_uname('WNCD056')
        self.input_upass('woniu123')
        self.input_vfcode('0000')
        self.click_button()
if __name__ == '__main__':
    L=Login()
    L.do_login()