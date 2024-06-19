# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/12 14:28
@Auth ： yuslience
@File ： stringUtils
@IDE ： PyCharm
@Motto: Emmo...
"""
from typing import Dict
import datetime as dt
import arrow
import pandas as pd
from datetime import datetime, timedelta, time

# 历史所有节假日
ALL_HOLIDAYS = ["20240101",
                "20240212",
                "20240213",
                "20240214",
                "20240215",
                "20240216",
                "20240404",
                "20240405",
                "20240501",
                "20240502",
                "20240503",
                "20240610",
                "20240916",
                "20240917",
                "20241001",
                "20241002",
                "20241003",
                "20241004",
                "20241007"]


def get_cur_hour():
    """ 获取当前小时时间 """
    return datetime.now().hour


def get_cur_datetime() -> str:
    """ 获取当前时间 """
    return str(datetime.now()).split(".")[0]


def get_cur_date() -> str:
    """ 获取当前时间 """
    return str(datetime.now().date()).replace("-", "")


def get_yesterday_date() -> str:
    """ 获取当前时间 """
    return str(datetime.now().date() + timedelta(days=-1)).replace("-", "")


def get_tomorrow_date() -> str:
    """ 获取明天日期 """
    return str(datetime.now().date() + timedelta(days=1)).replace("-", "")


def format_date_str(date_str: str):
    """
    将日期字符串从'YYYYMMDD'格式转换为'YYYY-MM-DD'格式。
    参数:
    - date_str (str): 原始日期字符串，格式为'YYYYMMDD'。
    返回:
    - str: 转换后的日期字符串，格式为'YYYY-MM-DD'。
    """
    try:
        # 尝试解析日期字符串
        date_obj = datetime.strptime(date_str, "%Y%m%d")
        # 转换为需要的格式
        formatted_date = date_obj.strftime("%Y-%m-%d")
        return formatted_date
    except ValueError as e:
        # 处理可能的错误，例如如果输入的日期格式不正确
        print(f"Error converting date: {e}")
        return None


def generate_full_timestamp(tick: Dict):
    """ 拼接时间 """
    trading_day = tick["TradingDay"]
    update_time = tick["UpdateTime"]
    update_millisec = tick["UpdateMillisec"]
    # 将日期、时间和毫秒合并成一个完整的时间戳字符串
    full_timestamp = f"{trading_day[:4]}-{trading_day[4:6]}-{trading_day[6:8]} {update_time}.{update_millisec}"
    return full_timestamp


def is_weekday():
    """ 判断是否为工作日 """
    # 获取今天的日期
    today = datetime.now()
    # 判断今天是不是周末（周六是5，周日是6）
    return today.weekday() < 5


def yesterday_is_weekday():
    """ 获取昨天的日期 """
    yesterday = datetime.now() + timedelta(days=-1)
    # 判断昨天是不是周末（周六是5，周日是6）
    return yesterday.weekday() < 5


def init_cur_year_weekdays():
    """ 生成今年的所有工作日 """
    # 获取当前年份
    current_year = datetime.now().year

    # 初始化日期列表
    date_list = []
    # 定义年份的起始和结束日期
    start_date = dt.date(current_year, 1, 1)
    end_date = dt.date(current_year, 12, 31)

    # 遍历日期，添加周一到周五的日期到列表
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5:  # 0-4对应周一到周五
            date_list.append(current_date.strftime("%Y%m%d"))
        current_date += timedelta(days=1)
    return date_list


def is_trading_time():
    """
    判断当前是否为交易时间
    :return:
    """
    # 获取当前时间，不包含日期
    current_time = datetime.now().time()
    # 白盘时间
    morning_start = time(8, 55)
    morning_end = time(15, 16)
    # 夜盘时间
    evening_start = time(20, 55)
    evening_end = time(23, 59)  # 23:59 表示晚上的结束时间
    # 凌晨时间
    midnight_start = time(0, 0)  # 凌晨的结束时间
    midnight_end = time(2, 31)  # 凌晨的结束时间

    # -------------------------- 交易日白天时间判断 --------------------------
    if morning_start <= current_time <= morning_end:
        # 是交易日
        if is_weekday() and get_cur_date() not in ALL_HOLIDAYS:
            return True
    # -------------------------- 夜盘时间判断  ------------------------------
    elif evening_start <= current_time <= evening_end:
        # 是交易日
        if is_weekday() and get_cur_date() not in ALL_HOLIDAYS:
            # 明天不是节假日
            if get_tomorrow_date() not in ALL_HOLIDAYS:
                return True
    # -------------------------- 凌晨交易时间 -------------------------------
    elif midnight_start <= current_time <= midnight_end:
        # 昨天是交易日
        if yesterday_is_weekday() and get_yesterday_date() not in ALL_HOLIDAYS:
            # 今天不是节假日
            if get_cur_date() not in ALL_HOLIDAYS:
                return True
    else:
        return False


def get_this_day_tomorrow_date(current_date_str):
    # 将字符串格式的日期转换成日期对象
    current_date = datetime.strptime(current_date_str, "%Y%m%d")
    # 计算明天的日期
    tomorrow_date = current_date + timedelta(days=1)
    # 将日期对象转换回字符串格式
    return tomorrow_date.strftime("%Y%m%d")


def convert_trading_time(weekday, raw_trading_time):
    """
    时间转换
    :param weekday:
    :param raw_trading_time:
    :return:
    """
    # 将日期字符串转换为日期对象
    date_obj = datetime.strptime(weekday, "%Y%m%d").date()

    # 解析交易时间段
    start_time_str, end_time_str = raw_trading_time.split('-')
    start_time = datetime.strptime(start_time_str, "%H:%M").time()
    end_time = datetime.strptime(end_time_str, "%H:%M").time()

    # 判断是否跨越午夜，并调整日期
    if end_time < start_time:  # 跨越午夜的情况
        end_date_obj = date_obj + timedelta(days=1)
    else:
        end_date_obj = date_obj

    # 设置开始和结束的完整日期时间
    start_datetime = datetime.combine(date_obj, start_time)
    end_datetime = datetime.combine(end_date_obj, end_time)

    # 格式化输出
    formatted_start = start_datetime.strftime("%Y-%m-%d %H:%M:%S")
    formatted_end = end_datetime.strftime("%Y-%m-%d %H:%M:%S")

    return f"{formatted_start}~{formatted_end}"


def days_difference(date_str: str):
    """ 计算日期差 """
    # 将字符串格式的日期转换为datetime对象
    date_given = datetime.strptime(date_str, "%Y%m%d")
    # 获取当前日期
    today = datetime.now()
    # 计算两个日期之间的差值
    delta = today - date_given
    return delta.days


def get_latest_3_year_trading_days() -> list:
    """ 获取近两年的工作日 """
    current_year = datetime.now().year
    start_date = f"{current_year - 1}-01-01"
    end_date = f"{current_year + 1}-12-31"

    # 使用 pandas 生成当前年份的所有工作日，并转换为 'YYYYMMDD' 格式
    business_days_auto = pd.bdate_range(start=start_date, end=end_date, freq='B').strftime('%Y%m%d').tolist()

    # 将国家规定的节假日去除掉
    return [day for day in business_days_auto if day not in ALL_HOLIDAYS]


def get_latest_effective_day(interval: int = 0):
    """
    根据当前日期倒推前第interval的工作日
    :return:
    """
    all_trading_days = get_latest_3_year_trading_days()
    index = 0
    # 获取当前日期
    cur_date = get_cur_date()
    if cur_date in all_trading_days:
        index = all_trading_days.index(cur_date)
    else:
        for day_index in range(len(all_trading_days) - 2):
            if all_trading_days[day_index] < cur_date < all_trading_days[day_index + 1]:
                index = day_index
                break

    return all_trading_days[index - interval]


def time_str_to_time(time_str: str):
    """
    将时间字符串转为Arrow对象
    :param time_str: 153010 格式,不够6位的用0补齐,超过6位抛出异常
    :return:
    """
    if len(time_str) < 6:
        time_str = f"{'0' * (6 - len(time_str))}{time_str}"
    elif len(time_str) > 6:
        raise Exception(f"时间长度大于6位,无法进行转换,请处理~")

    # 将字符串转换为arrow.Arrow对象
    arrow_obj = arrow.get(time_str, "HHmmss")

    return arrow_obj.time()
