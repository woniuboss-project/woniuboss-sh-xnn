Action()
{
	
	//登录检查点
	
	web_reg_find("Search=Body",
		"SaveCount=login_resp",
		"Text={expect}",
		LAST);

	
	lr_think_time(3);
	
	lr_start_transaction("login");
	//发送登录请求
	web_submit_data("login",
		"Action=http://192.168.1.8:8080/WoniuBoss2.5/log/userLogin",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=userName", "Value={username}", ENDITEM,
		"Name=userPass", "Value={password}", ENDITEM,
		"Name=checkcode", "Value={verifycode}", ENDITEM,
		LAST);
	
	
	if(atoi(lr_eval_string("{login_resp}"))==1){
		lr_output_message("登录成功");
		lr_end_transaction("login", LR_PASS);

	}else{
		lr_output_message("登录失败");
		lr_end_transaction("login", LR_FAIL);

	}
	
	
	
	
	web_reg_find("SaveCount=edcode",
		"Text=yes",
		LAST);
	
	
	lr_start_transaction("code");

	//新增查询事务
	web_submit_data("verifycode",
		"Action=http://192.168.1.8:8080/WoniuBoss2.5/second?vp=woniu123",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=vp", "Value=woniu123 ", ENDITEM,
		LAST);
	if (atoi(lr_eval_string("{edcode}"))==1){
	    	lr_output_message("解密成功");
	    	lr_end_transaction("code", LR_PASS);
	    }else{lr_output_message("解密失败");
	    lr_end_transaction("code", LR_FAIL);
	    }
	    	

	

	
	
	
	return 0;
}
