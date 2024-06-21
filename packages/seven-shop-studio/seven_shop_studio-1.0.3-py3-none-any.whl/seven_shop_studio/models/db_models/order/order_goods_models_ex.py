# -*- coding: utf-8 -*-
"""
:Author: KangWenBin
:Date: 2024-05-22 16:19:34
:LastEditTime: 2024-06-19 11:32:08
:LastEditors: KangWenBin
:Description: 
"""
from seven_shop_studio.models.db_models.order.order_goods_model import *

class OrderGoodsModelEx(OrderGoodsModel):
    def __init__(self, db_connect_key='db_shopping_center', sub_table=None, db_transaction=None, context=None):
        super().__init__(db_connect_key, sub_table, db_transaction, context)


    def get_order_goods_list(self,order_id_list):
        """
        :description: 获取订单商品相关信息
        :last_editors: Kangwenbin
        """
        
        sql = "SELECT a.order_id,a.sku_name,a.goods_picture,a.goods_name,a.buy_count,a.price,a.real_pay_price,c.status as refund_status FROM order_goods_tb a LEFT JOIN order_refund_goods_tb b ON a.order_id = b.order_id AND a.goods_id = b.goods_id AND a.sku_id = b.sku_id LEFT JOIN order_refund_tb c ON b.refund_order_id = c.refund_order_id where a.order_id in %s"
        goods_list = self.db.fetch_all_rows(sql, (order_id_list,))
        return goods_list