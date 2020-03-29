boss_login()
{

	/*注:在以下login事务中需要注意以下几点:
	1,检查点只能放在请求的前面,这是由工作原理来决定的
	2,事务开始的地方只能在发送请求的前面
	3,定义事务时要避免事务的命名不可以与请求的命名相同
	4,定义事务的开始与结束的命名要一致,且事务的状态需要手动更改为PASS或FAIL
	5,如果参数是能过参数列中添加的,只需要加{}就行,不用加$符号
	*/
	
	//登录检查点--方法：web_reg_find
	web_reg_find("SaveCount=login_resp",
		"Text/BIN={expect}",
		LAST);

	//定义一个login事务开始的地方
	lr_start_transaction("login");
	
	//登录请求--方法:web_submit_data
	web_submit_data("login_post",
		"Action={url}",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=userName", "Value={username}", ENDITEM,
		"Name=userPass", "Value={userpass}", ENDITEM,
		"Name=checkcode", "Value={code}", ENDITEM,
		LAST);

	//断言,如果在响应结果中找到预期结果中的文本内容,事务成功,否则事务失败
	if (atoi(lr_eval_string("{login_resp}")) == 1){
		lr_output_message("登录成功");
		lr_end_transaction("login", LR_PASS);

	}else{
		lr_output_message("登录失败");
		lr_end_transaction("login", LR_FAIL);
	}
	
	//思考时间
	lr_think_time(2);

	
	
	//解密的检查点
	web_reg_find("SaveCount=code_resp",
		"Text={cexpect}",
		LAST);

	
	lr_start_transaction("decode");
	
	//解密的请求
	web_submit_data("code_post",
		"Action={curl}",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=vp", "Value={cpassword}", ENDITEM,
		LAST);

	if (atoi(lr_eval_string("{code_resp}"))==1){
	    	lr_output_message("解密成功");
	    	lr_end_transaction("decode", LR_PASS);

	    }else{
	    	lr_output_message("解密失败");
	    	lr_end_transaction("decode", LR_FAIL);
	    }
	
	
	lr_think_time(2);
	
	
	//查询培训资源检查点
	web_reg_save_param_json(
		"ParamName=query_resp",
		"QueryString=$..totalRow",
		"SelectAll=No",
		SEARCH_FILTERS,
		LAST);
	lr_start_transaction("query");	
	//查询培训资源请求
	web_submit_data("query_post",
		"Action={query_url}",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=pageSize", "Value=10", ENDITEM,
		"Name=pageIndex", "Value=1", ENDITEM,
		"Name=status", "Value=", ENDITEM,
		"Name=cusInfo", "Value=", ENDITEM,
		"Name=lastStatus", "Value=", ENDITEM,
		"Name=empName", "Value=", ENDITEM,
		"Name=source", "Value=", ENDITEM,
		"Name=s_time", "Value=", ENDITEM,
		"Name=e_time", "Value=", ENDITEM,
		"Name=poolType", "Value=", ENDITEM,
		LAST);	
	//查询培训资源断言
	if (atoi(lr_eval_string("{query_resp}")) != 0){
		lr_output_message("查询成功");
		lr_end_transaction("query", LR_PASS);
	}else{
		lr_output_message("查询失败");
		lr_end_transaction("query", LR_FAIL);

	}
	
	
	return 0;
}
