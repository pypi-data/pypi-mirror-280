# -*- coding: utf-8 -*-
"""
@Time ： 2024/05/30 15:00
@Auth ： yuslience
@File ： InitLogger.py
@IDE ： CLion
@Motto: Emmo......
"""
import sys
from loguru import logger


def init_logger(log_file: str, level: str = "INFO"):
    """
    设置并返回一个日志记录器。

    :param log_file: 日志文件路径
    :param level: 日志级别，默认为 "INFO"
    :return: 配置好的 logger 对象
    """
    # 创建一个新的 logger 对象
    new_logger = logger.bind()

    # 移除默认的日志配置
    new_logger.remove()

    # 添加控制台输出
    new_logger.add(sys.stdout,
                   level=level,
                   colorize=True,
                   format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
                   )

    # 添加文件输出
    new_logger.add(log_file,
                   level=level,
                   format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} - {message}",
                   rotation="10 MB"
                   )

    return new_logger


if __name__ == '__main__':
    log_file_path = "../logs/trade_center_example.log"
    custom_logger = init_logger(log_file_path)
    custom_logger.info("This is a test log message.")