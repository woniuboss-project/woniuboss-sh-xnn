*** Settings ***
Resource          Login.txt
Resource          customer.txt
Library           ../../../../Lib/site-packages/NewLibrary/DataJsonLibrary.py
Resource          Cards.txt
Resource          Spending.txt
Resource          Goods.txt
Resource          Assert.txt

*** Test Cases ***
do_login
    @{li}    DataJsonLibrary.Excel Dict    D:\\woniuxiaodian.xlsx    接口测试    登录
    FOR    ${i}    IN    @{li}
        ${resp}    login    ${i["url"]}    ${i["password"]}    ${i["phone"]}    ${i["shop_id"]}
        assert    ${i["expect"]}     ${resp.status_code }    ${i["number"]}
    END

do_add_customer
    @{li}    DataJsonLibrary.Excel Dict    D:\\woniuxiaodian.xlsx    接口测试    会员卡
    FOR    ${i}    IN    @{li}
        ${resp}    add_customer    url=${i["url"]}    addr=${i["addr"]}    cardNumber=${i["cardNumber"]}    is_open_upgrade=${i["is_open_upgrade"]}    is_spending_msg=${i["is_spending_msg"]}    mark=${i["mark"]}    member_tags=${i["member_tags"]}    name=${i["name"]}    pets=${i["pets"]}    phone=${i["phone"]}    sex=${i["sex"]}    shop_id=${i["shop_id"]}    shopId=${i["shopId"]}    spare_phone=${i["spare_phone"]}
        assert    ${i["expect"]}    ${resp.status_code}    ${i["number"]}
    END

do_cards
    @{li}    DataJsonLibrary.Excel Dict    D:\\woniuxiaodian.xlsx    接口测试    购物卡
    FOR    ${i}    IN    @{li}
        ${resp}    cards    ${i["url"]}    ${i["exp_time_type"]}    ${i["integral_percentage"]}    ${i["name"]}    ${i["shop_id"]}    ${i["shopId"]}
        assert    ${i["expect"]}    ${resp.status_code}    ${i["number"]}
    END

do_spending
    @{li}    DataJsonLibrary.Excel Dict    D:\\woniuxiaodian.xlsx    接口测试    支出
    FOR    ${i}    IN    @{li}
        ${resp}    spending    ${i["url"]}    ${i["actionTime"]}    ${i["type"]}    ${i["mark"]}    ${i["amount"]}    ${i["shopId"]}    ${i["shop_id"]}
        assert    ${i["expect"]}    ${resp.status_code}    ${i["number"]}
    END

do_goods
    @{li}    DataJsonLibrary.Excel Dict    D:\\woniuxiaodian.xlsx    接口测试    新增商品
    FOR    ${i}    IN    @{li}
        ${resp}    goods    ${i["url"]}    ${i["shopId"]}    ${i["productId"]}    ${i["barCode"]}     ${i["isServer"]}    ${i["name"]}    ${i["categoryId"]}    ${i["inPrice"]}    ${i["outPrice"]}    ${i["percentage"]}    ${i["notice_stocks"]}    ${i["weight"]}    ${i["logo_images"]}    ${i["detail_images"]}
        ...    ${i["production_time"]}    ${i["brand_name"]}    ${i["add_brand_category_id"]}    ${i["version"]}    ${i["shop_id"]}
        assert    ${i["expect"]}    ${resp.status_code}    ${i["number"]}
    END
