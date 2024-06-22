# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/10 19:20
@Auth ： yuslience
@File ：listeningKit.py
@IDE ：CLion
@Motto: Emmo......
"""
import threading
import orjson
from loguru import logger

from proredis.redisApi import RedisClient


class ListeningKit:
    """ 订阅逻辑 """

    def __init__(self, host='localhost', db=0, callback: callable = None):
        self.redis_client = RedisClient(host=host, db=db)
        self.callback_func = callback

    def start_channel_listener(self, channels: list):
        """启动订阅行情和交易频道推送的线程"""
        t2 = threading.Thread(target=self.run_channel_listener, args=(channels,))
        t2.start()

    def run_channel_listener(self, channels: list):
        """ 订阅指定频道 """
        pubsub = self.redis_client.subscribe(channels)
        logger.info(f"订阅频道:{channels} 成功,开始监听~")
        # 监听消息
        for message in pubsub.listen():
            if message['type'] != 'message':
                continue
            # 处理订阅返回消息
            data = orjson.loads(message['data'])
            if self.callback_func:
                self.callback_func(data)

    def start_queue_listener(self, queues: list, timeout=0):
        """启动监听队列推送的线程"""
        t3 = threading.Thread(target=self.run_queue_listener, args=(queues, timeout))
        t3.start()

    def run_queue_listener(self, queues: list, timeout=0):
        """从指定队列中阻塞获取数据"""
        logger.info(f"开始监听队列:{queues}，超时设置:{timeout}秒")
        while True:
            result = self.redis_client.blpop_data(queues, timeout=timeout)
            if result:
                queue, data = result
                data = orjson.loads(data)
                if self.callback_func:
                    self.callback_func(data)
