# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/8 21:23
@Auth ： yuslience
@File ：OrderManagerCenter.py
@IDE ：CLion
@Motto: Emmo......
"""
from tradewinpy.tradecenter import cancel_order_by_price_offset
from tradewinpy.tradecenter import cancel_order_by_time_offset
from tradewinpy.tradecenter import resend_order_by_cancelled_order


class OrderManagerCenter:
    """ 订单中心 """
    sub_types = ["order", "open_orders"]

    def __init__(self, config, listening_kit, hft_context, order_convert, tracing_account_td_api, logger):
        # 参数配置
        self.config = config
        # 监听模块
        self.listening_kit = listening_kit
        # 高频上下文管理器
        self.hft_context = hft_context
        # 订单转化
        self.order_convert = order_convert
        # 跟单账户td_api
        self.tracing_account_td_api = tracing_account_td_api
        self.logger = logger
        # 当前最新tick
        self.tick = None
        # 平仓标识:处于有效交易时间范围内时,此标识为False
        self.stop_tracing_flag = False
        # 当前最新挂单
        self.open_orders = {}
        # 生成订阅接口,方便后续过滤pub推送
        self.sub_types_with_account = [f"{self.config.tracing_account}_{data_type}" for data_type in self.sub_types]
        # 添加回调并启动订阅逻辑
        self.listening_kit.add_callback(self.handle_order_message)
        self.listening_kit.start_subscriptions(self.config.tracing_account, self.sub_types)

    def update_tracing_flag(self, tracing_flag: bool):
        """ """
        self.stop_tracing_flag = tracing_flag

    def on_tick_update(self, newTick: dict):
        """ tick回调 """
        self.tick = newTick

        if not self.open_orders or self.stop_tracing_flag:
            return
        try:
            if self.config.time_offset > 0:
                # 执行时间撤单
                cancel_order_by_time_offset(newTick, self.open_orders, self.tracing_account_td_api, self.config)

            if self.config.price_offset > 0:
                # 执行价格偏移撤单
                cancel_order_by_price_offset(newTick, self.open_orders, self.tracing_account_td_api, self.config)

        except Exception as err:
            self.logger.error(err)

    def handle_order_message(self, raw_data: dict):
        """ 处理成交回报信息 """
        msg_type = raw_data["msg_type"]
        # 主账户成交单
        if msg_type not in self.sub_types_with_account or self.stop_tracing_flag:
            return
        # 获取对应的频道详情
        date_type = msg_type.split('_', 1)[1]

        # 如果收到的数据是order
        if date_type == self.sub_types[0]:
            order = raw_data["data"]
            try:
                # 执行重发指令
                resend_order_by_cancelled_order(self.tick, order, self.hft_context, self.order_convert)
            except Exception as err:
                self.logger.error(err)

        # 如果收到的是挂单详情
        elif date_type == self.sub_types[1]:
            # 执行更新方法
            self.open_orders = raw_data["data"]


