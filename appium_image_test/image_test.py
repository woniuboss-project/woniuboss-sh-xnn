from appium import webdriver
import os,time,cv2


class OneStrokeImage:
    def __init__(self):
        desired_caps = {
            'platformName':'Android',
            'platformVersion':'5.1.1',
            'deviceName':'Appium',
            'appPackage':'com.mobivans.onestrokecharge',
            'appActivity':'com.stub.stub01.Stub01',
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        time.sleep(10)

    def find_image(self,target):
        image_path = os.path.join(os.getcwd(),'source')
        #利用appium的方法截取当前屏幕大图
        screen_path = os.path.join(image_path,'one_stroke.png')
        self.driver.get_screenshot_as_file(screen_path)
        screen = cv2.imread(screen_path)
        template = cv2.imread(os.path.join(image_path,target))
        result = cv2.matchTemplate(screen,template,cv2.TM_CCOEFF_NORMED)
        min,similarity,min_loc,max_loc = cv2.minMaxLoc(result)
        if similarity < 0.95:
            return -1,   -1
        x = max_loc[0] + int(template.shape[1] / 2)
        y = max_loc[1] + int(template.shape[0] / 2)
        return x,y

    def check_exists(self,target):
        x,y = self.find_image(target)
        return x != -1 and y != -1
    #定义一个针对指定模板进行单击操作的方法
    def do_click(self,target):
        x,y = self.find_image(target)
        if x == -1 and y == -1:
            print('没有找到目标%s.'% target)
            return
        #要注意tap方法的第-一个参数是-一个位置列表，因为它支持多指触摸的行为。
        self.driver.tap([(x,y)],10)
        print('在[%d,%d]位置单击%s'% (x,y,target))
        time.sleep(3)

    def start_test(self):
        self.do_click('./stroke.png')
        self.do_click('./type.png')
        self.do_click('./2.png')
        self.do_click('./4.png')
        self.do_click('./5.png')
        self.do_click('./affirm.png')
        time.sleep(3)
        self.do_click('./cancel.png')
        if self.check_exists('./list.png'):
            print('测试成功')
        else:
            print('测试失败')

        # self.driver.quit()
if __name__ == '__main__':
    one = OneStrokeImage()
    one.start_test()