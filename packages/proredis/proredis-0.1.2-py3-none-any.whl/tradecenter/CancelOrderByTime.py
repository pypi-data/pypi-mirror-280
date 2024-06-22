# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/8 21:24
@Auth ： yuslience
@File ：CancelOrderByTime.py
@IDE ：CLion
@Motto: Emmo......
"""
import arrow
from loguru import logger


def cancel_order_by_time_offset(tick: dict, open_orders: dict, tracing_account_td_api, config):
    """
    时间偏移撤单执行逻辑
    :param config:
    :param tracing_account_td_api:
    :param open_orders:
    :param tick:
    :return:
    """
    # 对字节类型进行解码操作
    raw_symbol = tick["code"]
    if not isinstance(raw_symbol, str):
        raw_symbol = raw_symbol.decode("utf-8")
    # 获取当前code对应的未成交订单
    order_symbol = "".join(raw_symbol.split(".")[1:])
    cur_code_orders = open_orders.get(order_symbol, {})
    if not cur_code_orders:
        return
    # 获取tick时间
    tick_time = make_date_time(str(tick["action_date"]), str(tick["action_time"])[:-3])
    # 遍历所有的挂单
    for order_local_id, order in cur_code_orders.items():
        # 获取挂单时间: 'InsertDate': '20240509', 'InsertTime': '09:37:47'
        order_time = make_date_time(order["InsertDate"], order["InsertTime"].replace(":", ""))

        # 判断发单时间时候超过预设时间
        if cal_time_difference(tick_time, order_time) > config.time_offset:
            logger.info(f"Cancel OrderId By TimeOffset: {order_local_id}")
            exchange = order["ExchangeID"]
            symbol = order["InstrumentID"]
            order_sys_id = order["OrderSysID"]
            cancel_order_res = tracing_account_td_api.order_cancel1(exchange, symbol, order_sys_id)
            logger.info(f"Cancel OrderId By TimeOffset Res: {cancel_order_res}")


def make_date_time(action_date: str, action_time: str):
    """ 生成tick详细时间 """
    # 标准化时间格式: 235220500 这种9位的格式
    if len(action_time) < 6:
        real_action_time = f"{'0' * (6 - len(action_time))}{action_time}"
    else:
        real_action_time = f"{action_time}"
    # 转换时间
    arrow_time = arrow.get(real_action_time, "HHmmss")
    # 转换日期
    arrow_date = arrow.get(f"{action_date}", "YYYYMMDD")

    # 合并日期和时间
    return arrow_date.replace(hour=arrow_time.hour,
                              minute=arrow_time.minute,
                              second=arrow_time.second)


def cal_time_difference(tick_time, order_time) -> int:
    """
    计算时间差
    :param tick_time:
    :param order_time:
    :return: 整数类型的秒
    """
    # 计算时间差，返回 timedelta 对象
    time_difference = tick_time - order_time

    # 获取时间差的秒数
    return time_difference.total_seconds()
