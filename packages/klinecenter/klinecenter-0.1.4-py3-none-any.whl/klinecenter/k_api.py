"""总接口"""

import requests
import pandas as pd
from functools import lru_cache
import json


USER_TOKEN = "5befb03c-a4c1-4018-af64-bb07d5273527"  # 输入登陆页面生成的user_token

base_url = "http://127.0.0.1:5008/api/"


def user_session():
    session = requests.Session()  # 使用 Session 对象以保持 cookies
    headers = {
        "X-usertoken": USER_TOKEN,
    }
    session.headers.update(headers)
    # print(session.headers)
    # r = session.get(base_url+'/get-csrf-token')
    # print(type(r.text))# ['csrf_token']
    # print(r.json()['csrf_token'])# ['csrf_token']
    # headers = {
    #     "X-CSRFToken": r.json()['csrf_token'],
    # }
    # session.headers.update(headers)
    # print(session.headers)
    # print(headers)
    # r = session.post(base_url+'/ver-csrf-token')
    # r = session.post(base_url+'/get-csrf-token')
    # print(r.text)

    return session


session = user_session()


def get_stock_kline(
    stock: str = "SZ.000001",
    start: str = "19700101",
    end: str = "22220101",
    kline_type: str = "day",
    adjust: str = "",
) -> pd.DataFrame:
    """
    获取沪深股票的k线数据
    :param stock: 股票代码
    :type stock: str
    :param start: 开始日期
    :type start: str
    :param end: 结束日期
    :type end: str
    :param kline_type: k线类型,choice of {'day', 'week', 'month','minute','5m','30m'}
    :type kline_type: str
    :param adjust: choice of {"qfq": "前复权", "hfq": "后复权", "": "不复权"}
    :type adjust: str
    :return: k线行情
    :rtype: pandas.DataFrame
    """
    url = base_url + "getstock"
    # print(url)
    params = {
        "stock": stock,
        "start": start,
        "end": end,
        "kline_type": kline_type,
        "adjust": adjust,
    }
    d = session.get(url, json=params)
    d_json = d.json()
    # print(d_json)
    # d = pd.DataFrame(json.loads(d_json['data']))
    d = pd.DataFrame(columns=d_json["col"], data=d_json["val"])
    # print(d)
    return d


# d = get_stock_kline(start="20200101")
# print(d)


def get_index_kline(
    index_code: str = "SH.000001",
    start: str = "19700101",
    end: str = "22220101",
    kline_type: str = "day",
) -> pd.DataFrame:
    """
    获取沪深股票指数的k线数据
    :param index_code: 沪深股票指数代码
    :type index_code: str
    :param start: 开始日期
    :type start: str
    :param end: 结束日期
    :type end: str
    :param kline_type: k线类型,choice of {'day', 'week', 'month','minute','5m','30m'}
    :type kline_type: str
    :return: 沪深股票指数的k线行情
    :rtype: pandas.DataFrame
    """
    url = base_url + "getindex"
    params = {
        "index_code": index_code,
        "start": start,
        "end": end,
        "kline_type": kline_type,
    }
    d = session.get(url, json=params)
    d_json = d.json()
    d = pd.DataFrame(columns=d_json["col"], data=d_json["val"])
    return d


def get_index_contains(index_code: str = "SH.000001") -> pd.DataFrame:
    """
    获取沪深股票指数的成份股
    :param index_code: 沪深股票指数代码
    :type index_code: str
    :return: 沪深股票指数的成分股表格
    :rtype: pandas.DataFrame
    """
    url = base_url + "getindexcontains"
    params = {"index_code": index_code}
    d = session.get(url, json=params)
    d_json = d.json()
    d = pd.DataFrame(columns=d_json["col"], data=d_json["val"])
    return d


def get_all_index_name() -> pd.DataFrame:
    """
    获取所有沪深股票指数的名称与代码对应表
    :return: 所有指数名称与代码对应表
    :rtype: pandas.DataFrame
    """
    url = base_url + "getallindex"
    d = session.get(url)
    d_json = d.json()
    d = pd.DataFrame(columns=d_json["col"], data=d_json["val"])
    return d


def get_stock_finance(
    stock: str = "SZ.000001",
    report_type: str = "balance",
    start: str = "19700101",
    end: str = "22220101",
) -> pd.DataFrame:
    """
    获取指定代码的财务数据
    :param stock: 股票代码
    :type stock: str
    :param report_type: 报表类型,choice of {'balance':'资产负债表','profit':'利润表','cash_flow':'现金流量表','financial_abstract':'财务指标'}
    :type stock: str
    :param start: 开始日期
    :type start: str
    :param end: 结束日期
    :type end: str
    :return: 财务报表
    :rtype: pandas.DataFrame
    """
    url = base_url + "getfinance"
    params = {
        "stock": stock,
        "report_type": report_type,
        "start": start,
        "end": end,
    }
    d = session.get(url, json=params)
    d_json = d.json()
    d = pd.DataFrame(columns=d_json["col"], data=d_json["val"])
    return d


def get_all_industry_name() -> pd.DataFrame:
    """
    获取所有沪深股票行业的名称与代码对应表
    :return: 行业名称与代码对应表
    :rtype: pandas.DataFrame
    """
    url = base_url + "getallindustry"
    d = session.get(url)
    d_json = d.json()
    d = pd.DataFrame(columns=d_json["col"], data=d_json["val"])
    return d


def get_industry_contains(industry_code: str = "801890") -> pd.DataFrame:
    """
    获取沪深股票行业的成份股
    :param industry_code: 沪深股票行业代码
    :type industry_code: str
    :return: 行业成分股表格
    :rtype: pandas.DataFrame
    """
    url = base_url + "getindustrycontains"
    params = {"industry_code": industry_code}
    d = session.get(url, json=params)
    d_json = d.json()
    d = pd.DataFrame(columns=d_json["col"], data=d_json["val"])
    return d


def get_industry_kline(
    industry_code: str = "801890",
    start: str = "19700101",
    end: str = "22220101",
    kline_type: str = "day",
) -> pd.DataFrame:
    """
    获取行业的k线数据
    :param industry_code: 行业代码
    :type industry_code: str
    :param start: 开始日期
    :type start: str
    :param end: 结束日期
    :type end: str
    :param kline_type: k线类型,choice of {'day', 'week', 'month',}
    :type kline_type: str
    :return: 行业的k线行情
    :rtype: pandas.DataFrame
    """
    url = base_url + "getindustry"
    params = {
        "industry_code": industry_code,
        "start": start,
        "end": end,
        "kline_type": kline_type,
    }
    d = session.get(url, json=params)
    d_json = d.json()
    d = pd.DataFrame(columns=d_json["col"], data=d_json["val"])
    return d


def get_all_common_macro() -> pd.DataFrame:
    """
    获取常用宏观指标名称与代码对应表
    :return: 宏观指标与名称
    :rtype: pandas.DataFrame
    """
    url = base_url + "getallcommonmacro"
    d = session.get(url)
    d_json = d.json()
    d = pd.DataFrame(columns=d_json["col"], data=d_json["val"])
    return d



def get_macro_indicator(indicator: str = "CPI") -> pd.DataFrame:
    """
    获取宏观指标数据
    :param indicator: 宏观指标代码
    :type indicator: str
    :return: 宏观指标数据表格
    :rtype: pandas.DataFrame
    """
    url = base_url + "getmacroindicator"
    params = {"indicator": indicator}
    d = session.get(url, json=params)
    d_json = d.json()
    d = pd.DataFrame(columns=d_json["col"], data=d_json["val"])
    return d



