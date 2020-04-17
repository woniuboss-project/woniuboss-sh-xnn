*** Settings ***
Library           Selenium2Library

*** Test Cases ***
login
    Open Browser    https://snailpet.com/index
    sleep    3
    Click Link    确定
    Click Element    css=.red_btn
    Input Text    xpath=/html/body/app-root/div/snail-index/div/div/div/div[3]/div/div[1]/input[1]    15617980785
    Input Password    xpath=/html/body/app-root/div/snail-index/div/div/div/div[3]/div/div[1]/input[2]    admin123
    Click Link    xpath=/html/body/app-root/div/snail-index/div/div/div/div[3]/div/div[1]/a
    Page Should Contain Link    安全退出
    ${m}    Get Cookies
    Log    ${m}

save_spend
    Open Browser    https://snailpet.com/index
    Add Cookie    phone    15617980785
    Add Cookie    password    admin123
    Sleep    3
    Click Element    css=a.menu_item:nth-child(7) > div:nth-child(3)
    Click Link    xpath=/html/body/app-root/div/snail-else-main/snail-expend/div[1]/div[2]/div/a
    Click Element    css=li.active
    Input Text    xpath=/html/body/app-root/div/snail-else-main/snail-expend/div[2]/div/div/div[2]/div/div[3]/div[1]/div/div/input    32252
    Input Text    id=id-exp-date    1585238400
    Click Element    xpath=/html/body/app-root/div/snail-else-main/snail-expend/div[2]/div/div/div[3]/div[2]
