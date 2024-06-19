from seven_shop_studio.models.db_models.order.order_model import *


class OrderModelEx(OrderModel):
    
    def __init__(self, db_connect_key='db_shopping_center', sub_table=None, db_transaction=None, context=None):
        super().__init__(db_connect_key, sub_table, db_transaction, context)

    def get_order_page_list(self, page_index, page_size, where='', params=None):
        """
        :description: 订单列表
        :last_editors: KangWenBin
        """        
        limit = f"LIMIT {str(int(page_index) * int(page_size))},{str(page_size)}"

        condition = ""
        if where:
            condition += f" where {where}"


        sql = f"SELECT a.order_id,a.add_time,a.real_pay_price,a.remark,a.shop_remark,a.status,a.province_name,a.city_name,a.district_name,a.consignee,a.phone,a.address_info,a.logistics_company,a.logistics_number FROM order_tb a left JOIN order_goods_tb b ON a.order_id = b.order_id {condition} group by a.order_id order by a.add_time desc {limit}"

        ret_list = self.db.fetch_all_rows(sql,params)
        sql_count = f"SELECT COUNT(*) as order_count FROM (SELECT a.order_id FROM order_tb a LEFT JOIN order_goods_tb b ON a.order_id = b.order_id {condition} GROUP BY a.order_id) AS order_table "
        row = self.db.fetch_one_row(sql_count,params)
        
        return ret_list,row["order_count"]