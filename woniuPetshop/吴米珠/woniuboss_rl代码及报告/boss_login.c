boss_login()
{

	/*ע:������login��������Ҫע�����¼���:
	1,����ֻ�ܷ��������ǰ��,�����ɹ���ԭ����������
	2,����ʼ�ĵط�ֻ���ڷ��������ǰ��
	3,��������ʱҪ��������������������������������ͬ
	4,��������Ŀ�ʼ�����������Ҫһ��,�������״̬��Ҫ�ֶ�����ΪPASS��FAIL
	5,����������ܹ�����������ӵ�,ֻ��Ҫ��{}����,���ü�$����
	*/
	
	//��¼����--������web_reg_find
	web_reg_find("SaveCount=login_resp",
		"Text/BIN={expect}",
		LAST);

	//����һ��login����ʼ�ĵط�
	lr_start_transaction("login");
	
	//��¼����--����:web_submit_data
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

	//����,�������Ӧ������ҵ�Ԥ�ڽ���е��ı�����,����ɹ�,��������ʧ��
	if (atoi(lr_eval_string("{login_resp}")) == 1){
		lr_output_message("��¼�ɹ�");
		lr_end_transaction("login", LR_PASS);

	}else{
		lr_output_message("��¼ʧ��");
		lr_end_transaction("login", LR_FAIL);
	}
	
	//˼��ʱ��
	lr_think_time(2);

	
	
	//���ܵļ���
	web_reg_find("SaveCount=code_resp",
		"Text={cexpect}",
		LAST);

	
	lr_start_transaction("decode");
	
	//���ܵ�����
	web_submit_data("code_post",
		"Action={curl}",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=vp", "Value={cpassword}", ENDITEM,
		LAST);

	if (atoi(lr_eval_string("{code_resp}"))==1){
	    	lr_output_message("���ܳɹ�");
	    	lr_end_transaction("decode", LR_PASS);

	    }else{
	    	lr_output_message("����ʧ��");
	    	lr_end_transaction("decode", LR_FAIL);
	    }
	
	
	lr_think_time(2);
	
	
	//��ѯ��ѵ��Դ����
	web_reg_save_param_json(
		"ParamName=query_resp",
		"QueryString=$..totalRow",
		"SelectAll=No",
		SEARCH_FILTERS,
		LAST);
	lr_start_transaction("query");	
	//��ѯ��ѵ��Դ����
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
	//��ѯ��ѵ��Դ����
	if (atoi(lr_eval_string("{query_resp}")) != 0){
		lr_output_message("��ѯ�ɹ�");
		lr_end_transaction("query", LR_PASS);
	}else{
		lr_output_message("��ѯʧ��");
		lr_end_transaction("query", LR_FAIL);

	}
	
	
	return 0;
}
