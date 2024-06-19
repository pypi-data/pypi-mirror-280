# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/12 14:28
@Auth ： yuslience
@File ： stringUtils
@IDE ： PyCharm
@Motto: Emmo...
"""
import inspect
import json
import re
import yaml
from typing import Dict
from datetime import datetime


def formatData(rsp) -> Dict:
    """ 格式化数据
    :param rsp:
    :return:
    """
    formatted_rsp = {}
    if rsp:
        for name, value in inspect.getmembers(rsp):
            # 筛选出属性
            if name[0].isupper():
                formatted_rsp[name] = value
    return formatted_rsp


def parse_product_id_from_symbol(symbol: str):
    """
    由合约名称解析品种信息
    :param symbol:
    :return:
    """
    # 期货品种信息
    if len(symbol) <= 6:
        product_id = re.sub('\d+$', '', symbol)
    # 期权品种信息
    else:
        product_id = re.match(r'^\D+', symbol).group(0)
    return product_id


def parse_symbol_from_option(raw_symbol: str):
    """
    由期权名称中解析合约名
    :param raw_symbol:
    :return:
    """
    if "-" not in raw_symbol:
        symbol = re.sub('\d+$', '', raw_symbol)
    else:
        execute_price = raw_symbol.split("-")[-1]
        symbol = raw_symbol.replace(f"-{execute_price}", "")
    return symbol


def rename_futures_symbol(symbol: str):
    """
    重命名合约名称
    :param symbol:
    :return:
    """
    res = re.compile(r'^[A-Za-z]+\d{3}$').match(symbol)
    if res:
        cur_year = datetime.now().year % 1000
        symbol_year_name = symbol[-3]
        if symbol_year_name == "0":
            res_symbol = f"{symbol[:-3]}{cur_year + 1}{symbol[-2:]}"
        else:
            res_symbol = f"{symbol[:-3]}{str(cur_year)[0]}{symbol[-3:]}"
    else:
        res_symbol = symbol
    return res_symbol


def rename_options_symbol(input_str):
    # 正则表达式匹配
    match = re.match(r'([A-Za-z]+[0-9]{3})([PC])([0-9]+)$', input_str)
    if not match:
        return input_str  # 如果不匹配，返回 None 或适当的错误处理

    # 提取各部分
    prefix = match.group(1)  # 'ZC407'
    middle = match.group(2)  # 'P'
    suffix = match.group(3)  # '990'

    # 假设这是你的处理函数，它将 'ZC407' 转换为 'ZC2407'
    # 处理 prefix
    new_prefix = rename_futures_symbol(prefix)
    # 重新组合字符串
    new_str = f"{new_prefix}{middle}{suffix}"
    return new_str


def make_full_contract_name(symbol: str) -> str:
    """
    由原始合约名称解析合约全称
    :param symbol:
    :return:
    """
    # ------------------ 期货合约名称修正 ------------------
    if len(symbol) <= 5:
        symbol = rename_futures_symbol(symbol)

    # ------------------ 期权合约名称修正 ------------------
    elif len(symbol) > 6:
        if "-" not in symbol:
            symbol = rename_options_symbol(symbol)
    return symbol


def dump_to_json_file(dest_path: str, data: dict):
    """ 落地数据至json文件 """
    try:
        with open(dest_path, "w", encoding="UTF-8") as fp:
            fp.write(json.dumps(data, indent=4))
    except Exception as err:
        print(f"落地json报错:{dest_path} Err:{err}")


def dump_to_yaml_file(dest_path: str, data: dict):
    """ 落地数据至yaml文件 """
    try:
        with open(dest_path, "w", encoding="UTF-8") as fp:
            yaml.dump(data, fp, default_flow_style=False, allow_unicode=True)
    except Exception as err:
        print(f"落地yaml报错:{dest_path} Err:{err}")
