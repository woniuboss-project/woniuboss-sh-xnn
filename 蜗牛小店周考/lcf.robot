*** Settings ***
Library           Selenium2Library

*** Test Cases ***
login
    Open Browser    https://snailpet.com/index
    Sleep    2
    Input Text Into Alert    accept
    Sleep    2
    Click Button    xpath=/html/body/div[3]/div/div/div[3]/div[2]
    Sleep    2
    Input Text    css=input.cla-tex:nth-child(1)    16621322412
    Input Password    css=input.cla-tex:nth-child(2)    lcf123
    Click Button    css=.ori-btn
    Wait Until Element Is Visible    link=安全退出
    Element Should Contain    id=user_name    店长
    Close Browser
