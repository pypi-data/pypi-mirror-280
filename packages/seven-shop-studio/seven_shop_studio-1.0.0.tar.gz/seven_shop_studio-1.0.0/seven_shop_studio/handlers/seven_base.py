# -*- coding: utf-8 -*-
"""
:Author: KangWenBin
:Date: 2023-06-06 15:54:30
:LastEditTime: 2024-05-24 17:08:04
:LastEditors: KangWenBin
:Description: 
"""

# -*- coding: utf-8 -*-

from seven_studio.handlers.studio_base import *


class SevenBaseHandler(StudioBaseHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def write_error(self, status_code, **kwargs):
        """
        @description: 重写全局异常事件捕捉
        @last_editors: Kangwenbin
        """
        self.logger_error.error(traceback.format_exc())
        return self.reponse_json_error("server error")
    
    def load_json_or_empty(self,data):
        try:
            return json.loads(data)
        except:
            return []
    
    def param_check(self,param,check_list):
        """
        :description: 检查参数完整
        :last_editors: KangWenBin
        """       
        result = True
        for item in check_list:
            if not param.get(item,None):
                if param.get(item,None) == 0:
                    continue
                return False
        return result
    
    def dict_to_entity(self,entity,dict_info):
        """
        :description: 字段转化实体
        :last_editors: KangWenBin
        """        
        field_list = entity.get_field_list()
        for item in field_list:
            if item in dict_info:
                setattr(entity,item,dict_info[item])
        return entity
    
