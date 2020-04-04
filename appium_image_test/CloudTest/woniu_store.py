from appium import webdriver
import os,time



class woniu_store:
    def __init__(self,device_name,platform_version,port):
        #定义apk所在的路径
        app_path = os.path.join(os.getcwd(),r'F:\appium\gui_tools\app\apk\com.ccsuper.snailshop_3.8.1_139.apk')
        self.device_name = device_name
        self.desired_caps = {
            # 'automationName':'Uiautomator1',
            'platformName': 'Android',
            'platformVersion' :platform_version,
            'deviceName': self.device_name, #这个参数主要用于模拟器，如果是真机建议将这个键名换成udid
            'appPackage':'com.ccsuper.snailshop',
            'appActivity':'com.ccsuper.snailshop.view.activity.SignInActivity',
            'app': app_path, #能够自动安装指定路径下的应用
            'unicodeKeyboard':'true'#用于在测试中输入中文
        }
        self.url = f'http://127.0.0.1:{port}/wd/hub'
    def start_test(self):
        driver = webdriver.Remote(self.url, self.desired_caps)
        try:
            driver.implicitly_wait(120)
            #注意find_element_by_android_uiautomator方法使用的时候引号的特点，必须外单内双，
            #因为内部的字符串将来会被当作java代码由android系统来执行，而java的字 符串不认单引号
            phone = driver.find_element_by_android_uiautomator('text("手机号")')
            phone.send_keys('15238899225')

            driver.find_element_by_id('ed_sign_in_password').send_keys('a805791737')
            driver.find_element_by_android_uiautomator('text("开启蜗牛小店")').click()
            driver.find_element_by_android_uiautomator('text("支出")').click()
            driver.find_element_by_android_uiautomator('text("记一笔")').click()
            driver.find_element_by_android_uiautomator('text("餐饮")').click()
            driver.find_element_by_android_uiautomator('text("0.00")').click()
            driver.find_element_by_android_uiautomator('text("0.0")').send_keys('168')
            driver.find_element_by_android_uiautomator('text("确定")').click()
            driver.find_element_by_android_uiautomator('text("保存")').click()
            type = driver.find_elements_by_id('tv_expend_name')
            money = driver.find_elements_by_id('tv_expend_price')
            if type[0].text == '餐饮' and money[0].text == '168.00':
                print('测试成功')
            else:
                print('测试失败')

        finally:
            driver.quit()

        #     remarks = driver.find_elements_by_id('account_item_txt_remark')
        #     money = driver.find_elements_by_id('account_item_txt_money')
        #     if remarks[0].text == '出去玩' and money[0].text == '-236':
        #         print('测试成功')
        #     else:
        #         print('测试失败')
        # except Exception as e:
        #     with open(os.path.join(os.getcwd(),'report/%s.log' % self.device_name),'w') as f:
        #         f.write(str(e) + '\n')
        #
        #     now = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        #     driver.get_screenshot_as_file(os.path.join(os.getcwd(),f'report/{self.device_name}_{now}.png'))
        # finally:
        #     driver.quit()
#
if __name__ == '__main__':
    woniu_store('127.0.0.1:21503','5.1.1',4723).start_test()
