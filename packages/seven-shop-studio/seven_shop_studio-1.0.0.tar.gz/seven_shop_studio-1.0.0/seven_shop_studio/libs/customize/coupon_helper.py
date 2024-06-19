from seven_shop_studio.models.db_models.order.order_goods_model import *
from seven_shop_studio.models.db_models.order.order_refund_goods_model import *
from seven_shop_studio.models.db_models.coupon.coupon_record_model import *

class CouponHelper(object):
    @classmethod
    def refund_coupon_check(self, coupon_id, order_id):
        """
        :description: 检测优惠券是否可退
        :last_editors: KangWenBin
        """        
        if coupon_id > 0:
            order_goods_count = OrderGoodsModel().get_total(where="order_id = %s", params=[order_id])
            order_refund_goods_count = OrderRefundGoodsModel().get_total(where="order_id = %s", params=[order_id])
            if order_goods_count == order_refund_goods_count:
                # 退还优惠券
                CouponRecordModel().update_table("order_id = '',use_time = 0,status = 0","id = %s",coupon_id)
