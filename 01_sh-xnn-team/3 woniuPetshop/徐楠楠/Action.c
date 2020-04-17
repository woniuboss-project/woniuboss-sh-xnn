Action()
{
	//检查
	web_reg_save_param_json(
	"ParamName=queryLoginByJson",
	"QueryString=$.error",
	"NotFound=warning",
	"SelectAll=No",
	SEARCH_FILTERS,
	"Scope=BODY",
	LAST);
	//登录
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
	//断言
	if (atoi(lr_eval_string("queryLoginByJson")) == 0){
		lr_output_message("release login success");
	} else{
		lr_output_message("release login fail");
	}
	
	//检查
	web_reg_save_param_json(
	"ParamName=queryCountByJson",
	"QueryString=$.error",
	"NotFound=warning",
	"SelectAll=No",
	SEARCH_FILTERS,
	"Scope=BODY",
	LAST);
	
	//收银

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
	
	//断言
	if (atoi(lr_eval_string("queryCountByJson")) == 0){
		lr_output_message("release count success");
	} else{
		lr_output_message("release count fail");
	}
	
	//会员检查
	web_reg_save_param_json(
	"ParamName=queryAnalysisByJson",
	"QueryString=$.error",
	"NotFound=warning",
	"SelectAll=No",
	SEARCH_FILTERS,
	"Scope=BODY",
	LAST);
	//会员
	web_submit_data("web_Analysisdata",
		"Action=https://snailpet.com/v2/analysis_es/action",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=ex_current_pages", "Value=首页", ENDITEM,
		"Name=ex_kind", "Value=点击", ENDITEM,
		"Name=ex_next_page", "Value=会员", ENDITEM,
		"Name=ex_title", "Value=会员", ENDITEM,
		"Name=shop_id", "Value=17557", ENDITEM,
		LAST);
	//会员断言
	if (atoi(lr_eval_string("queryAnalysisByJson")) == 0){
		lr_output_message("release count success");
	} else{
		lr_output_message("release count fail");
	}
	
	//商品管理检查
	web_reg_save_param_json(
	"ParamName=queryAnalysisByJson",
	"QueryString=$.error",
	"NotFound=warning",
	"SelectAll=No",
	SEARCH_FILTERS,
	"Scope=BODY",
	LAST);
	//商品管理
	web_submit_data("web_Analysisdata",
		"Action=https://snailpet.com/v2/analysis_es/action",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=ex_current_pages", "Value=首页", ENDITEM,
		"Name=ex_kind", "Value=点击", ENDITEM,
		"Name=ex_next_page", "Value=商品管理", ENDITEM,
		"Name=ex_title", "Value=商品管理", ENDITEM,
		"Name=shop_id", "Value=17557", ENDITEM,
		LAST);
	//商品管理断言
	if (atoi(lr_eval_string("queryAnalysisByJson")) == 0){
		lr_output_message("release count success");
	} else{
		lr_output_message("release count fail");
	}
	
	
	//支出检查
	web_reg_save_param_json(
	"ParamName=queryAnalysisByJson",
	"QueryString=$.error",
	"NotFound=warning",
	"SelectAll=No",
	SEARCH_FILTERS,
	"Scope=BODY",
	LAST);
	//支出
	web_submit_data("web_Analysisdata",
		"Action=https://snailpet.com/v2/analysis_es/action",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=ex_current_pages", "Value=首页", ENDITEM,
		"Name=ex_kind", "Value=点击", ENDITEM,
		"Name=ex_next_page", "Value=支出", ENDITEM,
		"Name=ex_title", "Value=支出", ENDITEM,
		"Name=shop_id", "Value=17557", ENDITEM,
		LAST);
	//断言
	if (atoi(lr_eval_string("queryAnalysisByJson")) == 0){
		lr_output_message("release count success");
	} else{
		lr_output_message("release count fail");
	}
	
	
	return 0;
}
