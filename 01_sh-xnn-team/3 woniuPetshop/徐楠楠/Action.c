Action()
{
	//���
	web_reg_save_param_json(
	"ParamName=queryLoginByJson",
	"QueryString=$.error",
	"NotFound=warning",
	"SelectAll=No",
	SEARCH_FILTERS,
	"Scope=BODY",
	LAST);
	//��¼
	web_submit_data("web_login_data",
		"Action=https://snailpet.com/v2/Passport/login",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=phone", "Value=18018661946", ENDITEM,
		"Name=password", "Value=18018661946x", ENDITEM,
		"Name=shop_id", "Value=null", ENDITEM,
		LAST);
	//����
	if (atoi(lr_eval_string("queryLoginByJson")) == 0){
		lr_output_message("release login success");
	} else{
		lr_output_message("release login fail");
	}
	
	//���
	web_reg_save_param_json(
	"ParamName=queryCountByJson",
	"QueryString=$.error",
	"NotFound=warning",
	"SelectAll=No",
	SEARCH_FILTERS,
	"Scope=BODY",
	LAST);
	
	//����

	web_submit_data("web_Count_data",
		"Action=https://snailpet.com/v2/cats/change_member",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=cart_type", "Value=0", ENDITEM,
		"Name=member_id", "Value=586076", ENDITEM,
		"Name=out_id", "Value=0", ENDITEM,
		"Name=shop_id", "Value=17557", ENDITEM,
		LAST);
	
	//����
	if (atoi(lr_eval_string("queryCountByJson")) == 0){
		lr_output_message("release count success");
	} else{
		lr_output_message("release count fail");
	}
	
	//��Ա���
	web_reg_save_param_json(
	"ParamName=queryAnalysisByJson",
	"QueryString=$.error",
	"NotFound=warning",
	"SelectAll=No",
	SEARCH_FILTERS,
	"Scope=BODY",
	LAST);
	//��Ա
	web_submit_data("web_Analysisdata",
		"Action=https://snailpet.com/v2/analysis_es/action",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=ex_current_pages", "Value=��ҳ", ENDITEM,
		"Name=ex_kind", "Value=���", ENDITEM,
		"Name=ex_next_page", "Value=��Ա", ENDITEM,
		"Name=ex_title", "Value=��Ա", ENDITEM,
		"Name=shop_id", "Value=17557", ENDITEM,
		LAST);
	//��Ա����
	if (atoi(lr_eval_string("queryAnalysisByJson")) == 0){
		lr_output_message("release count success");
	} else{
		lr_output_message("release count fail");
	}
	
	//��Ʒ������
	web_reg_save_param_json(
	"ParamName=queryAnalysisByJson",
	"QueryString=$.error",
	"NotFound=warning",
	"SelectAll=No",
	SEARCH_FILTERS,
	"Scope=BODY",
	LAST);
	//��Ʒ����
	web_submit_data("web_Analysisdata",
		"Action=https://snailpet.com/v2/analysis_es/action",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=ex_current_pages", "Value=��ҳ", ENDITEM,
		"Name=ex_kind", "Value=���", ENDITEM,
		"Name=ex_next_page", "Value=��Ʒ����", ENDITEM,
		"Name=ex_title", "Value=��Ʒ����", ENDITEM,
		"Name=shop_id", "Value=17557", ENDITEM,
		LAST);
	//��Ʒ�������
	if (atoi(lr_eval_string("queryAnalysisByJson")) == 0){
		lr_output_message("release count success");
	} else{
		lr_output_message("release count fail");
	}
	
	
	//֧�����
	web_reg_save_param_json(
	"ParamName=queryAnalysisByJson",
	"QueryString=$.error",
	"NotFound=warning",
	"SelectAll=No",
	SEARCH_FILTERS,
	"Scope=BODY",
	LAST);
	//֧��
	web_submit_data("web_Analysisdata",
		"Action=https://snailpet.com/v2/analysis_es/action",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=ex_current_pages", "Value=��ҳ", ENDITEM,
		"Name=ex_kind", "Value=���", ENDITEM,
		"Name=ex_next_page", "Value=֧��", ENDITEM,
		"Name=ex_title", "Value=֧��", ENDITEM,
		"Name=shop_id", "Value=17557", ENDITEM,
		LAST);
	//����
	if (atoi(lr_eval_string("queryAnalysisByJson")) == 0){
		lr_output_message("release count success");
	} else{
		lr_output_message("release count fail");
	}
	
	
	return 0;
}
