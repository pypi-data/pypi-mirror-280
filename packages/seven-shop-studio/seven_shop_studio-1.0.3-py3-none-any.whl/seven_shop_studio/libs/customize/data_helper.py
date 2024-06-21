# -*- coding: utf-8 -*-
"""
:Author: KangWenBin
:Date: 2024-06-19 16:24:05
:LastEditTime: 2024-06-21 14:01:32
:LastEditors: KangWenBin
:Description: 
"""
from seven_shop_studio.models.db_models.order.order_model import *
from seven_shop_studio.models.db_models.cart.cart_model_ex import *
from seven_shop_studio.models.db_models.order.order_refund_model_ex import *

class DataHelper:
    @classmethod
    def get_shop_data(self,shop_id,begin_time,end_time):
        """
        :description: 支付数据提供
        :last_editors: KangWenBin
        """        
        ret_data = {
            "pay_price":0, # 支付金额
            "pay_user":0, # 支付人数
            "pay_count":0, # 支付订单数
            "pay_goods_count":0, # 支付商品件数
            "average_sale":0, # 客单价
            "cart_pay_rate":"0%",
            "cart_user":0, # 加购人数
            "cart_goods_count":0, # 加购商品件数
            "refund_price":0, # 成功退款金额
            "refund_user":0, # 成功退款人数
            "refund_count":0, # 成功退款次数
            "refund_rate":0, # 成功退款率
        }
        # 订单数据
        order_list = OrderModel().get_dict_list(field="real_pay_price,user_code,buy_count,channel_id", where="shop_id = %s and add_time >= %s and add_time < %s and pay_time > 0",params=[shop_id,begin_time,end_time])
        if order_list:
            ret_data["pay_price"] = sum([order["real_pay_price"] for order in order_list])
            ret_data["pay_user"] = len(set([order["user_code"] for order in order_list]))
            ret_data["pay_count"] = len(order_list)
            ret_data["pay_goods_count"] = sum([order["buy_count"] for order in order_list])
            ret_data["average_sale"] = round(ret_data["pay_price"]/ret_data["pay_user"],2)
            ret_data["cart_pay_rate"] = str(int(round(len([x for x in order_list if x["channel_id"] == 2])/ret_data["pay_count"],2)*100))+"%"

        # 购物车数据
        cart_list = CartModelEx().get_cart_list(shop_id,begin_time,end_time)
        if cart_list:
            ret_data["cart_goods_count"] = sum([cart["buy_count"] for cart in cart_list])
            ret_data["cart_user"] = len(set([cart["user_code"] for cart in cart_list]))
        
        # 退款数据
        refund_conn = OrderRefundModelEx()
        refund_list = refund_conn.get_dict_list(field="real_refund_price,user_code",where="shop_id = %s and add_time >= %s and add_time < %s and status = 5 and refund_status = 2",params=[shop_id,begin_time,end_time])
        if refund_list:
            ret_data["refund_price"] = sum([refund["real_refund_price"] for refund in refund_list])
            ret_data["refund_user"] = len(set([refund["user_code"] for refund in refund_list]))
            ret_data["refund_count"] = len(refund_list)
            refund_total = refund_conn.get_total(where="shop_id = %s and add_time >= %s and add_time < %s",params=[shop_id,begin_time,end_time])
            ret_data["refund_rate"] = str(int(round(ret_data["refund_count"]/refund_total,2)*100))+"%"

        return ret_data
       