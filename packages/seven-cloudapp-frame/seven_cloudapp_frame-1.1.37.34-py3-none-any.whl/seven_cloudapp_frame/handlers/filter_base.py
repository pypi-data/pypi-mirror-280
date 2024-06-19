# -*- coding: utf-8 -*-
"""
@Author: HuangJianYi
@Date: 2022-04-24 15:15:19
@LastEditTime: 2024-03-25 17:15:31
@LastEditors: HuangJianYi
@Description: 
"""

from seven_framework.web_tornado.base_handler.base_api_handler import *
from seven_cloudapp_frame.libs.customize.seven_helper import *
from seven_cloudapp_frame.libs.customize.cryptography_helper import *
from seven_cloudapp_frame.libs.customize.safe_helper import *
from seven_cloudapp_frame.models.app_base_model import *
from urllib.parse import parse_qs


def filter_check_params(must_params=None, check_user_code=False):
    """
    :description: 参数过滤装饰器 仅限handler使用,
                  提供参数的检查及获取参数功能
                  装饰器使用方法:
                  @client_filter_check_params("param_a,param_b,param_c")  或
                  @client_filter_check_params(["param_a","param_b,param_c"])
                  参数获取方法:
                  self.request_params[param_key]
    :param must_params: 必须传递的参数集合
    :param check_user_code: 是否校验用户标识必传
    :last_editors: HuangJianYi
    """
    def check_params(handler):
        def wrapper(self, **args):
            finally_must_params = must_params
            if hasattr(self, "must_params"):
                finally_must_params = self.must_params
            if type(finally_must_params) == str:
                must_array = finally_must_params.split(",")
            if type(finally_must_params) == list:
                must_array = finally_must_params

            if finally_must_params:
                for must_param in must_array:
                    if not must_param in self.request_params or self.request_params[must_param] == "":
                        self.response_json_error("param_error", f"参数错误,缺少必传参数{must_param}")
                        return
            if check_user_code == True and not self.get_user_id():
                self.response_json_error("param_error", f"参数错误,缺少必传参数user_code")
                return

            return handler(self, **args)

        return wrapper

    return check_params


def filter_check_current_limit(handler_name=None, current_limit_count=0):
    """
    :description: 流量限制过滤装饰器 仅限handler使用
    :param handler_name: handler名字
    :param current_limit_count: 流量限制数量
    :last_editors: HuangJianYi
    """
    def check_current(handler):
        def wrapper(self, **args):
            # 是否流量控制
            safe_config = share_config.get_value("safe_config", {})
            if safe_config.get("traffic_control_ways", 0) == 2: # 流量控制方式 0-关闭 1-全局控制 2-指定handler控制
                app_base_model = AppBaseModel(context=self)
                app_id = self.get_app_id()
                open_id = self.get_open_id()
                limit_count = current_limit_count
                if limit_count == 0:
                    app_info_dict = app_base_model.get_app_info_dict(app_id,True,"current_limit_count")
                    limit_count = app_info_dict["current_limit_count"] if app_info_dict else 0
                if SafeHelper.check_current_limit(app_id, limit_count, handler_name) == True:
                    self.response_json_error("current_limit", "当前人数过多,请稍后再试")
                    return
                if handler_name:
                    SafeHelper.add_current_limit_count(app_id, open_id, handler_name)

            return handler(self, **args)

        return wrapper

    return check_current


