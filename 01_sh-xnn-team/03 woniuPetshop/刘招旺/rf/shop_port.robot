*** Settings ***
Library           RequestsLibrary

*** Variables ***
${headers}        Content-Type=application/json; charset=utf-8

*** Test Cases ***
login
    ${data}    Create Dictionary    phone=15617980785    password=admin123    shop_id=null
    Create Session    session    https://
    ${resp}    Post Request    session    snailpet.com/v2/Passport/login    ${data}    headers=${headers}
    Log    ${resp.text}
