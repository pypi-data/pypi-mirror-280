# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/8 21:26
@Auth ： yuslience
@File ：ResendOrderByRtnOrder.py
@IDE ：CLion
@Motto: Emmo......
"""
from loguru import logger


def resend_order_by_cancelled_order(tick: dict, order: dict, hft_context, order_convert):
    """
    价格偏移撤单执行逻辑
    :param order_convert:
    :param hft_context:
    :param order:
    :param tick:
    :return:
    """
    order_status = order["OrderStatus"]
    # 只处理挂单,非挂单直接跳过
    if order_status not in ["5"]:
        return
    remain_volume = order["VolumeTotalOriginal"] - order["VolumeTraded"]
    if remain_volume < 1:
        logger.info(f"订单:{order['OrderLocalID']}无剩余未成交数量,无需重新发单")
        return

    # 针对byte类型的code进行转换
    code = tick["code"]
    if not isinstance(code, str):
        code = code.decode("utf-8")

    price = tick["price"]
    direction = str(order["Direction"])
    # 计算发单价格
    order_price = order_convert.generate_order_price(direction, price, code)
    # 判断需要触发的指令方向
    if direction == "0":
        order_id = hft_context.stra_buy(code, order_price, remain_volume, flag=order_convert.config.order_type)
    else:
        order_id = hft_context.stra_sell(code, order_price, remain_volume, flag=order_convert.config.order_type)

    logger.info(f"order_id:{order_id}")
