# -*- coding: utf-8 -*-
"""
:Author: KangWenBin
:Date: 2024-06-04 10:16:19
:LastEditTime: 2024-06-19 14:46:39
:LastEditors: KangWenBin
:Description: 
"""
from seven_shop_studio.models.db_models.order.order_refund_model import *

class OrderRefundModelEx(OrderRefundModel):
    def __init__(self, db_connect_key='db_shopping_center', sub_table=None, db_transaction=None, context=None):
        super().__init__(db_connect_key, sub_table, db_transaction, context)
    
    def get_refund_order_page_list(self, page_index, page_size, where='', params=None):
        """
        :description: 退款订单列表
        :last_editors: KangWenBin
        """        
        limit = f"LIMIT {str(int(page_index) * int(page_size))},{str(page_size)}"

        condition = ""
        if where:
            condition += f" where {where}"


        sql = f"SELECT a.order_id,a.refund_order_id,a.add_time,IF(b.logistics_number = '',0,1) AS logistics_status,a.real_refund_price,a.refund_type,a.reason,a.status  FROM order_refund_tb a  JOIN order_tb b ON a.order_id = b.order_id JOIN order_refund_goods_tb c ON a.refund_order_id = c.refund_order_id {condition} GROUP BY a.refund_order_id ORDER BY a.add_time desc {limit}"

        ret_list = self.db.fetch_all_rows(sql,params)
        sql_count = f"SELECT COUNT(*) as order_count FROM (SELECT a.order_id FROM order_refund_tb a  JOIN order_tb b ON a.order_id = b.order_id JOIN order_refund_goods_tb c ON a.refund_order_id = c.refund_order_id {condition} GROUP BY a.refund_order_id) AS order_table "
        row = self.db.fetch_one_row(sql_count,params)
        
        return ret_list,row["order_count"]