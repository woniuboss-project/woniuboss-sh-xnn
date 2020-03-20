import random,xlrd



class Util:

    #新增培训资源中所需要输入的信息
    @classmethod
    def random_info(cls,pre):
        if pre == "tel":  #电话
            result = random.randint(13000000000,18999999999)
        elif pre == "school": #毕业学校
            li = ['上海大学财经大学', '上海同济大学', '上海交通大学', '上海复旦大学', '上海大学', '上海师范大学','四川农业大学']
            result = random.choice(li)
        elif pre == "major":  #专业
            li = ['计算机专业','金融专业','市场营销','工商管理','人力资源管理','信息管理与信息系统']
            result = random.choice(li)
        elif pre == "intent":  #求职意向
            li = ['java开发',"自动化测试",'测式开发',"Python全栈开发","java高架构师","通信工程师","初级会计","大数据开发工程师/程序员","室内设计师-设计师助理"]
            result = random.choice(li)
        elif pre == "applposition": #应聘岗位
            li = ['java开发', "自动化测试", '测式开发', "Python全栈开发", "java高架构师"]
            result = random.choice(li)
        elif pre == "salary":  #薪资要求
            result = random.randint(10000,20000)
        elif pre == "age":     #年龄
            result = random.randint(18,35)
        elif pre == "eduexp":   #教育经历
            li = ["无", ""]
            result = random.choice(li)
        elif pre =="experience": #工作经历
            li = ['保险公司销售员', "贷款电销", '公司人事', "CAD画图", "招聘专员","app测试","html开发","房地产销售员","物业文员","超市销售","工厂流水线工人","公务员","银行柜面员"]
            result = random.choice(li)
        elif pre =="last_tracking_remark": #最后跟踪
            result = ""
        else:
            result = "参数不对"
        return result

    #随机姓名
    @classmethod
    def random_name(cls):
        str = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方知耀达建功彰聪志立睿荣勋卓友增善进以纲毅澔意铖迅章敬朕锦舱达璟俯瑞冠容固承儒彤佚翰立俊豪瀚融哲候真超晋浦来合利智"'
        li = "知耀达建功彰聪志立睿荣勋卓友增善进以纲毅澔意铖迅章敬朕锦舱达璟俯瑞冠容固承儒彤佚翰立俊豪瀚融哲候真超晋浦来合利智"
        start = random.choice(str)
        end = ''.join(random.sample(li, 2))
        random_name = ''.join(start + end)
        return random_name

    #随机邮箱
    @classmethod
    def random_email(cls):
        cls.num = random.randint(100000,999999)
        li = ['qq.com','126.com',"163.com"]
        email = random.choice(li)
        result = ("%d" + "@" + email) % cls.num
        return result

    #随机的qq
    @classmethod
    def random_qq(cls):
        qq = random.randint(1111111,99999999)
        return qq

    #excel数据处理--列表+字典的格式[{},{},{}]
    @classmethod
    def excel_dict(cls,cont):
        file = xlrd.open_workbook("demo.xlsx")               #读取指定文件
        content = file.sheet_by_name("resources")            #打开指定的sheet页
        rows = content.nrows                                 #获取总行数
        cols = content.ncols                                 #藜取总列数
        li = []
        if rows != 0:                                            #如果sheet页的内容不为空
            for i in range(1,rows):                              #遍历每一行， 第0行是表头
                if cont in content.cell_value(i,1):              #如果传入的参数名在第1列中(第0列是模块名,第一列是测试编号）
                    rsult = content.cell_value(i,cols-2)         #取到包含参数名的每一行的测试数据
                    temp = rsult.strip().split("\n")             #去掉首尾空格，以\n分割
                    expect = content.cell_value(i,cols-1)        #预期结果在总列数一1的那一列
                    di = {}
                    for item in temp:                            #遍历所有的测试数据
                        tup = item.split("=")                    #每行测试数据单元格中的每一行的内容以=号分割
                        di[tup[0]]=tup[1]                        #将每一行等号左边内容为键，等号右边内容为值
                    di['expect'] = expect                        #在每一行遍历结束后，预期结果的内容
                    li.append(di)                                #在每一行结束时，把字典添加到列表中
        return li

    #excel数据处理--列表+元组的格式[(),(),()]
    @classmethod
    def excel_tup(cls,path,sheetname,cont):
        file = xlrd.open_workbook(path)                     # 读取指定文件
        content = file.sheet_by_name(sheetname)                  # 打开指定的sheet页
        rows = content.nrows                                       # 获取总行数
        cols = content.ncols                                       # 藜取总列数
        li = []
        if rows != None:                                           #如果sheet页的内容不为空
            for i in range(1, rows):                                   # 遍历每一行， 第0行是表头
                if cont in content.cell_value(i, 1):                   # 如果传入的参数名在第1列中(第0列是模块名,第一列是测试编号）
                    rsult = content.cell_value(i, cols-2)              # 取到包含参数名的每一行的测试数据
                    temp = rsult.strip().split("\n")                   # 去掉首尾空格，以\n分割
                    expect = content.cell_value(i, cols-1)            # 预期结果在总列数一1的那一列
                    li2 = []                                          # 用于周转
                    li2.append(expect)                                 # 将内容入到列表li2中
                    number = len(temp)                                 # 获取每行测试数据里的参数有多少行
                    fileds = [temp[i].split("=")[1] for i in range(number)] # 利用列表生成式，获取测试数据有几行就可以生成几行参数
                    tup = tuple(fileds + li2)                          # 将测试数据的参数和预期结果拼接到一个列表中，并转为元组格式
                    li.append(tup)                                     # 添加到列表中，形成列表+元组的格式
        return li
























# if __name__ == '__main__':
#     data = Util.excel_tup("..\\data\\demo.xlsx","resources",cont="add")
#     print(data)
#     from woniuboss.lib.resources_add import Resources_Add
#     from woniuboss.tools.server import Server
#     from selenium import webdriver
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     driver.get("http://192.168.1.8:8080/WoniuBoss2.5/")
#     Server.login(driver)
#     add = Resources_Add(driver)
#     add.add_source(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6],data[0][7],data[0][8],data[0][9],data[0][10],data[0][11],data[0][12],data[0][13])
