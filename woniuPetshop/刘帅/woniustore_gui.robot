*** Settings ***
Library           SeleniumLibrary

*** Test Cases ***
login
    Open Browser    https://snailpet.com/index
    Sleep    6
    Click Element    css=.red_btn
    Input Text    name=phone    15238899225
    Input Password    name=password    a805791737
    Click Element    css=.ori-btn
    Sleep    3
    Page Should Contain Link    安全退出
    Close Browser

cash
    Open Browser    https://snailpet.com/index
    Sleep    6
    Click Element    css=.red_btn
    Sleep    3
    Input Text    name=phone    15238899225
    Input Password    name=password    a805791737
    Click Element    css=.ori-btn
    Sleep    3
    Click Element    css=a.menu_item:nth-child(2) > div:nth-child(3)
    Sleep    5
    Page Should Contain Link    挂单列表
    Close Browser

vip
    Open Browser    https://snailpet.com/index
    Sleep    6
    Click Element    css=.red_btn
    Sleep    3
    Input Text    name=phone    15238899225
    Input Password    name=password    a805791737
    Click Element    css=.ori-btn
    Sleep    3
    Click Element    css=a.menu_item:nth-child(3) > div:nth-child(3)
    Sleep    3
    Page Should Contain Link    新增会员
    Close Browser

goods
    Open Browser    https://snailpet.com/index
    Sleep    6
    Click Element    css=.red_btn
    Sleep    3
    Input Text    name=phone    15238899225
    Input Password    name=password    a805791737
    Click Element    css=.ori-btn
    Sleep    3
    Click Element    css=a.menu_item:nth-child(4) > div:nth-child(3)
    Sleep    3
    Page Should Contain Link    新增商品
    Close Browser

sale
    Open Browser    https://snailpet.com/index
    Sleep    6
    Click Element    css=.red_btn
    Sleep    3
    Input Text    name=phone    15238899225
    Input Password    name=password    a805791737
    Click Element    css=.ori-btn
    Sleep    3
    Click Element    css=a.menu_item:nth-child(6) > div:nth-child(3)
    Sleep    3
    Close Browser

statement
    Open Browser    https://snailpet.com/index
    Sleep    6
    Click Element    css=.red_btn
    Sleep    3
    Input Text    name=phone    15238899225
    Input Password    name=password    a805791737
    Click Element    css=.ori-btn
    Sleep    3
    Click Element    css=a.menu_item:nth-child(8) > div:nth-child(3)
    Sleep    3
    Page Should Contain Link    工资
    Close Browser

tools
    Open Browser    https://snailpet.com/index
    Sleep    6
    Click Element    css=.red_btn
    Sleep    3
    Input Text    name=phone    15238899225
    Input Password    name=password    a805791737
    Click Element    css=.ori-btn
    Sleep    3
    Click Element    xpath=/html/body/app-root/div/snail-menu-nav/div/a[8]/div
    Sleep    3
    Page Should Contain Link    下载APP
    Close Browser

settings
    Open Browser    https://snailpet.com/index
    Sleep    6
    Click Element    css=.red_btn
    Sleep    3
    Input Text    name=phone    15238899225
    Input Password    name=password    a805791737
    Click Element    css=.ori-btn
    Sleep    3
    Click Element    css=a.menu_item:nth-child(18) > div:nth-child(3)
    Sleep    3
    Page Should Contain Link    店员设置
    Close Browser

message
    Open Browser    https://snailpet.com/index
    Sleep    6
    Click Element    css=.red_btn
    Sleep    3
    Input Text    name=phone    15238899225
    Input Password    name=password    a805791737
    Click Element    css=.ori-btn
    Sleep    3
    Click Element    css=a.menu_item:nth-child(12) > div:nth-child(2)
    Sleep    3
    Page Should Contain Link    综合
    Close Browser
