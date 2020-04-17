from appium import webdriver
import os,time



class OnestrokeTest:
    def __init__(self,device_name,platform_version,port):
        #定义apk所在的路径
        app_path = os.path.join(os.getcwd(),'yibijizhang.apk')
        self.device_name = device_name
        self.desired_caps = {
            # 'automationName':'Uiautomator1',
            'platformName': 'Android',
            'platformVersion' :platform_version,
            'deviceName': self.device_name, #这个参数主要用于模拟器，如果是真机建议将这个键名换成udid
            'appPackage':'com.mobivans.onestrokecharge',
            'appActivity':'com.stub.stub01.Stub01',
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
            driver.find_element_by_android_uiautomator('text("记一笔")').click()
            # driver.scroll(driver.find_element_by_android_uiautomator('text("医疗")'),
            #               driver.find_element_by_android_uiautomator('text("餐饮")'),1000)
            driver.find_element_by_android_uiautomator('text("旅行")').click()
            edit = driver.find_element_by_id('add_et_remark')
            edit.clear()
            edit.send_keys('出去玩')
            driver.find_element_by_id('keyb_btn_2').click()
            driver.find_element_by_id('keyb_btn_3').click()
            driver.find_element_by_id('keyb_btn_6').click()
            driver.find_element_by_id('keyb_btn_finish').click()
            driver.find_element_by_android_uiautomator('text("长按记录可删除")').click()
            remarks = driver.find_elements_by_id('account_item_txt_remark')
            money = driver.find_elements_by_id('account_item_txt_money')
            if remarks[0].text == '出去玩' and money[0].text == '-236':
                print('测试成功')
            else:
                print('测试失败')
        except Exception as e:
            with open(os.path.join(os.getcwd(),'report/%s.log' % self.device_name),'w') as f:
                f.write(str(e) + '\n')

            now = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            driver.get_screenshot_as_file(os.path.join(os.getcwd(),f'report/{self.device_name}_{now}.png'))
        finally:
            driver.quit()
#
if __name__ == '__main__':
    OnestrokeTest('127.0.0.1:21503','5.1.1',4723).start_test()
