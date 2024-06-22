# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/10 19:00
@Auth ： yuslience
@File ：redisApi.py
@IDE ：CLion
@Motto: Emmo......
"""
import redis
import orjson


class RedisClient:
    def __init__(self, host='localhost', db=0, port=6379, password=None):
        """
        初始化Redis连接
        :param host: Redis服务器地址
        :param port: Redis服务器端口
        :param password: Redis连接密码，如果无需密码则为None
        """
        self.client = redis.Redis(host=host, port=port, db=db, password=password, decode_responses=True)
        self.trim_data = True  # 是否剪切数据标识

    def select_db(self, db: int):
        """ 切换db """
        self.client.select(db)

    def set_data(self, key, value):
        """
        写入数据到Redis
        :param key: 键
        :param value: 值，可以是dict、list等，将会被JSON序列化
        """
        if isinstance(value, (dict, list)):  # 检查value是否是字典或列表
            value = orjson.dumps(value)        # 序列化为JSON字符串
        self.client.set(key, value)

    def get_data(self, key):
        """
        从Redis读取数据
        :param key: 键
        :return: 对应键的值，如果是JSON字符串，则返回反序列化的数据
        """
        value = self.client.get(key)
        try:
            # 尝试反序列化，如果是有效的JSON字符串，则返回原始数据结构
            return orjson.loads(value)
        except (TypeError, orjson.JSONDecodeError):
            # 如果不是JSON字符串或者value为None，返回原始字符串值
            return value

    def hset(self, name, key, value):
        """
        向哈希中添加键值对
        :param name: 哈希的名称
        :param key: 键
        :param value: 值
        """
        if isinstance(value, (dict, list)):  # 检查value是否是字典或列表
            value = orjson.dumps(value)        # 序列化为JSON字符串
        self.client.hset(name, key, value)

    def hget(self, name, key):
        """
        从哈希中获取值
        :param name: 哈希的名称
        :param key: 键
        :return: 键对应的值
        """
        value = self.client.hget(name, key)
        try:
            # 尝试反序列化，如果是有效的JSON字符串，则返回原始数据结构
            return orjson.loads(value)
        except (TypeError, orjson.JSONDecodeError):
            # 如果不是JSON字符串或者value为None，返回原始字符串值
            return value

    def hgetall(self, name):
        """
        获取哈希表中的所有键值对，并尝试将值反序列化为Python对象
        :param name: 哈希表的名称
        :return: 一个字典，其中包含所有键及其反序列化的值
        """
        # 从Redis获取整个哈希表
        hash_dict = self.client.hgetall(name)
        result = {}

        for key, value in hash_dict.items():
            if value is not None:
                try:
                    # 尝试反序列化值
                    result[key] = orjson.loads(value)
                except (TypeError, orjson.JSONDecodeError):
                    # 如果值不是有效的JSON，或者反序列化失败，则保留原始值
                    result[key] = value.decode('utf-8')
            else:
                # 如果值是None，可能是因为键不存在
                result[key] = None

        return result

    def push_data(self, key, value, method='rpush'):
        """
        将数据推送到Redis列表中
        :param key: 列表的键
        :param value: 要推送的值，可以是dict、list等，将会被JSON序列化
        :param method: 推送方法，'lpush' 或 'rpush'
        """
        if isinstance(value, (dict, list)):  # 检查value是否是字典或列表
            value = orjson.dumps(value)        # 序列化为JSON字符串
        if method == 'lpush':
            self.client.lpush(key, value)
        elif method == 'rpush':
            self.client.rpush(key, value)
        else:
            raise ValueError("Invalid push method. Use 'lpush' or 'rpush'.")

    def blpop_data(self, queues: list, timeout=0):
        """ 获取数据 """
        return self.client.blpop(queues, timeout=timeout)

    def del_key(self, key_name: str):
        """ 清空信号队列 """
        return self.client.delete(key_name)

    def get_list(self, key, start=0, end=-1):
        """
        从Redis获取列表数据
        :param key: 列表的键
        :param start: 起始索引
        :param end: 结束索引
        :return: 列表范围内的元素，尝试反序列化JSON字符串
        """
        items = self.client.lrange(key, start, end)
        result = []
        for item in items:
            try:
                # 尝试反序列化，如果是有效的JSON字符串，则返回原始数据结构
                result.append(orjson.loads(item))
            except orjson.JSONDecodeError:
                # 如果不是JSON字符串，保留原始值
                result.append(item)
        return result

    def publish_data(self, channel, message):
        """
        发布消息到指定的频道
        :param channel: 频道名称
        :param message: 消息内容，可以是dict，将会被JSON序列化
        """
        if isinstance(message, (dict, list)):  # 检查message是否是字典或列表
            message = orjson.dumps(message)      # 序列化为JSON字符串
        self.client.publish(channel, message)

    def subscribe(self, channels):
        """
        订阅一个或多个频道的消息
        :param channels: 单个频道字符串或多个频道的列表
        """
        if isinstance(channels, str):
            channels = [channels]  # 如果是单个频道，转换为列表
        pubsub = self.client.pubsub()
        pubsub.subscribe(*channels)
        return pubsub  # 返回pubsub对象以便外部处理消息

    def get_all_keys(self):
        """ Get Db All Keys """
        return self.client.keys()

    def get_queue_length(self, key: str):
        """ Get Queue Length """
        return self.client.llen(key)

    def get_md_data(self, key: str, queue_length):
        """ Get Keys From Db """
        data_res = []
        try:
            # Debug Mode
            if not self.trim_data:
                queue_length = 2
            if queue_length > 30000:
                queue_length = 29999
                data_res = self.client.lrange(key, 0, queue_length)
            else:
                data_res = self.client.lrange(key, 0, queue_length)
            if self.trim_data:
                self.client.ltrim(key, queue_length, -1)
        except Exception as err:
            print(err)

        return [orjson.loads(data) for data in data_res]
